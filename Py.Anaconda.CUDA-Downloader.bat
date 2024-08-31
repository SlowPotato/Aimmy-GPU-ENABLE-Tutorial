@echo off
rundll32 url.dll,FileProtocolHandler https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
pause
rundll32 url.dll,FileProtocolHandler https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Windows-x86_64.exe
pause
rundll32 url.dll,FileProtocolHandler https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_522.06_windows.exe