from pytesseract import *
import cv2
from PIL import Image
import PyQt5
import os.path
from orc import Ui_results
from PyQt5 import QtCore, QtGui, QtWidgets
import _pyinstaller_hooks_contrib


class main:

    pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    HERE = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join('C:\\Users\\brkeq\\PycharmProjects\\ocr1\\img.PNG')
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Cut image ekg
    if type(img) != 'NoneType':
        cut_img_ekg = img[0: 55, 200: 270]
    print(type(img))
    ekg_result = pytesseract.image_to_string(cut_img_ekg)

    # Cut image SPQ2a
    cut_img_spq2a = img[100: 150, 212: 270]
    spq2a_result = pytesseract.image_to_string(cut_img_spq2a)

    # Cut image resp ecg
    cut_img_resp_ecg = img[150: 200, 215: 270]
    resp_ecq_result = pytesseract.image_to_string(cut_img_resp_ecg)

    # Cut image ni_bp
    cut_img_ni_bp = img[250: 315, 190: 270]
    ni_bp_result = pytesseract.image_to_string(cut_img_ni_bp)

    if __name__ == "__main__":
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            results = QtWidgets.QMainWindow()
            ui = Ui_results(ekg_result,spq2a_result,resp_ecq_result,ni_bp_result)
            ui.setupUi(results)
            results.show()
            sys.exit(app.exec_())