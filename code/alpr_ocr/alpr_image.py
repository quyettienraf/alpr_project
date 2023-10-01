from ultralytics import YOLO
import cv2
import os
import glob
import numpy as np 
from paddleocr import PaddleOCR 

ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')
# Load a model
model = YOLO("../yolov8/alpr_yolov8n_8000img_100epochs.pt") 

def perform_ocr(image):
    ocr_res = ocr.ocr(image, cls=False, det=False)
    return ocr_res

def test_img_yolov8(input, out_path):
    file_name = input.split("/")[-1]
    print("file_name:", file_name)
    # Use the model
    results = model(input)  # predict on an image
    img = cv2.imread(input)
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
                
                if 0 <= aspect_ratio <= 1.5:
                    # Biển số xe gần vuông hoặc hình vuông
    
                    # Tính toán điểm chia ảnh thành hai phần trên và dưới
                    split_point = y1 + (y2 - y1) // 2

                    
                    # Tạo hai phần ảnh con từ ảnh cr_img
                    upper_part = img[int(y1):int(split_point), int(x1):int(x2)]
                    lower_part = img[int(split_point):int(y2), int(x1):int(x2)]
                    
                    image_upper=cv2.resize(upper_part,(int(width),int(height/2)))
                    image_lower=cv2.resize(lower_part,(int(width),int(height/2)))

                    image_collage_horizontal =np.hstack([image_upper, image_lower])
                    image_filename = str(file_name) + ".jpg"  # Tên file ảnh đầu ra
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
                    
                    
                    image_filename = str(file_name) + ".jpg"  # Tên file ảnh đầu ra
                    cv2.imwrite("results/crop_image/" + image_filename, cr_img)
                    ocr_res = perform_ocr(cr_img)
            recognized_text = ocr_res[0][0][0] if ocr_res else "No Text"
            print("recognized_text: ",recognized_text)
            
            ocr_conf = ocr_res[0][0][1] if ocr_res else "No Conf"
            ocr_conf = round(ocr_conf,3)
            print("ocr_conf: ",ocr_conf)
            # Draw on the image
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  # Red bounding box
            cv2.putText(img, recognized_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(img, str(ocr_conf), (int(x1) + 150, int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # Writing output image for each image
        file_name = os.path.join(out_path, 'out_' + os.path.basename(input))
        cv2.imwrite(file_name, img)
    

def perform_ocr(image):
    ocr_res = ocr.ocr(image, cls=False, det=False)
    return ocr_res


# Usage example
files = glob.glob('../../datasets/yolo_plate_dataset/val/images/*.jpg', recursive = True)

x = 0
y = len(files)
for file in files:
    x = x + 1
    print(str(x) + "/" + str(y))
    test_img_yolov8(file, './results')