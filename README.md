# WALL-E and EVE's Signal

An autonomous agent built in Python that explores a simulated 2D grid environment to locate EVE based on initial signal readings, while managing a limited battery budget.

## Core Features
* **Configurable Environment:** Loads map state and budgets via `config.json`.
* **Autonomous Decision Making:** The agent dynamically updates its coordinates based on signal evidence and remaining resources.
* **ASCII Visualization:** Real-time terminal output showing WALL-E (`[W]`), EVE's estimated location (`[?]`), and empty space (`.`).
* **Trace Logging:** Full action, observation, and reasoning logs compiled into a final mission report.

## How to Run
1. Ensure Python 3 is installed.
2. Clone or download this repository.
3. Open your terminal, navigate to the folder, and run:
   `python3 walle_agent.py`
