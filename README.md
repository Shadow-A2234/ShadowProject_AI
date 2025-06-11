# new device
- step 1
.\.venv38\Scripts\activate
- step 2
Remove-Item -Recurse -Force .\.venv38 (kalau dah ada/rusak)
- step 3
python -m venv .venv38
- step 4
.\.venv38\Scripts\activate

# lib req
- pip install --upgrade pip setuptools
- pip install tensorflow==2.10 keras==2.10
- pip install opencv-python numpy
- pip install opencv-contrib-python (opsional)
- pip install mediapipe
- pip install pyautogui
- pip install pygetwindow pymsgbox pyrect
