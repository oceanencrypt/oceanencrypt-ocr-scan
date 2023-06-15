import cv2
import pytesseract
import json

def extract_text(image_file = 'design.jpg', data_file = 'text.json'):
    # Load the UI design image
    img = cv2.imread(f'log/{image_file}')

    # Convert the image to grayscale for better text recognition
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use the Tesseract OCR engine to extract the text from the image
    text = pytesseract.image_to_string(gray)

    # Split the text into lines
    lines = text.split("\n")

    # Create a list to hold the information about each line of text
    text_lines = []

    # Iterate through each line of text
    for line in lines:
        # Add the line of text to the list of text lines
        text_lines.append({"text": line})
    
    with open(data_file, 'w') as f:
        json.dump(text_lines, f)
    
    print(text_lines)
    return text_lines

extract_text(image_file = 'design.jpg', data_file = 'text.json')