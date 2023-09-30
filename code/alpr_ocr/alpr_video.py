from ultralytics import YOLO
import cv2
import os
import time
import numpy as np 
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')
# Load a model
model = YOLO("../yolov8/alpr_yolov8n_8000img_100epochs.pt") 


def perform_ocr(image):
    ocr_res = ocr.ocr(image, cls=False, det=False)
    return ocr_res


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
                    
                    for bbox in bboxes:
                        xyxy = bbox.xyxy
                        x1, y1, x2, y2 = xyxy[0]
            
                        # Kiểm tra xem biển số xe có gần vuông không (ví dụ: tỷ lệ 1:1)
                        width = x2 - x1
                        height = y2 - y1
                        aspect_ratio = width / height
                        print("aspect_ratio:", aspect_ratio)
            
                        if 0 <= aspect_ratio <= 2:
                            # Biển số xe gần vuông hoặc hình vuông
            
                            # Tính toán điểm chia ảnh thành hai phần trên và dưới
                            split_point = y1 + (y2 - y1) // 2

                            
                            # Tạo hai phần ảnh con từ ảnh cr_img
                            upper_part = img[int(y1):int(split_point), int(x1):int(x2)]
                            lower_part = img[int(split_point):int(y2), int(x1):int(x2)]
                            
                            image_upper=cv2.resize(upper_part,(int(width),int(height/2)))
                            image_lower=cv2.resize(lower_part,(int(width),int(height/2)))

                            image_collage_horizontal =np.hstack([image_upper, image_lower])
                            image_filename = str(ct) + ".jpg"  # Tên file ảnh đầu ra
                            cv2.imwrite("results/crop_image/" + image_filename, image_collage_horizontal)
            
                            # Tiếp tục xử lý ảnh chữ nhật cr_img ở đây
                            ocr_res = perform_ocr(image_collage_horizontal)
            
                            # Lưu hai phần ảnh
                            # cv2.imwrite("results/upper_part.jpg", upper_part)
                            # cv2.imwrite("results/" + str(ct) + ".jpg", lower_part)
                        else:
                            # Biển số xe không gần vuông
                            # Xử lý ảnh bình thường ở đây (cr_img = img[int(y1):int(y2), int(x1):int(x2)])
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

input_dir = '../../test_video/test_1.mp4'
out_path = 'results/test_1.avi'
test_vid_yolov8(input_dir, out_path)