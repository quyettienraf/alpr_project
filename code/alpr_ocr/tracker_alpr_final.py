from ultralytics import YOLO
import cv2
import os
import time
import numpy as np 
from paddleocr import PaddleOCR
from collections import defaultdict
# from tracker import Tracker
from collections import Counter
import re
import datetime

INPUT_DIR = '../../test_video/test_1.mp4' 
OUT_PATH = './results/test_1_track_1.avi'
IMG_SIZE = 640
CONF = 0.6
ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')
# Load a model
# model = YOLO("../yolov8/alpr_yolov8n_8000img_100epochs.pt") 
model = YOLO("../yolov8/alpr_yolov8n_8000img_100epochs.pt") 



def perform_ocr(image):
    ocr_res = ocr.ocr(image, cls=False, det=False)
    return ocr_res

def rotate_and_split_license_plate(image):
    # Convert images to grayscale for easy processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find contours in the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3) # Use 3x3 kernel to detect edges

    # Find line segments in the image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)
    # np.pi / 180: Minimum value for angle theta (in radians)
    # threshold=100: This is the threshold for considering a straight line.
    # If there are many lines with the same angle and high contrast (correlation),
    # only lines with contrast higher than this threshold are considered a valid line.
    # When the threshold value is low, many straight lines will be detected;
    # when it is high, only very clear lines are considered
    # Test run the snippet below to see details
    # cv2.imshow("edges", edges)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Check if lines has a valid value
    if lines is not None:
        # Calculate the average rotation angle of the line segments
        total_angle = 0
        count = 0

        for rho, theta in lines[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            # Calculate the rotation angle of the line segment
            angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi

            # Eliminate nearly square line segments (with angles less than a threshold)
            if abs(angle) > 10 and abs(angle) < 80:
                total_angle += angle
                count += 1

        # Calculate the average rotation angle
        if count > 0:
            average_angle = total_angle / count
        else:
            average_angle = 0

        # Rotate the photo so the license plate is horizontal
        height, width = image.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, average_angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

        # Calculate the point that divides the image into upper and lower parts
        split_point = height // 2

        # Create two sub-image parts from rotated_image
        upper_part = rotated_image[:split_point, :]
        lower_part = rotated_image[split_point:, :]

        print("Đã tìm thấy đoạn thẳng.")
        print("angle:", angle)
        print("rotate angle:", average_angle)
        return upper_part, lower_part
    else:
        print("Không tìm thấy đoạn thẳng.")
        return None, None


def test_vid_yolov8(vid_dir, out_path):
    # Declaring variables for video processing.
    cap = cv2.VideoCapture(vid_dir)
    # Get the total frame count
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    codec = cv2.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # file_name = os.path.join(out_path, 'out_' + vid_dir.split('/')[-1] + )
    # out = cv2.VideoWriter(file_name, codec, fps, (width, height))
    out = cv2.VideoWriter(out_path, codec, fps, (width, height))

    # Frame count variable.
    ct = 0
    
    # Reading video frame by frame.
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret == True:
            print(str(ct) + "/" + str(total_frames))

            # Noting time for calculating FPS.
            prev_time = time.time()

            # Use the model
            results = model(img)  # predict on an image
            img_tmp = img
            for result in results:
                if result.boxes is not None and len(result.boxes) > 0:
                    # Get the bounding boxes and image for each result
                    bboxes = result.boxes[0].cpu().numpy()
                    # img = cv2.imread(input)  # Đảm bảo bạn đã định nghĩa biến 'input'
            
                    # Loop through bboxes and apply OCR, then draw on the image
                    
                    try:
                        for bbox in bboxes:
                            xyxy = bbox.xyxy
                            x1, y1, x2, y2 = xyxy[0]
                
                            # Check that the license plate is roughly square (e.g. 1:1 ratio)
                            width = x2 - x1
                            height = y2 - y1
                            aspect_ratio = width / height
                            print("aspect_ratio:", aspect_ratio)
                
                            if 0 <= aspect_ratio <= 1.5:
                                # Cut and rotate the license plate --------------
                                image_upper, image_lower = rotate_and_split_license_plate(
                                    img[int(y1):int(y2), int(x1):int(x2)])

                                if image_upper is None and image_lower is None:
                                    # License plates are roughly square or square
                    
                                    # Calculate the point that divides the image into upper and lower parts
                                    split_point = y1 + (y2 - y1) // 2

                                    # Create two subimage parts from the cr_img image
                                    upper_part = img[int(y1):int(split_point), int(x1):int(x2)]
                                    lower_part = img[int(split_point):int(y2), int(x1):int(x2)]
                                
                                    image_upper=cv2.resize(upper_part,(int(width),int(height/2)))
                                    image_lower=cv2.resize(lower_part,(int(width),int(height/2)))

                                image_collage_horizontal =np.hstack([image_upper, image_lower])
                                image_filename = str(ct) + ".jpg"  # Tên file ảnh đầu ra
                                cv2.imwrite("results/crop_image/" + image_filename, image_collage_horizontal)
                
                                # Continue processing the cr_img rectangular image here
                                ocr_res = perform_ocr(image_collage_horizontal)
                
                                # Save two parts of the image
                                # cv2.imwrite("results/upper_part.jpg", upper_part)
                                # cv2.imwrite("results/" + str(ct) + ".jpg", lower_part)
                            else:
                                # The license plate is not nearly square
                                # Normal image processing here (cr_img = img[int(y1):int(y2), int(x1):int(x2)])
                                cr_img = img[int(y1):int(y2), int(x1):int(x2)]
                                image_filename = str(ct) + ".jpg"  # Tên file ảnh đầu ra
                                cv2.imwrite("results/crop_image/" + image_filename, cr_img)
                                ocr_res = perform_ocr(cr_img)
                            recognized_text = ocr_res[0][0][0] if ocr_res else "No Text"
                            print("recognized_text: ",recognized_text)
                            
                            ocr_conf = ocr_res[0][0][1] if ocr_res else "No Conf"
                            ocr_conf = round(ocr_conf,3)
                            print("ocr_conf: ",ocr_conf)
                            # Draw on the image
                            
                            cv2.rectangle(img_tmp, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  # Red bounding box
                            cv2.putText(img_tmp, recognized_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                            cv2.putText(img_tmp, str(ocr_conf), (int(x1) + 150, int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                    except Exception as e:
                        print("----------------------------------------")
                        print("Error:", e)
                        print("----------------------------------------")
                        continue
                else:
                    # If there are no bounding boxes or the result is empty, skip this result
                    continue

            # Calculating time taken and FPS for the whole process.
            tot_time = time.time() - prev_time
            fps = round(1 / tot_time,2)

            # Writing information onto the frame and saving it to be processed in a video.
            cv2.putText(img_tmp, 'frame: %d fps: %s' % (ct, fps),
                        (0, int(100 * 1)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), thickness=2)
            out.write(img_tmp)

            ct = ct + 1
        else:
            break

def validate_plate(str_plate):

    regex_pattern = r'^\d{2}(-[A-HK-PR-Z]{2}|-[A-HK-PR-Z]{1}\d{1}|[A-HK-PR-Z]{1})[- ]?((?!000\.00)([0-9]\d{0,2}|0)\.\d{2}|[0-9]{4})$'  # [- ]?

    if re.match(regex_pattern, str_plate):
        return str_plate
    else:
        return None

def save_info_file(name_folder, name_file, data):
    # Check if the directory does not exist then create a new one
    if not os.path.exists(name_folder):
        os.makedirs(name_folder)

    # Create the full path to the file
    file_path = os.path.join(name_folder, f"{name_file}.txt")

    with open(file_path, 'a') as file:
        
        # Add data to the file
        for entry in data:
            file.write(f"{entry['Track_id']}\t{entry['Recognized_text']}\t{entry['Confidence']}\t{entry['Time']}\n")
            # file.write(f"{entry['Track_id']}\t{entry['Recognized_text']}\t{entry['Confidence']}\n")

    print("Data has been added to the file.")


def get_best_ocr(data, track_ids):
    counter_dict = Counter((item['track_id'], item['ocr_txt']) for item in data)

    most_common_recognized_text = {}
    rec_conf = ""
    ocr_res = ""
    for item in data:
        track_id = item['track_id']
        recognized_text = item['ocr_txt']
        confidence = item['ocr_conf']
        count = counter_dict[(track_id, recognized_text)]

        current_count, current_confidence, current_text = most_common_recognized_text.get(track_id, (0, 0, ''))

        if count > current_count or (count == current_count and confidence > current_confidence):
            most_common_recognized_text[track_id] = (count, confidence, recognized_text)

    if track_ids in most_common_recognized_text:
        rec_conf, ocr_res = most_common_recognized_text[track_ids][1], most_common_recognized_text[track_ids][2]

    return rec_conf, ocr_res

def tracker_test_vid_with_deep_sort(vid_dir,out_path):
    # Declaring variables for video processing.
    cap = cv2.VideoCapture(vid_dir)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    out = cv2.VideoWriter(out_path, codec, fps, (width, height))

    tracker = Tracker()
    preds = []

    list_plate = []
    time_out = ""

    # Initializing some helper variables.
    ct = 0
    preds = []
    CONFIDENCE_THRESHOLD = 0.3
    # Reading video frame by frame.
    time_folder = datetime.datetime.now().strftime("%Y-%m-%d")
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret == True:

            h, w = img.shape[:2]
            overlay_img = img.copy()
            prev_time = time.time()
            detections = model(img, imgsz=IMG_SIZE, conf=CONF)[0]
            # detections = model.track(img, persist=True)
            
            results = []

            datas = detections.boxes.data.tolist()
            
            for data in datas:
                # Get the conf of object detection
                confidence = data[4]
                
                if float(confidence) > CONFIDENCE_THRESHOLD:
                    # continue

                    # get the bounding box and the class id
                    xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
                    # print("Toạ do 1: ",xmin, ymin, xmax, ymax)
                    class_id = int(data[5])

                    # Thêm bounding box(x, y, w, h) và conf vào list
                    results.append([xmin, ymin, xmax, ymax, confidence])
            # Update các info vào tracker 
            tracker.update(img, results)
            # loop over the tracks
            for detection in detections:
                if detection.boxes is not None and len(detection.boxes) > 0:
                    try:
                        for track in tracker.tracks:

                        # Get track_id and bounding box
                            track_id = track.track_id
                            x1, y1, x2, y2 = track.bbox
                            
                            width = x2 - x1
                            height = y2 - y1
                            aspect_ratio = width / height

                            if 0 <= aspect_ratio <= 1.5:
                                # Cut and rotate the license plate --------------
                                image_upper, image_lower = rotate_and_split_license_plate(img[int(y1):int(y2), int(x1):int(x2)])

                                if image_upper is None and image_lower is None:
                                    # License plates are roughly square or square

                                    # Calculate the point that divides the image into upper and lower parts
                                    split_point = y1 + (y2 - y1) // 2

                                    # Create two subimage parts from the cr_img image
                                    upper_part = img[int(y1):int(split_point), int(x1):int(x2)]
                                    lower_part = img[int(split_point):int(y2), int(x1):int(x2)]

                                    image_upper=cv2.resize(upper_part,(int(width),int(height/2)))
                                    image_lower=cv2.resize(lower_part,(int(width),int(height/2)))

                                image_collage_horizontal =np.hstack([image_upper, image_lower])
                                image_filename = str(ct) + ".jpg"  # Tên file ảnh đầu ra
                                cv2.imwrite("results/crop_image/" + image_filename, image_collage_horizontal)

                                # Continue processing the cr_img rectangular image here
                                ocr_res = perform_ocr(image_collage_horizontal)
                                print('text:', ocr_res)

                                # Save two parts of the image
                                # cv2.imwrite("results/upper_part.jpg", upper_part)
                                # cv2.imwrite("results/" + str(ct) + ".jpg", lower_part)
                            else:
                                # The license plate is not nearly square
                                # Normal image processing here (cr_img = img[int(y1):int(y2), int(x1):int(x2)])
                                cr_img = img[int(y1):int(y2), int(x1):int(x2)]
                                image_filename = str(ct) + ".jpg"  # Tên file ảnh đầu ra
                                cv2.imwrite("results/crop_image/" + image_filename, cr_img)
                                ocr_res = perform_ocr(cr_img)
                                print('text:', ocr_res)

                            print('-------------------')
                            # Draw bounding box and put text
                            recognized_text = ocr_res[0][0][0] if ocr_res else "No Text"
                            print("recognized_text: ",recognized_text)

                            ocr_conf = ocr_res[0][0][1] if ocr_res else "No Conf"
                            ocr_conf = round(ocr_conf,3)
                            print("ocr_conf: ",ocr_conf)

                            output_frame = {"track_id": track_id, "ocr_txt": recognized_text, "ocr_conf": ocr_conf}
                            preds.append(output_frame)

                            if track_id in list(set(ele['track_id'] for ele in preds)):

                                rec_conf, ocr_resc = get_best_ocr(preds, track_id)
                            
                                ocr_resc_test = validate_plate(recognized_text)

                                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                
                                if ocr_resc_test != None and current_time != time_out:

                                    list_plate.append({'Track_id': track_id, 'Recognized_text': ocr_resc_test, 'Confidence': ocr_conf, "Time": current_time})
                                    save_info_file(f"./save_file_txt/{time_folder}", ocr_resc_test, [{'Track_id': track_id, 'Recognized_text': ocr_resc_test, 'Confidence': rec_conf, 'Time': current_time}])
                                    time_out = current_time

                                txt = str(track_id) + ": " + str(ocr_resc) + '-' + str(rec_conf)
                                # Draw bounding box and track id 
                                cv2.rectangle(overlay_img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                                cv2.putText(overlay_img, txt, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)   
                                cv2.putText(overlay_img, str(ocr_resc_test), (int(x1), int(y1) + 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                            else:
                                continue
                    except Exception as e:
                        continue
                else:
                    # If there are no bounding boxes or the result is empty, skip this result
                    continue
            
            tot_time = time.time() - prev_time
            fps = round(1 / tot_time,2)

            if w < 2000:
                size = 1
            else:
                size = 2
            
            cv2.putText(overlay_img, 'frame: %d fps: %s' % (ct, int(fps)),
                        (0, int(100 * 1)), cv2.FONT_HERSHEY_SIMPLEX, size, (0, 0, 255), thickness=2)
            out.write(overlay_img)
            # Increasing frame count.
            ct = ct + 1
        else:
            break

def tracker_test_vid_with_yolo_track(vid_dir,out_path):
    # Declaring variables for video processing.
    cap = cv2.VideoCapture(vid_dir)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    #   file_name = os.path.join(out_path, 'out_' + vid_dir.split('/')[-1])
    
    out = cv2.VideoWriter(out_path, codec, fps, (width, height))

    # Store tracks
    track_history = defaultdict(lambda: [])

    preds = []
    # Initializing some helper variables.
    ct = 0
    alpha = 0.5
    time_out = ""

    list_plate = []
    # Reading video frame by frame.
    time_folder = datetime.datetime.now().strftime("%Y-%m-%d")
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret:
            h, w = img.shape[:2]
            print(ct)
            
            w_scale = w/1.55
            h_scale = h/17
    
            # # Method to blend two images, here used to make the information box transparent.
            # overlay_img = img.copy()
            # cv2.rectangle(img, (int(w_scale), 0), (w, int(h_scale*3.4)), (0,0,0), -1)
            # cv2.addWeighted(img, alpha, overlay_img, 1 - alpha, 0, overlay_img)

        # Run YOLOv8 tracking on the frame, persisting tracks between frames
            
            prev_time = time.time()

            results = model.track(img, imgsz=IMG_SIZE, conf=CONF, persist=True)
            boxes = results[0].boxes.xyxy.cpu()
            boxes_ct = results[0].boxes.xywh.cpu()
            try:
                track_ids = results[0].boxes.id.int().cpu().tolist()

            except Exception as e:
                continue

            # print("Bbox: ", boxes)
            for result in results:
                if result.boxes is not None and len(result.boxes) > 0: 
                    try:
                        for box, box_ct ,track_id in zip(boxes, boxes_ct, track_ids):
                            x1, y1, x2, y2 = box
                            x, y ,w, h = box_ct

                            track = track_history[track_id]
                            track.append((float(x), float(y)))  # x, y center point
                            if len(track) > 30:  # retain 90 tracks for 90 frames
                                track.pop(0)

                            width = w
                            height = h
                            aspect_ratio = width / height

                            if 0 <= aspect_ratio <= 1.5:
                                # Cut and rotate the license plate --------------
                                image_upper, image_lower = rotate_and_split_license_plate(img[int(y1):int(y2), int(x1):int(x2)])

                                if image_upper is None and image_lower is None:
                                    # License plates are roughly square or square

                                    # Calculate the point that divides the image into upper and lower parts
                                    split_point = y1 + (y2 - y1) // 2

                                    # Create two subimage parts from the cr_img image
                                    upper_part = img[int(y1):int(split_point), int(x1):int(x2)]
                                    lower_part = img[int(split_point):int(y2), int(x1):int(x2)]

                                    image_upper=cv2.resize(upper_part,(int(width),int(height/2)))
                                    image_lower=cv2.resize(lower_part,(int(width),int(height/2)))

                                image_collage_horizontal =np.hstack([image_upper, image_lower])
                                image_filename = str(ct) + ".jpg"  # Output image file name
                                cv2.imwrite("results/crop_image/" + image_filename, image_collage_horizontal)

                                # Continue processing the cr_img rectangular image here
                                ocr_res = perform_ocr(image_collage_horizontal)
                                print('text:', ocr_res)

                                # Save two parts of the image
                                # cv2.imwrite("results/upper_part.jpg", upper_part)
                                # cv2.imwrite("results/" + str(ct) + ".jpg", lower_part)
                            else:
                                # The license plate is not nearly square
                                # Normal image processing here (cr_img = img[int(y1):int(y2), int(x1):int(x2)])
                                cr_img = img[int(y1):int(y2), int(x1):int(x2)]
                                image_filename = str(ct) + ".jpg"  # Tên file ảnh đầu ra
                                cv2.imwrite("results/crop_image/" + image_filename, cr_img)
                                ocr_res = perform_ocr(cr_img)
                                print('text:', ocr_res)

                            print('-------------------')
                            # Draw bounding box and put text
                            recognized_text = ocr_res[0][0][0] if ocr_res else "No Text"
                            print("recognized_text: ",recognized_text)

                            ocr_conf = ocr_res[0][0][1] if ocr_res else "No Conf"
                            ocr_conf = round(ocr_conf,3)
                            print("ocr_conf: ",ocr_conf)

                            output_frame = {"track_id": track_id, "ocr_txt": recognized_text, "ocr_conf": ocr_conf}
                            preds.append(output_frame)

                            # Add track_id to the list, if exists in the list.
                            if track_id in list(set(ele['track_id'] for ele in preds)):

                                rec_conf, ocr_resc = get_best_ocr(preds, track_id)
                            
                            ocr_resc_test = validate_plate(ocr_resc)

                            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                            
                            if ocr_resc_test != None and current_time != time_out:

                                list_plate.append({'Track_id': track_id, 'Recognized_text': ocr_resc_test, 'Confidence': ocr_conf, "Time": current_time})
                                save_info_file(f"./save_file_txt/{time_folder}", ocr_resc_test, [{'Track_id': track_id, 'Recognized_text': ocr_resc_test, 'Confidence': rec_conf, 'Time': current_time}])
                                time_out = current_time

                            txt = str(track_id) + ": " + str(ocr_resc) + '-' + str(rec_conf)
                            # txt = str(track_id) + ": "
                            # Draw bounding box and track id
                            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                            cv2.putText(img, txt, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                            
                    except Exception as e:
                        continue
                else:
                    continue
            
            tot_time = time.time() - prev_time
            fps = round(1 / tot_time,2)

            if w < 2000:
                size = 1
            else:
                size = 2
            
            cv2.putText(img, 'frame: %d fps: %s' % (ct, int(fps)),
                        (0, int(100 * 1)), cv2.FONT_HERSHEY_SIMPLEX, size, (0, 0, 255), thickness=2)
            out.write(img)
            # Increasing frame count.
            ct = ct + 1
        else:
            break

tracker_test_vid_with_yolo_track(INPUT_DIR,OUT_PATH)
# tracker_test_vid_with_deep_sort(INPUT_DIR, OUT_PATH)