# I. Giới thiệu chủ đề và mục tiêu của video
- Giới thiệu về việc cài đặt YOLO, Tesseract OCR và bài toán nhận diện biển số xe trên Raspberry Pi
- Mục tiêu của video là giúp người xem có thể tự cài đặt và sử dụng YOLO và Tesseract OCR để nhận diện biển số xe trên Raspberry Pi

Chào mừng các bạn đến với video hướng dẫn cài đặt YOLO và Tesseract OCR để nhận diện biển số xe trên Raspberry Pi. Trong video này, chúng ta sẽ tìm hiểu cách cài đặt YOLO và Tesseract OCR sau đó sử dụng nó để nhận diện biển số xe trên Raspberry Pi.

Trong thời đại công nghệ 4.0, ứng dụng trí tuệ nhân tạo đang được sử dụng rộng rãi trong nhiều lĩnh vực, đặc biệt là trong lĩnh vực giao thông. Với YOLO, Tesseract OCR và Raspberry Pi, chúng ta có thể tự thiết kế một hệ thống nhận diện biển số xe đơn giản và hiệu quả.

Mục tiêu của video này là giúp các bạn có thể tự cài đặt và sử dụng YOLO để nhận diện biển số xe trên Raspberry Pi. Chúng ta sẽ đi từng bước, giải thích chi tiết cách cài đặt và sử dụng YOLO để nhận diện biển số xe trên Raspberry Pi.

Vì vậy, hãy cùng mình bắt đầu và tìm hiểu cách cài đặt YOLO và sử dụng nó để nhận diện biển số xe trên Raspberry Pi trong phần tiếp theo của video nhé!


# II. Thông tin cần chuẩn bị trước khi bắt đầu
- Giới thiệu về các thiết bị cần chuẩn bị (Raspberry Pi, camera, adapter,..)
- Cài đặt Yolo trên máy tính và pi

Trước khi chúng ta bắt đầu cài đặt YOLO và nhận diện biển số xe trên Raspberry Pi, chúng ta cần chuẩn bị một số thiết bị và phần mềm cần thiết.

Đầu tiên, chúng ta cần có một board Raspberry Pi, một camera để quay phim và chụp ảnh, ở đây mình chưa mua được camera nên mình sẽ thay thế bằng cách quay video bằng điện thoại, một adapter để cấp nguồn cho Raspberry Pi. 

Vì vậy, trước khi bắt đầu cài đặt YOLO và nhận diện biển số xe trên Raspberry Pi, hãy đảm bảo rằng bạn đã chuẩn bị đầy đủ các thiết bị để tiếp tục với các bước tiếp theo trong video.

# IV. Chuẩn bị video, hình ảnh biển số xe
- chuẩn bị hình ảnh và video test

# V. Giới thiệu YOLOv8
## Giải thích cách YOLO hoạt động và các thông số quan trọng cần chú ý

- Mô hình YOLO (You Only Look Once) là một mô hình học sâu được sử dụng cho việc nhận diện đối tượng trong ảnh và video. Nó được thiết kế để nhận diện và phân loại các đối tượng đồng thời trong một khung hình. Mô hình YOLO sử dụng một mạng nơ-ron tích chập để xác định vị trí, kích thước và loại của các đối tượng trong ảnh và đưa ra các dự đoán trong thời gian thực. Với độ chính xác cao và khả năng xử lý nhanh, YOLO đã trở thành một trong những mô hình phổ biến nhất trong lĩnh vực nhận diện đối tượng.

- yolo xuất hiện từ năm 2015, đã phát triển qua nhất nhiều phiên bản, chúng ta có thể nhìn thấy các phiên bản như trên hình. 
![evolution-of-yolo-models-1024x576](https://user-images.githubusercontent.com/13607004/231107354-1303dbc2-9948-4e42-90a6-0386f37b7823.png)
  - YOLOv1: Phiên bản đầu tiên của mô hình YOLO, đó là YOLOv1 đã được xuất bản bởi Joseph Redmon et al. vào năm 2015. Đây là mô hình phát hiện đối tượng (SSD - single stage object detection) single stage đầu tiên đã tạo ra các mô hình SSD và tất cả các mô hình YOLO tiếp theo.


- hiện nay yolo đã phát triển đến version 8, có 1 số tính năng chính như sau:
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

- Cài đặt YOLOv8
  + Cài trực tiếp
  + Cài bằng docker 

- Pretrain Model



# VI. Nhận diện biển số xe
- chuẩn hóa dữ liệu
- tạo file .yaml
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

# VII. Kết luận
- Tóm tắt lại các bước cần thực hiện để cài đặt và sử dụng YOLO và Tesseract OCR trên Raspberry Pi để nhận diện biển số xe
- Khuyến khích người xem thực hiện thử các bước này để có thể áp dụng vào các ứng dụng thực tế.

# VII. Hướng dẫn bổ sung (nếu có)
- Nếu có, cung cấp các hướng dẫn bổ sung hoặc các tài liệu tham khảo để người xem có thể tìm hiểu thêm về chủ đề này.
