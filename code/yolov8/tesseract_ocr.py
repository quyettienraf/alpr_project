import cv2
import os
import pytesseract
from pytesseract import Output

output_folder = "output_images/test_2"  # Update this to your output folder path

for filename in os.listdir(output_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(output_folder, filename)

        # Read the image using OpenCV
        image = cv2.imread(image_path)

        # Perform OCR on the image using pytesseract
        text = pytesseract.image_to_string(image, output_type=Output.STRING)

        if len(text) > 0:
            # Create a text file with the same name as the image
            text_filename = os.path.splitext(filename)[0] + ".txt"
            text_file_path = os.path.join(output_folder, text_filename)

            # Save the extracted text to the text file
            with open(text_file_path, "w") as text_file:
                text_file.write(text)

            # Print or save the extracted text
            print(f"File: {filename}\nText: {text}\nText saved to: {text_file_path}\n")

