# 🎯 Face Recognition Attendance System

This project uses real-time face recognition to mark attendance automatically. It captures a live video feed, recognizes faces from a pre-saved dataset, and logs attendance with timestamps into a CSV and Excel file.

---

## 📦 Features

- ✅ Face encoding and recognition using `face_recognition` and `OpenCV`
- 🧠 Smart attendance marking — only once per person per day
- 💾 Efficient encoding storage using `pickle`
- 📁 Auto CSV to Excel conversion with auto column width
- 💡 User-friendly console messages and bounding boxes in the video feed

---

## 🛠 Requirements

Install the dependencies using pip:

```bash
pip install opencv-python face_recognition numpy openpyxl
  

## 📂 Project Structure  
project-folder/
│
├── faces/                # Folder containing face images (one image per person)
│   ├── John.jpg
│   └── Alice.jpg
│
├── encodings.pkl         # Saved face encodings (generated on first run)
├── attendance.csv        # CSV log of attendance (auto-created)
├── attendance.xlsx       # Excel version of the attendance
└── main.py               # Main face recognition attendance script

## 📥 Installation & Setup  
1️⃣ **Clone this repository**:  

git clone https://github.com/utkarsh1042005/Face-Recognition-Attendance-System.git 
cd Face-Recognition-Attendance-System

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Run the project:
python main.py

🚀 How It Works
1.The program loads known face images from the faces/ directory.

2.It encodes faces and stores them in encodings.pkl for faster future loads.

3.It opens a webcam feed and detects faces in real-time.

4.If a recognized face is detected, it marks attendance in attendance.csv with the current date and time.

5.On exit (press Q), the CSV is converted to a formatted Excel sheet and deleted.

👤 Adding New Faces
Add an image to the faces/ folder.

Make sure the file name is the person name (e.g., John.jpg)

Restart the script. It will re-encode all faces if encodings.pkl is not present.

## 📸 Screenshots

### 1️⃣ Face Detection in Action  
![Face Detection](https://raw.githubusercontent.com/utkarsh1042005/Face-Recognition-Attendance-System./main/working_of_project.png)

### 2️⃣ Attendance Marked Successfully  
![Attendance Marked](https://raw.githubusercontent.com/utkarsh1042005/Face-Recognition-Attendance-System./main/created_csv_file_sample.png)

## 🎥 Demo Video  

[![Watch the demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://github.com//utkarsh1042005/Face-Recognition-Attendance-System./blob/main/demo_working.mp4)

