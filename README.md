🧠 Python-Based OCR Application for Medical Data Extraction




📚 About
This Optical Character Recognition (OCR) application, written in Python with Tesseract OCR and PyQt5, automates the extraction of specific medical data fields from images. It reads designated regions of the input image and displays extracted values like EKG, SPQ2A, RESP ECG, and NIBP in a graphical interface.

🔥 Features
🧾 Automatically detects and reads fixed image regions

🧠 Extracts medical data using OCR (Tesseract)

🖥️ Displays results in a simple and modern PyQt5 GUI

🧩 Button-triggered result display (VIEW button)

🖼️ Processes .png medical image files

🧱 Technologies
Python 3.x

Tesseract OCR

PyQt5

OpenCV

Pillow (PIL)

🚀 How to Run
1. Install requirements
pip install pytesseract opencv-python pillow pyqt5

2. Install Tesseract OCR and update the path in main.py
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

3. Set your image path in main.py
image_path = 'C:\\your_path\\img.PNG'

4. Run the application
python main.py
