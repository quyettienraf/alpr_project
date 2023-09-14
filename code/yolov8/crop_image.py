import cv2
import os

video_name = "test_2"
video_path = "runs/detect/predict3/test_2.mp4"  # Replace with your video file path
label_folder = "runs/detect/predict3/labels"  # Replace with the folder path containing the label files
output_folder = "output_images/test_2"  # Replace with the folder where you want to save the cropped images

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_number = 0

x = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Break the loop if we've reached the end of the video
    print("x: ", x)
    x = x + 1
    # Load the corresponding label file
    label_file = os.path.join(label_folder, video_name + "_" + f"{frame_number}.txt")
    print("label_file:", label_file)
    print("check000")
    if os.path.exists(label_file):
        with open(label_file, "r") as f:
            label_data = f.readline().strip().split()

            # Parse YOLO label data
            class_label, x_center, y_center, box_width, box_height = map(float, label_data)

            # Calculate the actual coordinates of the bounding box
            frame_height, frame_width, _ = frame.shape
            x_center *= frame_width
            y_center *= frame_height
            box_width *= frame_width
            box_height *= frame_height

            # Calculate bounding box coordinates
            x1 = int(x_center - box_width / 2)
            y1 = int(y_center - box_height / 2)
            x2 = int(x_center + box_width / 2)
            y2 = int(y_center + box_height / 2)

            # Crop the frame
            cropped_frame = frame[y1:y2, x1:x2]

            # Save the cropped image
            output_file = os.path.join(output_folder, f"{frame_number}.jpg")
            cv2.imwrite(output_file, cropped_frame)

    frame_number += 1

# Release the video object
cap.release()
