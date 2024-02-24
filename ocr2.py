import cv2
import numpy as np
import easyocr
from spellchecker import SpellChecker

def ocr(newpath):
    
# Load the image
    
    img = cv2.imread(newpath)

# Preprocess the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize OCR engine
    reader = easyocr.Reader(['en'])
    spell = SpellChecker()

    # Loop over contours and extract text
    for contour in contours:
        # Get bounding box coordinates
        x,y,w,h = cv2.boundingRect(contour)
        
        # Extract letter segment
        letter = gray[y:y+h, x:x+w]
        
        # Recognize text using OCR
        results = reader.readtext(letter, detail=0)
        
        # Check spelling of recognized text
        corrected_results = []
        for result in results:
            corrected_result = spell.correction(result)
            if corrected_result.isalpha():
                corrected_results.append(corrected_result)
        
        # Print the corrected text
        if corrected_results:
            print(corrected_results)
        
