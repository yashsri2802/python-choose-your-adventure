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
docker run --
