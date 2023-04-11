# 1. Giới thiệu chủ đề và mục tiêu của video
- Giới thiệu về edge computing (tính toán cận biên) và bài toán nhận diện biển số xe trên Raspberry Pi
- Mục tiêu của video là giúp người xem có thể tự cài đặt và sử dụng YOLO để nhận diện biển số xe trên Raspberry Pi

Chào mọi người, hôm nay chúng ta sẽ cùng tìm hiểu về edge computing hay còn gọi là tính toán cận biên, Edge computing là một phương pháp tính toán phân tán, đưa việc xử lý và lưu trữ dữ liệu gần với nguồn phát sinh và sử dụng dữ liệu. Điều này giúp giảm độ trễ, sử dụng băng thông và phụ thuộc vào tính toán trên server bằng cách xử lý dữ liệu cục bộ tại nguồn phát sinh.

Trong thời đại công nghệ 4.0, ứng dụng trí tuệ nhân tạo đang được sử dụng rộng rãi trong nhiều lĩnh vực, đặc biệt là trong lĩnh vực giao thông. Với YOLO và Raspberry Pi, chúng ta có thể tự thiết kế một hệ thống nhận diện biển số xe đơn giản và hiệu quả.

Mục tiêu của video này là giúp các bạn có thể tự cài đặt và sử dụng YOLO để nhận diện biển số xe trên Raspberry Pi. Chúng ta sẽ đi từng bước, giải thích chi tiết cách cài đặt và sử dụng YOLO để nhận diện biển số xe trên Raspberry Pi.

Vì vậy, hãy cùng mình bắt đầu và tìm hiểu cách cài đặt YOLO và sử dụng nó để nhận diện biển số xe trên Raspberry Pi trong phần tiếp theo của video nhé!


# 2. Thông tin cần chuẩn bị trước khi bắt đầu
- Giới thiệu về các thiết bị cần chuẩn bị (Raspberry Pi, camera, adapter,..)
- Cài đặt Yolo trên máy tính và pi

Trước khi chúng ta bắt đầu, chúng ta cần chuẩn bị một số thiết bị cần thiết.

Đầu tiên, chúng ta cần một Raspberry Pi. Raspberry Pi là một máy tính nhỏ gọn với kích thước tương đối nhỏ, nhưng vẫn có đủ khả năng để thực hiện các tác vụ cơ bản của một máy tính thông thường.

Tiếp theo, chúng ta cần một camera. Camera này sẽ được sử dụng để chụp ảnh biển số xe và đưa dữ liệu vào Raspberry Pi để xử lý, ở đây mình chưa mua được camera nên mình sẽ thay thế bằng cách quay video bằng điện thoại, 

Ngoài ra, chúng ta cũng cần một adapter để cấp nguồn cho Raspberry Pi. Adapter này có thể được mua từ các cửa hàng chuyên về các thiết bị điện tử hoặc các trang thương mại điện tử.

Sau khi chuẩn bị đầy đủ các thiết bị cần thiết, chúng ta sẽ bắt đầu cài đặt các công cụ và thực hiện bài toán nhận diện biển số xe trên Raspberry Pi.

# 3. Chuẩn bị video, hình ảnh biển số xe
- chuẩn bị hình ảnh và video test
	- Bộ dữ liệu được lấy từ link: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection gồm 443 ảnh biển số xe ô tô
	- Video test được quay bằng điện thoại với định dạng .mp4

# 4. Giới thiệu YOLOv8
## Giải thích cách YOLO hoạt động và các thông số quan trọng cần chú ý

- Mô hình YOLO (You Only Look Once) là một mô hình học sâu được sử dụng cho việc nhận diện đối tượng trong ảnh và video. Nó được thiết kế để nhận diện và phân loại các đối tượng đồng thời trong một khung hình. Mô hình YOLO sử dụng một mạng nơ-ron tích chập để xác định vị trí, kích thước và loại của các đối tượng trong ảnh và đưa ra các dự đoán trong thời gian thực. Với độ chính xác cao và khả năng xử lý nhanh, YOLO đã trở thành một trong những mô hình phổ biến nhất trong lĩnh vực nhận diện đối tượng.

### Sự phát triển của YOLO
- yolo xuất hiện từ năm 2015, đã phát triển qua nhất nhiều phiên bản, chúng ta có thể nhìn thấy các phiên bản như trên hình. 
![evolution-of-yolo-models-1024x576](https://user-images.githubusercontent.com/13607004/231107354-1303dbc2-9948-4e42-90a6-0386f37b7823.png)
  - YOLOv1: Phiên bản đầu tiên của mô hình YOLO, đó là YOLOv1 đã được xuất bản bởi Joseph Redmon et al. vào năm 2015. Đây là mô hình phát hiện đối tượng (SSD - single stage object detection) single stage đầu tiên đã tạo ra các mô hình SSD và tất cả các mô hình YOLO tiếp theo.
  - YOLOv2: còn được gọi là YOLO 9000 được xuất bản bởi tác giả gốc của YOLOv1, Joseph Redmon. Nó đã cải thiện YOLOv1 bằng cách giới thiệu khái niệm anchor boxes và backbone tốt hơn, đó là Darknet-19.
  - YOLOv3: Năm 2018, Joseph Redmon và Ali Farhadi đã xuất bản YOLOv3. YOLOv3 sử dụng backbone Darknet-53, loại bỏ các kết nối dư thừa, pretrain tốt hơn và các kỹ thuật tăng cường hình ảnh để đem lại những cải tiến.
  - Ultralytics YOLO Object Detection Models: Tất cả các mô hình phát hiện đối tượng YOLO cho đến YOLOv3 đều được viết bằng ngôn ngữ lập trình C và sử dụng framework Darknet. Những người mới học sẽ gặp khó khăn khi đọc code và tinh chỉnh các mô hình. Cùng khoảng thời gian với YOLOv3, Ultralytics đã phát hành mô hình YOLO (YOLOv3) đầu tiên được triển khai bằng framework PyTorch. Nó cũng dễ tiếp cận và dễ sử dụng hơn cho việc transfer learning. Ngay sau khi xuất bản YOLOv3, Joseph Redmon đã rời khỏi cộng đồng nghiên cứu Thị giác máy tính. YOLOv4 (của Alexey và cộng sự) là mô hình YOLO cuối cùng được viết trên Darknet. Sau đó đã có rất nhiều mô hình YOLO khác nhau. Trong đó YOLOv4, YOLOX, PP-YOLO, YOLOv6 và YOLOv7 là một số mô hình nổi bật. Sau YOLOv3, Ultralytics cũng phát hành YOLOv5 thậm chí còn tốt hơn, nhanh hơn và dễ sử dụng hơn tất cả các mô hình YOLO khác. Tính đến thời điểm hiện tại, Ultralytics đã xuất bản YOLOv8, đây có lẽ là mô hình YOLO tốt nhất cho đến nay.

- Trong YOLO version 8, có 1 số key features như sau:
  - user-friendly API (Command Line + Python): thay vì việc phải viết code python để thực hiện training, detect, với yolov8, bạn không cần phải thực hiện điều đó mà có thể thực hiện luôn trên dòng lệnh, chỉ cần import thư viện là xong
  - faster and more accurate
 Việc xử lý nhanh hơn và chính xác hơn
  - Suport: 
	  + Object Detection, (nhận dạng vật thể)
	  + Instance Segmentation, (phân vùng ảnh)
	  + Image Classification, (phân loại ảnh)
  - New backbone network: sử dụng backbone mới 
  - New Anchor-Free head
  - New Loss Function.
  - Flexible supporting numerous export formats (can run on CPUs & GPUs): hỗ trợ expor tmodel ra nhiều format khác nhau.

- Pretrain Model
Có năm mô hình trong mỗi danh mục mô hình YOLOv8 để detection, segmentation và classification. YOLOv8 Nano là nhanh nhất và nhỏ nhất, trong khi YOLOv8 Extra Large (YOLOv8x) là chính xác nhất nhưng chậm nhất.
YOLOv8 đi kèm với các mô hình được đào tạo trước sau đây:
	- Object Detection được đào tạo trên bộ dữ liệu COCO detection với độ phân giải hình ảnh là 640.
	- Instance segmentation được đào tạo trên bộ dữ liệu COCO segmentation với độ phân giải hình ảnh là 640.
	- Các mô hình Image classification được đào tạo trước trên bộ dữ liệu ImageNet với độ phân giải hình ảnh là 224.

- Cài đặt YOLOv8
  + Cài trực tiếp
```
pip install ultralytics
```
  + Cài bằng docker : tải yolov8 docker image từ docker hub
  - dành cho máy có GPU:
  ```
  docker pull ultralytics/ultralytics:latest
  ```
  - Dành cho máy không có GPU:
  ```
  docker pull ultralytics/ultralytics:latest-cpu
  ```
  - Dành cho máy có chip ARM như MacOS, Jetson Nano, Raspberry Pi,...
  ```
  docker pull ultralytics/ultralytics:latest-arm64
  ```

# 5. Nhận diện biển số xe
- chuẩn hóa dữ liệu
```
mkdir -p datasets/train/labels
mkdir -p datasets/train/images
mkdir -p datasets/val/labels
mkdir -p datasets/val/images

# copy image
cp ./archive/images dataset/train/images
cp ./archive/images/Cars1*.png dataset/train/images

#copy anotation
cp ./dataset/train/labels/Cars1*.txt dataset/val/labels
```
- tạo file .yaml
```
path:  datasets  # dataset root dir
train: train/images  # train images 
# val: val/images # val images 
val:
test:  # test images (optional)

# Classes
names:
  0: plate
```
- Train model


- test trên video tại PC 
- copy model vào pi
- test trên video tại Pi 
- Tính FPS
Speed: 0.7ms preprocess, 41.9ms inference, 0.5ms postprocess per image at shape (1, 3, 640, 640)
Đây là thông số về tốc độ xử lý của mô hình máy học khi thực hiện dự đoán trên ảnh có kích thước (1, 3, 640, 640), trong đó:

Preprocess (tiền xử lý): thời gian xử lý trước khi đưa ảnh vào mô hình, là 0.7 miligiây (ms).
Inference (dự đoán): thời gian mô hình thực hiện dự đoán trên ảnh, là 41.9 ms.
Postprocess (sau xử lý): thời gian xử lý sau khi mô hình dự đoán, là 0.5 ms.
Tổng thời gian để mô hình xử lý ảnh là khoảng 43.1ms, được tính bằng tổng của preproces, inference và postprocess. Kết quả này thường được sử dụng để đánh giá hiệu suất của mô hình máy học trong các ứng dụng thực tế.

Để tính toán số khung hình trên giây (FPS) tương ứng với thời gian xử lý của mô hình, ta có thể sử dụng công thức:

FPS = 1000 / (Preprocess + Inference + Postprocess)

Trong trường hợp này, thời gian Preprocess là 0.7ms, thời gian Inference là 41.9ms và thời gian Postprocess là 0.5ms. Thay vào công thức ta có:

FPS = 1000 / (0.7 + 41.9 + 0.5) = 22.63

Vậy, FPS của mô hình khi xử lý ảnh kích thước (1, 3, 640, 640) là khoảng 22.63, tức là mô hình có thể xử lý được 22.63 khung hình trong một giây.

# 6. Kết luận
- Tóm tắt lại các bước cần thực hiện để cài đặt và sử dụng YOLO và Tesseract OCR trên Raspberry Pi để nhận diện biển số xe
- Khuyến khích người xem thực hiện thử các bước này để có thể áp dụng vào các ứng dụng thực tế.

# 7. Hướng dẫn bổ sung (nếu có)
- Nếu có, cung cấp các hướng dẫn bổ sung hoặc các tài liệu tham khảo để người xem có thể tìm hiểu thêm về chủ đề này.
