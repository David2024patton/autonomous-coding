@echo off
echo ===================================================
echo   Autonomous AI Coder - Setup & Run Script
echo ===================================================
echo.

cd /d "%~dp0"

:: 1. Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed! 
    echo Please install Python 3.10+ from python.org and try again.
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

:: 2. Create Virtual Environment if missing
if not exist ".venv" (
    echo [INFO] Creating virtual environment...
    python -m venv .venv
)

:: 3. Activate Virtual Environment
call .venv\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b
)

:: 4. Install Dependencies
echo [INFO] Installing/Updating dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b
)

:: 5. Create .env if missing
if not exist ".env" (
    echo.
    echo [SETUP] .env file not found!
    echo Please enter your Kimi / Moonshot API Key below:
    set /p MOONSHOT_KEY="API Key: "
    echo MOONSHOT_API_KEY=%MOONSHOT_KEY% > .env
    echo [INFO] API Key saved to .env
)

:: 6. Run the Agent
echo.
echo ===================================================
echo   Starting the AI Agent...
echo   (This may take 10-20 minutes for the first step)
echo ===================================================
echo.

python autonomous_agent_demo.py --project-dir ./my_awesome_app --model kimi-k2-turbo-preview

echo.
echo [DONE] The agent has finished or was paused.
pause
