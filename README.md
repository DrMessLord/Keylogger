# CyberSecurity KeyLogger Project

## Overview
This Python-based keylogger project is designed to monitor and record keyboard input for cybersecurity applications. The keylogger captures keystrokes in real-time and stores them in a log file for analysis and security monitoring purposes.

## Features
- **Real-Time Keystroke Monitoring:** The keylogger captures keystrokes as they are typed, providing real-time monitoring of keyboard activity.
- **Logging:** Recorded keystrokes are logged to a text file, allowing for easy analysis and review of user input.
- **Customizable Logging Directory:** Users can specify the directory where the log file should be saved for flexibility and convenience.
- **Simple and Lightweight:** Built using the pynput library, the keylogger is lightweight and easy to use, making it suitable for a variety of cybersecurity applications.

## Usage
1. Clone or download the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the keylogger script using Python: `python keylogger.py`.
4. The keylogger will start capturing keystrokes in real-time. Press `Ctrl+C` to stop the keylogger.

## Dependencies
- **pynput:** Python library for monitoring and controlling keyboard and mouse input.

## Configuration
- **Log Directory:** By default, the log file (`keyLog.txt`) is saved in the same directory as the script. You can specify a custom directory by modifying the `log_dir` variable in the script.


## Disclaimer
This keylogger project is intended for educational and cybersecurity research purposes only. It is the responsibility of the user to comply with all applicable laws and regulations regarding the use of monitoring and surveillance software.
