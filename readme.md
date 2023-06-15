# OCR Code Setup and Usage Guide

This repository contains code for extracting text from images using optical character recognition (OCR). The code is implemented in Python and utilizes the OpenCV and pytesseract libraries.

## Prerequisites

Before setting up and running the OCR code, ensure you have the following prerequisites installed on your system:

- Python (version 3.6 or higher)
- pip (Python package installer)
- OpenCV library
- pytesseract library
- Tesseract OCR engine

## Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/oceanencrypt/oceanencrypt-ocr-scan.git
```

2. Change into the project directory:
```
cd oceanencrypt-ocr-scan
```


3. Install the required dependencies:
```
pip install -r requirements.txt
```


4. Install Tesseract OCR engine:
- For Windows: Download and install the Tesseract installer from the official GitHub repository: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- For macOS: Use Homebrew to install Tesseract:
  ```
  brew install tesseract
  ```
- For Linux (Ubuntu/Debian):
  ```
  sudo apt-get install tesseract-ocr
  sudo apt-get install libtesseract-dev
  ```

## Usage

1. Place the image file you want to extract text from in the `log` directory.

2. Open the `ocr_app/views.py` file.

3. In the `extract_text` function, modify the `image_file` parameter to the name of your image file:
```python
def extract_text(image_file='your_image.jpg', data_file='text.json'):
    # Rest of the code...
```

4. Install Tesseract OCR engine:
- For Windows: Download and install the Tesseract installer from the official GitHub repository: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- For macOS: Use Homebrew to install Tesseract:
  ```
  brew install tesseract
  ```
- For Linux (Ubuntu/Debian):
  ```
  sudo apt-get install tesseract-ocr
  sudo apt-get install libtesseract-dev
  ```

## Usage

1. Place the image file you want to extract text from in the `log` directory.

2. Open the `ocr.py` file.

3. In the `extract_text` function, modify the `image_file` parameter to the name of your image file:
```python
def extract_text(image_file='your_image.jpg', data_file='text.json'):
    # Rest of the code...
```

4. Optionally, modify the data_file parameter to specify a different output JSON file name if desired.

5. Save the changes to `ocr.py`.

6. Run the script:
```
python ocr.py
```

7. The extracted text will be displayed in the console output, and the results will be saved to the specified JSON file (text.json by default).