# Python Projects
# 1. 🧮 Python Calculator

A simple command-line calculator built with Python.

## Features
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- ❌ Error handling

## How to Run
```bash
python calculator.py
```
# 2. 🎮 Number Guessing Game

A fun and interactive command-line game where you try to guess a randomly generated number! Test your luck and intuition!

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Game](https://img.shields.io/badge/type-game-orange.svg)

## 🎯 About The Game

Try to guess a secret number between 1 and 100 in 10 attempts or less! After each guess, you'll get hints whether your guess is too high or too low. The fewer attempts you take, the better!

## ✨ Features

- 🎲 **Random Number Generation** - New number each game
- 🎯 **Limited Attempts** - 10 tries to guess correctly
- 💡 **Smart Hints** - Get "too high" or "too low" feedback
- ❌ **Input Validation** - Handles invalid inputs gracefully
- 🔄 **Replay Option** - Play multiple rounds
- 🎨 **Colorful Interface** - Engaging text-based UI
- 📊 **Attempt Tracking** - Know how many tries you've used

## 🚀 How to Play

### Prerequisites
- Python 3.x installed ([Download Python](https://www.python.org/downloads/))

### Installation & Running

**Option 1: Clone and Run**
```bash
# Clone the repository
git clone https://github.com/sakshidangi2006/python-projects.git

# Navigate to directory
cd python-projects-

# Run the game
python guessing_number.py
```

**Option 2: Quick Download**
1. Download `guessing_number.py`
2. Open terminal/command prompt
3. Run: `python guessing_number.py`

**Option 3: GitHub Codespaces**
1. Click **Code** → **Codespaces**
2. Create new codespace
3. Run: `python guessing_number.py`

## 🎮 Gameplay Example

```
==================================================
🎮 Welcome to the Number Guessing Game!
==================================================

🎯 I'm thinking of a number between 1 and 100
🎮 You have 10 attempts to guess it!

🤔 Attempt 1/10 - Enter your guess: 50
📈 Too low! Try a higher number.

🤔 Attempt 2/10 - Enter your guess: 75
📉 Too high! Try a lower number.

🤔 Attempt 3/10 - Enter your guess: 63
📈 Too low! Try a higher number.

🤔 Attempt 4/10 - Enter your guess: 69
==================================================
🎉 Congratulations! You guessed it in 4 attempts!
✨ The number was 69
==================================================

🔄 Do you want to play again? (yes/no): yes
```

## 🎲 Game Rules

1. 🎯 The computer picks a random number between 1 and 100
2. 🔢 You have 10 attempts to guess it
3. 💡 After each guess, you get a hint:
   - 📈 "Too low" - Guess higher
   - 📉 "Too high" - Guess lower
4. 🎉 Win by guessing correctly
5. 😢 Lose if you use all 10 attempts
6. 🔄 Play again as many times as you want!

## 🛠️ Code Structure

```python
# Main Functions
play_game()  # Single game session
main()       # Game loop with replay option
```

**Key Concepts Used:**
- `random.randint()` for number generation
- `while` loops for game logic
- `try-except` for error handling
- Conditional statements for hints

## 🔮 Future Enhancements

- [ ] Add difficulty levels (Easy: 1-50, Hard: 1-500)
- [ ] Implement score tracking
- [ ] Add timer/speed bonus
- [ ] Create leaderboard
- [ ] Add hint system (use a hint to narrow range)
- [ ] GUI version with Tkinter
- [ ] Multiplayer mode
- [ ] Save high scores to file

# 3. Todo List Application

This To-Do List application allows users to add, view, and delete tasks, with tasks being saved to a file so they persist even after the program is closed.

##  Features

- ➕ Add Tasks – Add new tasks to your list
- 📋 View Tasks – Display all saved tasks
- ✅ Complete Tasks – Mark task as completed
- ❌ Delete Tasks – Remove tasks by number
- 📊 View Statistics – Shows completion rate
- 🔍 Search Tasks – Search for a task
- 💾 File Storage – Tasks are saved in a file
- 🔄 Persistent Data – Tasks remain after restart
- ⚠️ Input Validation – Handles invalid inputs safely
- 🧠 Beginner-Friendly Logic

## 🚀 How to Play

### Prerequisites
- Python 3.x installed ([Download Python](https://www.python.org/downloads/))

### Installation & Running

**Option 1: Clone and Run**
```bash
# Clone the repository
git clone https://github.com/sakshidangi2006/python-projects.git

# Navigate to directory
cd python-projects-

# Run the game
python To_Do_List.py
```

## 📌 Sample Output
```
🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯
Welcome to Smart To-Do List Manager!
Stay organized and productive! 🚀
🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯🎯
================================================
               SMART TO-DO LIST
================================================

 MENU OPTIONS:
   1. ➕ Add New Task
   2. 📋 View All Tasks
   3. ✅ Complete Task
   4. 🗑️  Delete Task
   5. 📊 View Statistics
   6. 🔍 Search Tasks
   7. 🚪 Exit

  👉 Enter your choice(1-7): 1
  ==================================================
  ➕ ADD NEW TASK
  ==================================================

📝 Task title: complete python project

🎯 Priority Level:
   1. High 🔴
   2. Medium 🟡
   3. Low 🟢

Select priority (1-3): 2

✅ Task added successfully! (ID: 3)

⏸️  Press Enter to continue...
```

## 👤 Author

**Sakshi Dangi**

- 📧 Email: sakshidangi2006@gmail.com
- 💼 LinkedIn: [sakshidangi-633b2635b](https://www.linkedin.com/in/sakshidangi-633b2635b)
- 🌐 Portfolio: [sakshidangi2006.github.io/MyPortfolio](https://sakshidangi2006.github.io/MyPortfolio/)
- 🐱 GitHub: [@sakshidangi2006](https://github.com/sakshidangi2006)

## 🙏 Acknowledgments

- Built as a beginner Python project
## 🆘 Troubleshooting

**Problem: Game closes immediately**
- **Solution:** Run from terminal, not by double-clicking

**Problem: "ModuleNotFoundError: No module named 'random'"**
- **Solution:** `random` is built-in, ensure Python is correctly installed

**Problem: Input errors**
- **Solution:** Enter only numbers between 1-100

**Problem: Want to quit mid-game**
- **Solution:** Press `Ctrl+C` to exit

## 📊 Project Stats

- **Language:** Python
- **Difficulty:** Beginner
- **Version:** 1.0.0
- **Last Updated:** February 2026

## What I Learned
  
These projects helped me understand:
- ✅ Using Python's `random` module
- ✅ While loop implementation
- ✅ User input validation
- ✅ Functions in Python
- ✅ Exception handling
- ✅ Game logic and flow control
- ✅ Breaking loops with conditions
- ✅ Variable scope in functions
- ✅ Structuring Python program properly

## Technologies Used
- **Language:** Python 3.x
- **Module:** `random` (built-in)
- **No external dependencies required!**

<div align="center">

### ⭐ Star this repo if you enjoyed the game!

### 🎮 Happy Gaming! May the odds be in your favor! 🍀

**Made with ❤️ by Sakshi Dangi**

</div>
