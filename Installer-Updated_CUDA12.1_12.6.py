import webbrowser
import time
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
import os
import re
import pyperclip  # For clipboard copy

# --- Installer URLs ---
urls = {
    "Python 3.12.0": 'https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe',
    "CUDA_12.1": 'https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_531.14_windows.exe',
    "CUDA_12.6": 'https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda_12.6.0_560.76_windows.exe',
    "Anaconda": 'https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe'
}

# --- GUI Message Box ---
def show_message_box(message, title="Info"):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

# --- Y/N Prompt ---
def prompt_user_installation(name):
    while True:
        choice = input(f"{name} is not installed. Do you want to install {name}? (Y/N): ").strip().lower()
        if choice in ['y', 'n']:
            if choice == 'y':
                if name == "Anaconda":
                    show_message_box(
                        "During the Anaconda Wizard Setup, please make sure to check the middle box:\n"
                        "[Let Python 3.xx be default / added to PATH]",
                        title="Important Setup Instruction"
                    )
                elif name == "Python 3.12.0":
                    show_message_box(
                        "During the Python Wizard Setup, please make sure to check the checkbox at the bottom:\n"
                        "[x] Enable all PATH",
                        title="Important Setup Instruction"
                    )
            return choice == 'y'
        print("Invalid input. Please enter Y or N.")

# --- Installer Handler with Retry and Initial Delay ---
def handle_component_with_retry(name, check_func, download_url):
    if check_func():
        print(f"{name} is already installed.")
        return True

    if not prompt_user_installation(name):
        print(f"Skipping installation of {name}.")
        return False

    print(f"Opening download page for {name}...")
    webbrowser.open(download_url)

    # Start 5 second timer immediately after opening the URL
    print(f"Waiting for version validation {name}...")
    time.sleep(5)

    installer_name = download_url.split("/")[-1]
    show_message_box(f"Please install {installer_name}. After installation, click OK to start verification.", title=f"Install {name}")

    # Then enter retry loop every 5 seconds until detected
    while True:
        if check_func():
            print(f"{name} was successfully installed.")
            return True
        print(f"{name} not detected yet. Retrying in 5 seconds...")
        time.sleep(5)

# --- Version Checks ---
def check_python_version():
    """Check if Python 3.12.0 is installed."""
    try:
        output = subprocess.check_output([sys.executable, '--version'], stderr=subprocess.STDOUT).decode().strip()
        match = re.search(r'Python (\d+)\.(\d+)\.(\d+)', output)
        if match and tuple(map(int, match.groups())) == (3, 12, 0):
            print(f"{output} is installed.")
            return True
        print(f"Detected version: {output}. Expected Python 3.12.0.")
        return False
    except subprocess.CalledProcessError:
        print("Python not found.")
        return False

def check_cuda_version(expected_version):
    """Check if the expected CUDA version is installed."""
    try:
        output = subprocess.check_output("nvcc --version", stderr=subprocess.STDOUT, shell=True).decode().strip()
        if f"release {expected_version}" in output:
            print(f"CUDA {expected_version} is installed.")
            return True
        print(f"Detected CUDA version:\n{output}\nExpected CUDA {expected_version}.")
        return False
    except subprocess.CalledProcessError:
        print("CUDA (nvcc) not found.")
        return False

def check_anaconda_version():
    """Check if Anaconda is installed."""
    try:
        output = subprocess.check_output("conda --version", stderr=subprocess.STDOUT, shell=True).decode().strip()
        print(f"{output} is installed.")
        return True
    except subprocess.CalledProcessError:
        print("Anaconda not found.")
        return False

# --- Show Manual Conda Install Commands with Tkinter Widget ---
def show_conda_install_commands():
    commands = (
        "conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia\n"
        "conda install -c conda-forge ultralytics"
    )
    
    # Copy commands to clipboard initially
    pyperclip.copy(commands)

    # Create window
    window = tk.Tk()
    window.title("Run These Conda Commands")

    # Instructions label
    label = tk.Label(window, text="📌 Please open Anaconda PowerShell Prompt manually.\n\n"
                                  "Then copy and run each of the following commands:", justify="left")
    label.pack(padx=10, pady=(10, 0))

    # Text widget with scrollbar
    text_frame = tk.Frame(window)
    text_frame.pack(padx=10, pady=5)

    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(text_frame, height=5, width=80, wrap="word", yscrollcommand=scrollbar.set)
    text_widget.insert("1.0", commands)
    text_widget.configure(state="normal")  # Allow user to select/copy
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=text_widget.yview)

    # Function to copy text to clipboard
    def copy_to_clipboard():
        pyperclip.copy(commands)
        messagebox.showinfo("Copied", "Commands copied to clipboard!")

    # Buttons frame
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_button.pack(side=tk.LEFT, padx=5)

    close_button = tk.Button(button_frame, text="Close", command=window.destroy)
    close_button.pack(side=tk.LEFT, padx=5)

    window.mainloop()

# --- Main Execution ---
if __name__ == "__main__":
    show_message_box(
        "This script will guide you through installing Python 3.12.0, CUDA 12.1, CUDA 12.6, and Anaconda if they are not already installed.",
        title="Setup Start"
    )

    python_installed = handle_component_with_retry("Python 3.12.0", check_python_version, urls["Python 3.12.0"])
    cuda121_installed = handle_component_with_retry("CUDA 12.1", lambda: check_cuda_version("12.1"), urls["CUDA_12.1"])
    cuda126_installed = handle_component_with_retry("CUDA 12.6", lambda: check_cuda_version("12.6"), urls["CUDA_12.6"])
    anaconda_installed = handle_component_with_retry("Anaconda", check_anaconda_version, urls["Anaconda"])

    if anaconda_installed:
        show_message_box("Now it's time to install PyTorch and Ultralytics.", title="Manual Step Required")
        show_conda_install_commands()
    else:
        print("Anaconda was not installed or skipped, skipping conda commands.")

    show_message_box("Setup complete. All selected components have been handled.", title="Finished")
