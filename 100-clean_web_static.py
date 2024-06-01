#!/usr/bin/python3

"""contains a fabric script that deletets out-of-date archive
"""
from fabric.api import env, task, run, local
import os
from pathlib import Path


# Define the directory path
LOCAL_DIRECTORY = 'versions'
REMOTE_DIRECTORY = '/data/web_static/releases'

# Local task to clean the directory
@task
def clean_local_directory(number=0):
    # List all files in the directory
    files = sorted(Path(LOCAL_DIRECTORY).glob('*'), key=os.path.getctime)

    # If there are files in the directory
    if files:
        # Keep the most recent file
        if (number == 0 or number == 1):
            most_recent_file = files[-1]
        elif (number == 2):
            most_recent_file = files[-2]
        else:
            return

        # Delete all other files
        for file in files[:-1]:
            if file.is_file():  # Ensure it's a file and not a directory
                print(f"Deleting {file}")
                file.unlink()

        print(f"Kept the most recent file: {most_recent_file}")
    else:
        print(f"No files found in the local directory: {LOCAL_DIRECTORY}")

# Remote task to clean the directory
@task
def clean_remote_directory(number=0):
    # List all files in the directory
    files = sorted(run(f"ls -t {REMOTE_DIRECTORY}").split(), key=lambda f: run(f"stat -c %Z {REMOTE_DIRECTORY}/{f}"))

    # If there are files in the directory
    if files:
        # Keep the most recent file
        if (number == 0 or number == 1):
            most_recent_file = files[-1]
        elif (number == 2):
            most_recent_file = files[-2]
        else:
            return

        # Delete all other files
        for file in files[:-1]:
            print(f"Deleting {file}")
            run(f"rm {REMOTE_DIRECTORY}/{file}")

        print(f"Kept the most recent file: {most_recent_file}")
    else:
        print(f"No files found in the remote directory: {REMOTE_DIRECTORY}")

# Set the list of remote hosts
env.hosts = ['100.26.254.81', '100.26.158.71']  # Add more hosts as needed
env.user = "ubuntu"

# Define the main task to execute
@task
def do_clean(number=0):
    clean_local_directory(number)
    clean_remote_directory(number)

