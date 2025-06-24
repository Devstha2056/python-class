import subprocess
import os
from datetime import datetime

# Change to your Git repo
os.chdir("/home/devendra/Documents/python class")

def daily_commit():
    try:
        # Step 1: Update a daily log file
        with open("daily.log", "a") as log_file:
            log_file.write(f"Daily commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Step 2: Stage everything
        subprocess.run(["git", "add", "."], check=True)

        # Step 3: Commit with timestamp message
        commit_message = f"Daily commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Step 4: Push to remote (optional)
        subprocess.run(["git", "push"], check=True)

        print("✅ Daily commit pushed.")

    except subprocess.CalledProcessError as e:
        print("❌ Git command failed:", e)

if __name__ == "__main__":
    daily_commit()