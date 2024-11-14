# Project - Paint Wars 


## Prerequisites
Before starting, you need to install the Roborobo simulator on your machine. This simulator installs easily on Linux and macOS by following the official instructions. For Windows, it's recommended to use a virtual machine.

## Installation
After installing Roborobo, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/nekonaute/SU-LU3IN025-robots.git
   ```

2. To test the installation:
   ```bash
   conda activate roborobo
   python comportement.py
   ```
   
- Use a Python version other than 3.10 (e.g., Python 3.9 if available). Ensure the Python version in your Conda environment aligns with your command-line Python.
- Make sure you have enough storage quota to install and run Roborobo (approx. 3.5 GB).
- For common issues, refer to the Roborobo "Troubleshooting" section (at the bottom of the page).

If you are using Windows, or if you’re unable to install Roborobo on Linux or macOS, we suggest using VirtualBox with an Ubuntu virtual machine. As of early 2023, Roborobo installations on Mac M1 encountered issues (likely resolved by the end of 2023).


## Description
**Paint Wars** pits two teams of 8 robots each ("Red Team" and "Blue Team") against each other to claim control of an arena divided into cells. A cell belongs to the team that last visited it. After 2000 iterations, the team controlling the most cells wins. This is a competitive variation of the multi-agent patrol problem, a classic problem in robotics.

The final behavior design, include at least:

- A subsumption architecture or a behavior tree
- At least two Braitenberg-type behaviors

- **Memory Constraint**: Each robot can retain only a single integer between steps, useful as a counter or state variable.
- **Robot ID**: Each robot has a unique ID (`robotId`). Note: the first robot of Team 1 has `robotId = 0`, and the first of Team 2 has `robotId = 4`. Use `robotId % 4` to determine a robot’s position in its team.
- **No Communication**: Robots cannot communicate with each other.
- **Sensor-Only Information**: Robots can only use information from their sensors.
- **No Maps**: Robots cannot use maps of the arena.

You can use `get_extended_sensors(sensors)` from `comportement.py` for easier handling. However, the code in `paintwars.py` is more complete, distinguishing walls from robots and identifying team membership.

## Running Paint Wars
To run Paint Wars with specific configurations:
```bash
python paintwars.py <arena_number> <invert_starting_position> <simulation_speed>
```
- **`<arena_number>`**: 0–5
- **`<invert_starting_position>`**: `True` or `False`
- **`<simulation_speed>`**: `0` (normal), `1` (fast), `2` (very fast, no display)

Example:
```bash
python paintwars.py 3 True 1
```

