import os
import shutil
import subprocess

# Paths
source = r"C:\Users\abura\OneDrive\Desktop\centralize prototype\pisonettimer\dist\PisoNetTimer.exe"
repo_dir = r"C:\Users\abura\OneDrive\Desktop\centralize prototype\PisoNetRepo"
destination = os.path.join(repo_dir, "PisoNetTimer.exe")

try:
    # Ensure repo directory exists
    os.makedirs(repo_dir, exist_ok=True)

    # Remove old file if exists
    if os.path.exists(destination):
        os.remove(destination)
        print("Old file removed.")

    # Move new file
    shutil.move(source, destination)
    print("File moved successfully.")

    # Run Git commands
    subprocess.run("git add .", cwd=repo_dir, shell=True, check=True)
    subprocess.run('git commit -m "v3.1"', cwd=repo_dir, shell=True, check=True)
    subprocess.run("git push", cwd=repo_dir, shell=True, check=True)

    print("Git add, commit, and push completed successfully.")

except subprocess.CalledProcessError as git_error:
    print(f"Git command failed: {git_error}")

except Exception as e:
    print(f"Error: {e}")
