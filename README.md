# 🐍 Snake 🐍 Water 💧 Gun 🔫 Game (Python)

A simple and fun command-line game built using Python where you play against the computer in the classic **Snake-Water-Gun** game.

---

## 🎮 How the Game Works

* Snake 🐍 drinks Water 💧 → **Snake wins**
* Water 💧 damages Gun 🔫 → **Water wins**
* Gun 🔫 kills Snake 🐍 → **Gun wins**

---

## 🚀 Features

* 🎲 Random computer choice using Python
* 🧠 Smart winner logic using modulo (`%`) operation
* 📊 Score tracking system
* ❌ Invalid input handling
* 🔁 Continuous gameplay loop (until user exits)
* 🎯 Clean and readable output with emojis

---

## 🕹️ Controls

| Input | Choice   |
| ----- | -------- |
| 0     | Snake 🐍 |
| 1     | Gun 🔫   |
| 2     | Water 💧 |
| 3     | Quit ❌   |

---

## 🧮 Game Logic

The winner is decided using:

```
(user - computer) % 3
```

| Result | Outcome          |
| ------ | ---------------- |
| 0      | Draw 🤝          |
| 1      | User Wins 🎉     |
| 2      | Computer Wins 💻 |

---

## ▶️ How to Run

1. Make sure Python is installed
2. Clone the repository:

```
git clone - https://github.com/nikhilkumar210h-debug/-Snake-Water-Gun-Game-Python-
```

3. Run the script:

```
python game.py
```

---

## 📸 Sample Output

```
Choose one:
0 for Snake, 1 for Gun, 2 for Water

You: Snake 🐍
Computer: Gun 🔫

You Lose 🤦‍♂️
```

---

## 📊 Score System

* Tracks user and computer scores
* Displays results after each round
* Helps improve gameplay experience

---

## 🧑‍💻 Author

**Nikhil Kumar**

---

## ⭐ Future Improvements

* 🎯 Best of 5 mode
* 🖥️ GUI version (Tkinter / Web)
* 🏆 Leaderboard system
* 🌐 Online multiplayer version

---

## 📌 License

This project is open-source and free to use.

---

💡 *Made with passion while learning Python*
