from ultralytics import YOLO
import cv2
import os
import time
import numpy as np 
from paddleocr import PaddleOCR
INPUT_DIR = '../../test_video/test_1.mp4'
OUT_PATH = 'results/test_1.avi'
IMG_SIZE = 640
CONF = 0.6
ocr = PaddleOCR(lang='en',rec_algorithm='CRNN')
# Load a model
model = YOLO("../yolov8/alpr_yolov8n_8000img_100epochs.pt") 


def perform_ocr(image):
    ocr_res = ocr.ocr(image, cls=False, det=False)
    return ocr_res

def rotate_and_split_license_plate(image):
    # Chuyển đổi ảnh sang độ xám để dễ dàng xử lý
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Tìm các đường viền trong ảnh
    edges_image = cv2.Canny(gray_image, 100, 200, apertureSize=3, L2gradient=True) # dùng kernel 3x3 để phát hiện cạnh

    # Tìm các đoạn thẳng trong ảnh
    lines = cv2.HoughLines(edges_image, 1, np.pi / 180, threshold=100)
    # np.pi / 180: Giá trị tối thiểu cho góc theta (trong đơn vị radians)
    # threshold=100: Đây là ngưỡng (threshold) cho việc xem xét một đường thẳng.
    # Nếu có nhiều đường thẳng có cùng một góc và tương phản (sự tương quan) cao,
    # chỉ những đường thẳng có tương phản cao hơn ngưỡng này mới được xem xét là một đường thẳng hợp lệ.
    # Khi giá trị threshold thấp, nhiều đường thẳng sẽ được phát hiện;
    # khi nó cao, chỉ các đường thẳng rất rõ ràng mới được xem xét
    # chạy thử đoạn dưới đây để xem chi tiết
    # cv2.imshow("edges", edges)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Kiểm tra xem lines có giá trị hợp lệ hay không
    if lines is not None:
        # Lọc và chọn lựa đoạn thẳng phù hợp (đoạn thẳng có độ dài > threshold_length)
        threshold_length = 150
        filtered_lines = []
        # Tính toán góc xoay trung bình của các đoạn thẳng
        total_angle = 0
        count = 0

        for rho, theta in lines[:, 0]:
            if np.pi / 4 < theta < 3 * np.pi / 4:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * a)
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * a)
                line_length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if line_length > threshold_length:
                    filtered_lines.append(((x1, y1), (x2, y2)))
                
        if filtered_lines:
            # Lựa chọn đoạn thẳng dài nhất và thẳng nhất
            longest_line = max(filtered_lines, key=lambda x: np.linalg.norm(np.array(x[0]) - np.array(x[1])))
            x1, y1 = longest_line[0]
            x2, y2 = longest_line[1]
            # Vẽ đường thẳng dài nhất
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)



            # Tính góc xoay của đoạn thẳng
            rotation_angle = (np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi)

            # Xoay lại ảnh để biển số xe nằm ngang
            height, width = image.shape[:2]
            center = (width // 2, height // 2)
            rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1)
            rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

        # Tính toán điểm chia ảnh thành hai phần trên và dưới
        split_point = height // 2

        # Tạo hai phần ảnh con từ ảnh rotated_image
        upper_part = rotated_image[:split_point, :]
        lower_part = rotated_image[split_point:, :]

        # Điều chỉnh chiều cao của cả hai phần ảnh để chúng có cùng chiều cao
        upper_part = cv2.resize(upper_part, (int(width), int(height / 2)))
        lower_part = cv2.resize(lower_part, (int(width), int(height / 2)))

        print("FOUND LINES")
        print("rotate angle:", rotation_angle)
        return upper_part, lower_part
    else:
        print("NO LINES!")
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
        if ret:
            print(str(ct) + "/" + str(total_frames))

            # Noting time for calculating FPS.
            prev_time = time.time()

            # Use the model
            results = model(img, imgsz=IMG_SIZE, conf=CONF)  # predict on an image
            for result in results:
                if result.boxes is not None and len(result.boxes) > 0:
                    for bbox in result.boxes:
                        x1, y1, x2, y2 = bbox[0].xyxy[0]
                    # img = cv2.imread(input)  # Đảm bảo bạn đã định nghĩa biến 'input'
            
                        # Loop through bboxes and apply OCR, then draw on the image
                        try:
                            # Kiểm tra xem biển số xe có gần vuông không (ví dụ: tỷ lệ 1:1)
                            width = x2 - x1
                            height = y2 - y1
                            aspect_ratio = width / height
                            print("aspect_ratio:", aspect_ratio)
                
                            if 0 <= aspect_ratio <= 1.5:
                                # Cắt và xoay lại biển số xe --------------
                                image_upper, image_lower = rotate_and_split_license_plate(img[int(y1):int(y2), int(x1):int(x2)])

                                if image_upper is None and image_lower is None:
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
                                print('text:', ocr_res)
                
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
                                print('text:', ocr_res)

                            print('-------------------')
                            # Draw bounding box and put text
                            recognized_text = ocr_res[0][0][0] if ocr_res else "No Text"
                            print("recognized_text: ",recognized_text)
                            
                            ocr_conf = ocr_res[0][0][1] if ocr_res else "No Conf"
                            ocr_conf = round(ocr_conf,3)
                            print("ocr_conf: ",ocr_conf)

                            # Draw on the image
                            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  # Red bounding box
                            cv2.putText(img, recognized_text, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                            cv2.putText(img, str(ocr_conf), (int(x1) + 150, int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

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
            cv2.putText(img, 'frame: %d fps: %s' % (ct, fps),
                        (0, int(100 * 1)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), thickness=2)
            out.write(img)

            ct = ct + 1
        else:
            break


test_vid_yolov8(INPUT_DIR, OUT_PATH)