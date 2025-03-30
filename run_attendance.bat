@echo off
cd /d C:\Users\ADMIN\OneDrive\Desktop\Face_Attendance
call C:\Users\ADMIN\anaconda3\Scripts\activate.bat
call conda activate face_env
python main.py
pause
