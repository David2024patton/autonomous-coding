# AI Cloud Studio (Autonomous Coder)

This tool allows you to build complete, complex software applications just by writing a text description. It uses the **Kimi 2 (Moonshot AI)** model to write code, run tests, and build your app for you.

You **do not** need to know how to code to use this.

---

## 🚀 Quick Start (Windows)

### 1. Download & Install
1.  **Install Python**: Download and install Python (3.12 or newer) from [python.org](https://www.python.org/downloads/).
    *   **IMPORTANT**: Check the box that says **"Add Python to PATH"** during installation.
2.  **Download this Code**: Click the green "Code" button > "Download ZIP" and extract it to a folder on your computer.

### 2. Configure Your App
1.  Open the `prompts` folder.
2.  Open `app_spec.txt` with any text editor (Notepad is fine).
3.  **Delete everything** and write what you want to build. Be as detailed as possible!
    *   *Example:* "Build a website for my bakery. It needs a menu page, a contact form, and an admin login where I can upload photos of cakes..."
4.  Save the file.

### 3. Run It!
1.  Double-click the **`start_agent.bat`** file.
2.  It will ask for your **Moonshot API Key** the first time. Paste it in and press Enter.
    *   (Get a key here: [Moonshot Console](https://platform.moonshot.cn/console/api-keys))
3.  Sit back and wait!
    *   **Phase 1 (10-20 mins)**: The AI reads your `app_spec.txt` and plans the entire project. It might look like it's frozen - **it is not!** Let it think.
    *   **Phase 2 (Hours)**: It will start writing code file by file.

---

## 📂 Where is my App?

Once the agent starts working, go to the `generations/my_awesome_app` folder. You will see:
*   `feature_list.json`: The checklist of tasks the AI is working on.
*   `src/` or `app/`: The actual code being written.

## 🛠 Advanced Usage (Optional)

If you are technical or want to run it manually from a terminal:

```powershell
# Setup
pip install -r requirements.txt

# Run with Kimi Model
python autonomous_agent_demo.py --project-dir ./my_app --model kimi-k2-turbo-preview
```

## ❓ FAQ

**It says "Command blocked by security hook"?**
This is a safety feature. The AI tried to run a command we didn't explicitly allow. You can usually ignore this, or add the command to `security.py` if you know what you're doing.

**It stopped working/crashed?**
Just run `start_agent.bat` again! The AI saves its progress in `feature_list.json`. It will pick up exactly where it left off.
