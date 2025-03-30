import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime
import openpyxl

# Path to the folder containing known faces
path = 'faces'
images = []
classNames = []
face_list = os.listdir(path)

# Load known images
for cl in face_list:
    cur_img = cv2.imread(f'{path}/{cl}')
    images.append(cur_img)
    classNames.append(os.path.splitext(cl)[0])

print("✅ Encoding Started...Please wait for a while!!!!")

def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if encode:  # Check if face encoding exists
            encode_list.append(encode[0])
    return encode_list

# Get encodings of known faces
known_encodings = find_encodings(images)
print("✅ Encoding Complete!!!!")

# Attendance Files
csv_filename = "attendance.csv"
excel_filename = "attendance.xlsx"

# Ensure CSV file has headers if not already created
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

# Set to track attendance already marked during the current session
marked_today = set()

def mark_attendance(name):
    now = datetime.now()
    date_today = now.strftime("%d-%m-%Y")
    time_now = now.strftime("%H:%M:%S")

    if name in marked_today:
        return  # Avoid duplicate marking in the same session
    
    # Read existing entries to prevent duplicate marking across runs
    try:
        with open(csv_filename, 'r') as f:
            existing_entries = f.readlines()
    except FileNotFoundError:
        existing_entries = []

    if f"{name},{date_today}" not in "".join(existing_entries):
        with open(csv_filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, date_today, time_now])
        print(f"✅ {name}'s attendance marked!")
        marked_today.add(name)

        # Convert CSV to Excel & delete CSV
        csv_to_excel_and_delete(csv_filename, excel_filename)
    else:
        marked_today.add(name)
        print(f"✅ {name}'s attendance already marked today!")

# Function to Convert CSV to Excel & Delete CSV File
def csv_to_excel_and_delete(csv_file, excel_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Attendance"

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

    # Adjust column width automatically
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max_length + 2

    wb.save(excel_file)
    os.remove(csv_file)  # Delete the CSV file after conversion

# Start Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_small = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)  # Resize for faster processing
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

    faces_current_frame = face_recognition.face_locations(img_small)
    encodes_current_frame = face_recognition.face_encodings(img_small, faces_current_frame)

    for encodeFace, faceLoc in zip(encodes_current_frame, faces_current_frame):
        matches = face_recognition.compare_faces(known_encodings, encodeFace)
        faceDis = face_recognition.face_distance(known_encodings, encodeFace)

        if len(faceDis) > 0:
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                mark_attendance(name)

    cv2.imshow('Face Attendance System', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'Q' to quit
        break

cap.release()
cv2.destroyAllWindows()
