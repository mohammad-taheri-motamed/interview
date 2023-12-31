import cv2
import pytesseract
import os
import openpyxl

# Set the path to the Tesseract OCR executable (Update this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get the current directory (where the script is located)
script_directory = os.getcwd()

# Set the directory containing the image files
image_directory = os.path.join(script_directory, 'images')

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Get a list of all image files in the directory
image_files = os.listdir(image_directory)
images = image_files.sort()

# Loop over each image file
for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(image_directory, image_file)

    # Load the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Define the region of interest (top right corner)
    roi_width = int(width * 0.55) # Adjust the width percentage as needed
    roi_height = int(height * 0.15) # Adjust the height percentage as needed
    roi = image[0:roi_height, width - roi_width:width]

    # Apply any preprocessing steps here if needed

    # Perform OCR on the region of interest
    text = pytesseract.image_to_string(roi)

    # Extract each number from the OCR text
    numbers = text.split()

    # Save each number to the Excel sheet
    sheet.append(numbers)

# Save the Excel workbook
workbook.save(os.path.join(script_directory, 'output.xlsx'))
