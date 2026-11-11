# Sudoku Solver

A Python desktop application that solves 9×9 Sudoku puzzles using a student-implemented recursive backtracking algorithm.

## Planned features
- At least 50 selectable Sudoku templates, each with one unique solution
- Readable 9×9 board with emphasized 3×3 regions
- Validation of contradictory starting clues
- Recursive backtracking solver with candidate checking
- Visual distinction between original clues and computed entries
- Solve and Reset controls
- Clear solved, invalid-puzzle, and no-solution statuses

## Planned technologies
- Python 3
- Tkinter (desktop GUI; included with many Python installations)
- JSON (puzzle data)
- Git and GitHub

## Project structure
- `main.py` — application entry point
- `solver.py` — recursive backtracking algorithm
- `validator.py` — Sudoku constraint and input validation
- `puzzle_manager.py` — loading and selecting puzzle templates
- `gui.py` — desktop user interface
- `data/` — puzzle templates
- `tests/` — automated tests
- `docs/` — planning and project documentation

## Setup
1. Install Python 3.
2. Clone or download this repository.
3. (Optional) Create and activate a virtual environment.
4. Install dependencies with `pip install -r requirements.txt`.
5. Run `python main.py` after the application components have been implemented.

## Development status
Planning and repository initialization. The application modules are starter placeholders and are not yet a working Sudoku solver.

## Puzzle data acknowledgment
Add the source and attribution for each puzzle dataset in `data/README.md` before including third-party puzzles.
