# PaintWars: Autonomous Robotics in Action!  
**Course**: LU3IN025 AI and Games – (Sorbonne Université)

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

## Project Structure
This repository includes three files outlining the topics for two labs and the project:

- **`instructions_TP1.md`**: Lab on behavior design, covering Braitenberg vehicles and subsumption architecture.
- **`instructions_TP2.md`**: Lab on behavior optimization for an autonomous robot, involving random search and genetic algorithms.
- **`instructions_projet.md`**: Project description.
