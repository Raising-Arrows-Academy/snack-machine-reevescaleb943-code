[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21205008)
# Snack Machine Demo

Welcome to the Snack Machine Demo project! This is a Python programming exercise designed to help you learn the basics of Python programming by building a virtual snack machine.

## Getting Started

### Prerequisites
- This project is designed to run in GitHub Codespaces
- No local installation required!

### How to Run the App

#### Step 1: Open in Codespace
1. Click the green "Code" button on GitHub
2. Select "Codespaces" tab
3. Click "Create codespace on main" (or your current branch)
4. Wait for the codespace to load (this may take a few minutes the first time)

#### Step 2: Run the Python App
Once your codespace is ready, you can run the app in two ways:

**Option A: Using the Terminal**
1. Open the terminal (Terminal → New Terminal from the menu)
2. Type the following command and press Enter:
   ```bash
   python main.py
   ```

**Option B: Using VS Code's Run Button**
1. Open the `main.py` file
2. Click the "Run Python File" button (▶️) in the top-right corner
3. Or press `Ctrl+F5` (Windows/Linux) or `Cmd+F5` (Mac)

#### Step 3: Run the Tests (Optional)
To verify that your code is working correctly, you can run the automated tests:

1. Open the terminal (Terminal → New Terminal from the menu)
2. Type the following command and press Enter:
   ```bash
   pytest
   ```
   Or for more detailed output:
   ```bash
   pytest -v
   ```

All tests should pass! If you make changes to the code, run the tests again to make sure everything still works.

### What You Should See
When you run the app, you should see:
```
🎯 Welcome to the Python Snack Machine!
=============================================

📋 Available snacks:
1. 🍿 Chips - $1.50
2. 🍫 Chocolate Bar - $2.00
3. 🥜 Granola Bar - $1.25
4. 🥤 Soda - $1.75
------------------------------
Enter the number of your choice (1-4):
```

## Project Structure
```
snack-machine/
├── main.py              # Main application file (start here!)
├── test_main.py         # Automated tests for the app
├── requirements.txt     # Python dependencies
├── .devcontainer/       # Codespace configuration
└── README.md           # This file
```

## Next Steps
Now that you have the basic setup working, you can start building your snack machine! Here are some ideas:
- Add a menu of snacks with prices
- Create functions to handle money input
- Add inventory tracking
- Build a user interface

## Troubleshooting

### If the app doesn't run:
1. Make sure you're in the correct directory (you should see `main.py` in the file explorer)
2. Try running `python3 main.py` instead of `python main.py`
3. Check that your codespace has finished loading completely

### Need Help?
- Ask your instructor
- Check the VS Code terminal for error messages
- Make sure all files are saved before running

Happy coding! 🐍🥤
