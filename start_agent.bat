@echo off
setlocal EnableDelayedExpansion
echo ===================================================
echo   Autonomous AI Coder - Setup & Run Script
echo ===================================================
echo.

cd /d "%~dp0"

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH! 
    echo Please install Python 3.10+ from python.org and check "Add Python to PATH".
    pause
    exit /b
)

:: 2. Self-Healing Environment Check
if exist ".venv" (
    echo [CHECK] Checking existing virtual environment...
    call .venv\Scripts\activate >nul 2>&1
    
    :: Try to import dotenv to see ifenv is healthy
    python -c "import dotenv" >nul 2>&1
    if !errorlevel! neq 0 (
        echo [WARN] Virtual environment seems broken or missing dependencies.
        echo [FIX] Deleting old environment and starting fresh...
        deactivate >nul 2>&1
        rmdir /s /q ".venv"
    ) else (
        echo [OK] Environment looks good.
    )
)

:: 3. Create Virtual Environment if missing
if not exist ".venv" (
    echo [INFO] Creating virtual environment...
    python -m venv .venv
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to create virtual environment. 
        echo You might need to install the 'venv' module or reinstall Python.
        pause
        exit /b
    )
)

:: 4. Activate Virtual Environment
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b
)

:: 5. Install Dependencies (Always run to ensure updates)
echo [INFO] Installing/Updating dependencies...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b
)

:: Double check dotenv is installed
python -c "import dotenv" >nul 2>&1
if %errorlevel% neq 0 (
    echo [RETRY] Force installing python-dotenv...
    pip install python-dotenv
)

:: 6. Create .env if missing
if not exist ".env" (
    echo.
    echo [SETUP] .env file not found!
    echo Please enter your Kimi / Moonshot API Key below:
    set /p MOONSHOT_KEY="API Key: "
    echo MOONSHOT_API_KEY=!MOONSHOT_KEY! > .env
    echo [INFO] API Key saved to .env
)

:: 7. Run the Agent
echo.
echo ===================================================
echo   Starting the AI Agent...
echo   (This may take 10-20 minutes for the first step)
echo ===================================================
echo.

python autonomous_agent_demo.py --project-dir ./my_awesome_app --model kimi-k2-turbo-preview

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] The agent crashed. See the error message above.
)

echo.
echo [DONE] Press any key to exit.
pause >nul
