import psutil
import platform
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import time
import webbrowser
import sys


def get_gpu():
    if platform.system() == "Windows":
        try:
            result = subprocess.check_output('wmic path win32_videocontroller get caption', shell=True)
            gpus = result.decode().split('\n')[1:]  
            gpus = [gpu.strip() for gpu in gpus if gpu.strip()]
            return gpus
        except Exception as e:
            return str(e)
    elif platform.system() == "Linux":
        try:
            result = subprocess.check_output("lspci | grep VGA", shell=True)
            return result.decode().splitlines()
        except Exception as e:
            return str(e)
    else:
        return "GPU detection not supported on this OS"


def is_gpu_compatible(gpu_list):
    compatible_gpus = [
        # Nvidia GPUs
        "GTX 960", "GTX 970", "GTX 980", "GTX 1060", "GTX 1070", "GTX 1080", "GTX 1660", "GTX 1660 Ti", "GTX 1060", "GTX 1070",
        "RTX 2060", "RTX 2070", "RTX 2080", "RTX 3060", "RTX 3070", "RTX 3080", "RTX 3090", 
        "RTX 4060", "RTX 4070", "RTX 4080", "RTX 4090",
        
        # AMD GPUs
        "AMD RX 580", "AMD RX 590", "AMD RX 5700", "AMD RX 6700", "AMD RX 6800", "AMD RX 6900", 
        "AMD RX 7600", "AMD RX 7700", "AMD RX 7800", "AMD RX 7900",
        
        # Intel GPUs
        "Intel Arc A750", "Intel Arc A770"
    ]
    
    for gpu in gpu_list:
        for model in compatible_gpus:
            if model in gpu:
                return True, gpu  
    return False, None  


def show_fancy_message(is_compatible_gpu, gpu_model=None):
    root = tk.Tk()
    root.withdraw()  

    # Fancy Window Design
    window = tk.Toplevel()
    window.title("GPU Hardware Results")
    window.geometry("550x330")  # Larger size for fancier window
    window.config(bg="#2E3B4E")  # Background color
    
    
    title_label = tk.Label(window, text="GPU Compatibility Check", font=("Helvetica", 18, "bold"), fg="white", bg="#2E3B4E")
    title_label.pack(pady=20)

    # Compatibility message
    if is_compatible_gpu:
        message_text = f"Your GPU is compatible: {gpu_model}"
        icon = "✔️"  # Success icon
        message_color = "#3BB143"  # Green color
    else:
        message_text = f"Your GPU is not compatible: {gpu_model}"
        icon = "❌"  # Failure icon
        message_color = "#F44336"  # Red color

    message_label = tk.Label(window, text=f"{icon} {message_text}", font=("Helvetica", 14), fg=message_color, bg="#2E3B4E", wraplength=450)
    message_label.pack(pady=20)

    button_frame = tk.Frame(window, bg="#2E3B4E")
    button_frame.pack(pady=20)
    
    if is_compatible_gpu:
        # Button for downloading AimmyV2.1.5
        download_button1 = tk.Button(button_frame, text="[x] Download AimmyV2.1.5 - Universal", font=("Helvetica", 12), fg="white", bg="#2196F3", command=ask_to_open_link_1, relief="flat", bd=2)
        download_button1.pack(padx=10, side="top", fill="x", expand=True, pady=5)

        # Button for downloading AimmyV2.2.0 (Tensor/DLLS-INCLUDED)
        download_button2 = tk.Button(button_frame, text="[x] Download AimmyV2.2.0 Tensor/DLLS-INCLUDED(Nvidia Only)", font=("Helvetica", 12), fg="white", bg="#4CAF50", command=ask_to_open_link_2, relief="flat", bd=2)
        download_button2.pack(padx=10, side="top", fill="x", expand=True, pady=5)

        # Button for joining the Discord server
        discord_button = tk.Button(button_frame, text="[x] Join Our Discord", font=("Helvetica", 12), fg="white", bg="#7289DA", command=join_discord, relief="flat", bd=2)
        discord_button.pack(padx=10, side="top", fill="x", expand=True, pady=5)
    else:
        # No download links, just an exit button for incompatible GPU
        exit_button = tk.Button(button_frame, text="Exit", font=("Helvetica", 12), fg="white", bg="#F44336", command=sys.exit, relief="flat", bd=2)
        exit_button.pack(padx=10, side="top", fill="x", expand=True, pady=5)
    
    window.mainloop()


def ask_to_open_link_1():
    url = "https://github.com/SlowPotato/LazyInstaller/blob/main/LazyAimmySetup.exe"
    webbrowser.open(url)


def ask_to_open_link_2():
    url = "https://github.com/TaylorIsBlue/Aimmy-CUDA/releases/download/2.2.0/DLLS-INCLUDED.2.2.0-AC.rar"
    webbrowser.open(url)


def join_discord():
    url = "https://discord.gg/mTXpkE2cVS"
    webbrowser.open(url)


def show_loading_bar():
    root = tk.Tk()
    root.title("Checking GPU Compatibility")
    
    style = ttk.Style()
    style.configure("TProgressbar",
                    thickness=20,
                    length=400,
                    barcolor="#4CAF50",
                    )

    progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
    progress.grid(row=0, column=0, padx=20, pady=20)
    progress["maximum"] = 100  

    label = tk.Label(root, text="Checking your GPU compatibility...\n\nSeriously... don't use Aimmy on Fortnite or Valorant we will not assist with HWID bans", font=("Arial", 10), fg="red", justify="center")
    label.grid(row=1, column=0, padx=20, pady=10)

    root.after(100, lambda: check_gpu_in_background(root, progress))
    root.mainloop()


def check_gpu_in_background(root, progress):
    for i in range(1, 101):
        time.sleep(0.05)  
        progress["value"] = i
        root.update_idletasks()

    gpu_list = get_gpu()
    is_compatible_gpu, gpu_model = is_gpu_compatible(gpu_list) if isinstance(gpu_list, list) and gpu_list else (False, None)

    show_fancy_message(is_compatible_gpu, gpu_model)  

    root.quit()


def check_gpu_compatibility():
    show_loading_bar()


check_gpu_compatibility()
