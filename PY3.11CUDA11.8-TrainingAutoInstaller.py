import webbrowser
import time
import subprocess
import sys
import os
import tkinter as tk
from tkinter import messagebox

urls = [
    'https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe',
    'https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_522.06_windows.exe',
    'https://github.com/SlowPotato/TrainingFolder/archive/refs/heads/main.zip'
]

def show_message_box():
    """Show a message box to prompt the user to install Python 3.11.5"""
    root = tk.Tk()
    root.withdraw()  
    messagebox.showinfo("Python 3.11.5 Installation", 
        "Please install Python 3.11.5 before proceeding.\n"
        "Make sure the 'ENABLE ALL PATH' checkbox is checked during installation.\n"
        "You will be redirected to the Python 3.11.5 download page."
    )
    root.destroy()

def open_urls():
    for url in urls:
        print(f"Opening {url}...")
        webbrowser.open(url)
        time.sleep(2)

def check_python_version():
    """Check if Python 3.11.5 is installed."""
    try:
        python_version = subprocess.check_output([sys.executable, '--version'], stderr=subprocess.STDOUT)
        python_version = python_version.decode().strip()
        if python_version.startswith('Python 3.11'):
            print(f"{python_version} is installed.")
            return True
        else:
            print(f"Current Python version: {python_version}. Please install Python 3.11.5.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking Python version: {e}")
        return False

def check_cuda_version():
    """Check if CUDA 11.8 is installed."""
    try:
        cuda_version = subprocess.check_output("nvcc --version", stderr=subprocess.STDOUT, shell=True)
        cuda_version = cuda_version.decode().strip()
        if "release 11.8" in cuda_version:
            print("CUDA 11.8 is installed.")
            return True
        else:
            print(f"CUDA version: {cuda_version}. Please install CUDA 11.8.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking CUDA version: {e}")
        return False

def open_cmd_and_install_dependencies():
    """Open a new CMD window and install dependencies."""
    subprocess.Popen('start cmd', shell=True)

    # Install Ultralytics package
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pip install ultralytics==8.0.238"])

    # Install PyTorch, Torchvision, and Torchaudio with the specified index URL
    subprocess.check_call([sys.executable, "-m", "pip", "pip3", "install", "torch", "torchvision", "torchaudio", "--index-url", "pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118"])

    subprocess.check_call([sys.executable, "-m", "pip", "pip3", "install", "pip3 install opencv-python"])
    
if __name__ == "__main__":
    show_message_box()  

    open_urls()  

    # Retry the check until Python 3.11.5 is detected
    while not check_python_version():
        print("Python 3.11.5 is not yet detected. Retrying in 10 seconds...")
        time.sleep(10)  
    
    # Retry the check until CUDA 11.8 is detected
    while not check_cuda_version():
        print("CUDA 11.8 is not yet detected. Retrying in 10 seconds...")
        time.sleep(10)  

    open_cmd_and_install_dependencies()  # Proceed with the installation once both Python and CUDA are detected
