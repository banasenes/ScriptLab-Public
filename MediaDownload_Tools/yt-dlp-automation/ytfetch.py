"""
ytfetch - YouTube Download Automation
-----------------------------
Author: yung-megafone
Date: 2025-02-24
License: MIT License

Description:
ytfetch is a Python script that automates YouTube video downloads, ensuring only new content 
is fetched without redownloading previously saved videos. It supports custom folder organization, 
efficient tracking, and automated execution via scheduling tools.

Features:
- Fetches only new videos, preventing duplicate downloads.
- Uses a text-based configuration file (`channels.txt`) for batch processing.
- Saves videos in user-specified folders based on creator names.
- Tracks downloaded content using `downloaded_videos.txt`.
- Supports scheduled execution via cron jobs or Task Scheduler.
- Optimized for automation, requiring minimal manual intervention.

Usage:
    python ytfetch.py

Example:
    python ytfetch.py

Automating the Script:
    - Linux/macOS (via crontab):
        0 * * * * /usr/bin/python3 /path/to/ytfetch.py
    - Windows (Task Scheduler):
        python C:\path\to\ytfetch.py

Configuration:
    The script reads `channels.txt` formatted as:
        Folder Name | Channel URL

Example:
    Midwest Safety | https://www.youtube.com/@MidwestSafety
    Engineering Explained | https://www.youtube.com/@EngineeringExplained
"""
import os           # File and dir ops
import yt_dlp       # To download yt content
import subprocess   # To execute python commands (python yt-dlp)
import sys          # For CLI argument handling
import argparse     # For CLI argument flags (ytfetch.py --help)
import shutil       # For file mgmt
import time         # For tracking performance and exec time
def download_handler():
    url = input("Please insert a url: \n").strip()

    if not url:
        print("Please enter a valid URL.")
        return  
    
    # Exec python yt-dlp -o "%(title)s.%(ext)s" inserturl
    command = ["yt-dlp", "-o", "%(title)s.%(ext)s", url]

    try:
        print(f"Executing: {' '.join(command)}")
        subprocess.run(command, check=True)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Download failed. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    download_handler()