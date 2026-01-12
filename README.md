# The Ruins of Kal-Har — Choose Your Own Adventure

A small, command-line "Choose Your Own Adventure" game written in Python. Explore the ruined temple of Kal-Har, make choices, and discover multiple endings (good, bad, and neutral). The game is simple, extensible, and designed to be a starter project for learning Python and building interactive fiction.

---

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Run Instructions](#installation--run-instructions)
  - [Option A — Run locally (recommended)](#option-a---run-locally-recommended)
  - [Option B — Run in the browser (no local install)](#option-b---run-in-the-browser-no-local-install)
  - [Option C — Run with Docker](#option-c---run-with-docker)
- [How to Play](#how-to-play)
- [Game Controls & Input](#game-controls--input)
- [Endings](#endings)
- [Project Structure](#project-structure)
- [How the code is organized](#how-the-code-is-organized)
- [How to expand the game](#how-to-expand-the-game)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact / Questions](#contact--questions)

---

## Demo

(Save `adventure.py` in a folder and run it — instructions below.)

When you run the script you'll see:
- A short story introduction
- A numbered list of choices at each decision point
- Branching scenes and multiple endings based on your choices

---

## Features

- Clean, function-based scene structure
- Input validation with graceful handling of invalid entries and interrupts
- At least three distinct endings: good, bad, neutral
- Guidance in comments for expanding the game
- Multiple ways to run (local, browser, Docker)

---

## Tech stack

- Language: Python 3 (works with Python 3.6+)
- Optional: Docker (for running without installing Python)
- Optional platforms: Replit for running in the browser

No external Python libraries are required.

---

## Prerequisites

- Option A (local): Python 3 installed (3.6+ recommended)
- Option B (browser): a Replit account or guest session (no local install)
- Option C (Docker): Docker installed & running

---

## Installation & Run Instructions

Place `adventure.py` and this `README.md` in the same folder.

### Option A — Run locally (recommended)

macOS / Linux:
```bash
# open a terminal, change directory to where adventure.py is saved
cd /path/to/game-folder

# run with python3
python3 adventure.py

# or if your system uses `python` for Python 3
python adventure.py
```

Windows (Command Prompt / PowerShell):
```powershell
cd C:\path\to\game-folder

# If Python launcher installed:
py adventure.py

# Or:
python adventure.py
```

Notes:
- If `python` runs Python 2 on your system, use `python3`.
- On Windows, ensure you added Python to PATH during installation.

### Option B — Run in the browser (no local install)

Use Replit:
1. Go to https://replit.com
2. Click "Create" → choose "Python" or "New repl" → "Python"
3. Replace `main.py` contents with `adventure.py` contents (or upload `adventure.py`)
4. Click Run

This is the fastest way if you don't want to install anything.

### Option C — Run with Docker

From the folder containing `adventure.py`:

Linux / macOS:
```bash
docker run --rm -it -v "$(pwd)":/app -w /app python:3.11 python adventure.py
```

Windows PowerShell:
```powershell
docker run --rm -it -v "${PWD}:/app" -w /app python:3.11 python adventure.py
```

---

## How to Play

- The game presents a short introduction and then a set of numbered choices (1, 2, 3, ...).
- Type the number that corresponds to the choice you want and press Enter.
- Some prompts accept `q`, `quit`, or `exit` to leave the game immediately.
- After reaching an ending, you'll be asked whether you want to play again (y/n).

Example:
- Prompt: `Choose an option (1-2):`
- Response: `1` (then press Enter)

---

## Game Controls & Input

- Valid input: integer in the shown range (e.g., `1`, `2`, `3`)
- Quick exit: type `q`, `quit`, or `exit` at the choice prompt
- Interrupt: Ctrl+C or Ctrl+D — the program will handle these gracefully
- Play again prompt: `y` / `n` (or `yes` / `no`)

The game validates input and will re-prompt if you enter invalid text.

---

## Endings

The game includes at least three endings:

- Good ending — you escape with the artifact and knowledge
- Neutral ending — you leave safely without the treasure
- Bad ending — you fall victim to temple traps or are trapped

Each ending is printed with a title and short concluding text.

---

## Project Structure

A minimal project layout:

```
/your-game-folder
  ├─ adventure.py
  └─ README.md
```

If you expand:
- Add `scenes/` directory for scene modules
- Add `assets/` for text files, maps, or JSON story data
- Add `tests/` for unit tests

---

## How the code is organized

- `get_choice(num_options)`: input validation and safe quitting
- `intro()`: prints story intro
- `crossroads()`: first decision point that routes to scenes
- `left_corridor()`, `right_chamber()`, `center_stairs()`: scene functions
- `ending_good()`, `ending_neutral()`, `ending_bad()`: ending functions
- `play_again_prompt()`: offers a replay option
- `main()`: main loop that runs the game

Each scene is a function, which makes adding or rearranging scenes straightforward.

---

## How to expand the game

Ideas and concrete instructions:

1. Add new scenes
   - Create a new function (e.g., `def secret_passage():`) that prints a scene and calls `get_choice(n)`.
   - From any scene call your new function.

2. Track player state (inventory, flags, health)
   - Replace global-free functions with a `state` dict argument or create a `Player` class.
   - Example signature:
     ```python
     def left_corridor(state):
         # read/write state['has_key']
         return state
     ```

3. Add persistence or saving/loading
   - Use JSON to dump and load `state` to/from a file.

4. Add randomness
   - `import random` and use `random.random()` or `random.choice()` for chance-based outcomes. Inform the player when an action has chance.

5. Move large scenes to separate modules
   - Create `scenes/` directory and import scene functions to keep `adventure.py` tidy.

6. Add unit tests
   - Mock `input()` and test `get_choice()` and scene transitions.

7. Add more endings and branching depth
   - Create intermediate scenes and increase choices to make the story larger.

---

## Troubleshooting

- "python: command not found"
  - Use `python3` if `python` maps to Python 2, or install Python from https://python.org.

- The game quits on Ctrl+C
  - This is expected; the script catches interrupts and exits gracefully.

- Unexpected Traceback
  - Copy the full traceback and share it — I can help debug.

---

## Contributing

- Feel free to:
  - Add more scenes or endings
  - Convert the linear flow into a stateful engine
  - Add unit tests and CI
- Suggested workflow:
  1. Fork the repository (if you put this in a GitHub repo)
  2. Create a feature branch
  3. Add changes, run tests
  4. Open a pull request describing your changes

If you'd like, I can propose example branches and PR descriptions.

---

## License

This project is provided under the MIT License. (Change as appropriate for your use.)

---

## Contact / Questions

If you want changes to the README (different wording, adding license header, or adding badges), tell me what you'd like and I'll update it. If you run into errors while running the game, tell me your OS and the exact error message and I'll guide you through fixes.

Enjoy building and expanding the adventure!
