# System Monitor Python

A Python-based tool to monitor CPU and memory usage in real-time. This script logs system metrics at specified intervals and can run indefinitely or for a limited duration as specified by the user.

## Features

CPU and Memory Monitoring: Tracks CPU load and memory usage of the system.

Real-Time Logging: Logs system metrics to both the console and a file (system_monitor.log).

Configurable Settings: Allows users to specify monitoring intervals and duration via command-line arguments.

Graceful Shutdown: Handles termination signals gracefully.

## Requirements:

- Python 3.x
- psutil library

## Installation

Clone the repository:

bash
Copy code
git clone https://github.com/Raihan11x/File-Monitor-Python.git
cd File-Monitor-Python
Install the required dependencies:

bash
Copy code
pip install psutil
Usage
To run the system monitor, use the following command:

bash
Copy code
python system_monitor.py --interval <interval> --duration <duration>
Arguments
--interval, -i (optional): Monitoring interval in seconds (default: 10 seconds).
--duration, -d (optional): Total monitoring duration in seconds. If not specified, the script will run indefinitely.
Examples
Monitor with a default interval of 10 seconds and run indefinitely:

bash
Copy code
python system_monitor.py
Monitor with a custom interval of 5 seconds:

bash
Copy code
python system_monitor.py --interval 5
Monitor with a custom interval of 5 seconds for a total duration of 60 seconds:

bash
Copy code
python system_monitor.py --interval 5 --duration 60
Logs
The script logs system metrics to:

The console (standard output).
A log file named system_monitor.log.
Stopping the Monitor
To stop the monitor, press Ctrl+C. The script handles shutdown gracefully, ensuring all resources are cleaned up.
