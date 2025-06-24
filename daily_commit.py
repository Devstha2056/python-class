import subprocess
from datetime import datetime

def daily_commit():
    try:
        # Add all files
        subprocess.run(["git", "add", "."], check=True)

        # Commit with timestamp
        commit_message = f"Daily commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push to remote (optional, remove if not needed)
        subprocess.run(["git", "push"], check=True)

        print("Commit successful.")
    except subprocess.CalledProcessError as e:
        print(" Git command failed:", e)

if __name__ == "__main__":
    daily_commit()
