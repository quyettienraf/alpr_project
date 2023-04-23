# CHƯƠNG 2: CÁC CÔNG TRÌNH LIÊN QUAN
Bài toán nhận dạng biển số xe là một trong những bài toán quan trọng trong lĩnh vực nhận diện văn bản ngoại cảnh. Vì vậy, các nghiên cứu liên quan đến hai bài toán này thường có sự tương quan mật thiết. Trong những năm gần đây, bài toán nhận diện biển số xe đã được quan tâm nhiều và có sự phát triển đáng kể. Thông thường, bài toán nhận dạng biển số xe bao gồm một số bước cơ bản như sau:

![Untitled](https://user-images.githubusercontent.com/13607004/233845181-e2a76ae9-1727-4aca-b81d-e0c664c1c911.png)

<i> Các bước cơ bản của một hệ thống nhận diện biển số xe </i>

Từ những bước trên, có ba bài toán chính cần được giải quyết trong việc nhận dạng biển số xe: phát hiện vị trí của biển số trên hình, phân đoạn các ký tự trong biển số và nhận diện chuỗi ký tự trên biển số. Dựa trên những nghiên cứu mới đây, đề tài nhận thấy rằng hướng tiếp cận nhận dạng chuỗi ký tự trên biển số mà không phải qua bước phân đoạn ký tự rất tiềm năng, vì có nhiều ưu điểm hơn. Do đó, đề tài tập trung vào khảo sát các công trình liên quan đến phát hiện vị trí của biển số và nhận diện ký tự trên biển số. Ngoài ra, trong số các nghiên cứu gần đây còn đề cập đến việc kết hợp xử lý cả hai quá trình phát hiện và nhận dạng một cách đồng thời, tạo ra một phương pháp tổng thể hiệu quả hơn để giải quyết bài toán này.

## 2.1 Phát hiện biển số xe
### 2.1.1 Các phương pháp trích xuất đặc trưng thủ công
Trong quá khứ, các phương pháp trích đặc trưng thủ công được sử dụng phổ biến trong việc phân tích ảnh. Những đặc trưng thường được sử dụng bao gồm các đặc trưng cơ bản như góc, cạnh, vân ảnh, màu sắc và mức sáng. Các phương pháp phổ biến để trích xuất các đặc trưng này bao gồm việc nhị phân hóa ảnh, sử dụng thuật toán SIFT, HOG, phân tích thành phần liên thông và hình thái học. Sau đó, các đặc trưng này được đưa qua các bộ phân loại như AdaBoost, SVM để phân loại.

Các phương pháp trích xuất đặc trưng cơ bản thường đơn giản, dễ hiện thực và nhanh chóng, đặc biệt là khi kết hợp nhiều đặc trưng với nhau, kết quả có thể đạt được độ chính xác tương đối cao. Tuy nhiên, các phương pháp này có nhược điểm là khá nhạy cảm với sự thay đổi mức sáng, nhiễu và mờ. Hơn nữa, việc thiết kế bộ rút trích đặc trưng còn phụ thuộc khá nhiều vào tập dữ liệu, do đó cần phải đảm bảo tập dữ liệu đủ đa dạng để đảm bảo tính chính xác của phương pháp trích xuất.

### 2.1.2 Các phương pháp học sâu
Hiện nay, phương pháp học sâu được sử dụng để phát hiện đối tượng rất đa dạng và hiệu quả. Có nhiều kiến trúc mạng được áp dụng, ví dụ như Faster RCNN, SSD, YOLO và YOLO2. Các kiến trúc này tỏ ra hiệu quả trong việc phát hiện nhiều đối tượng trong cùng một ảnh.

Mạng Faster RCNN 

Kiến trúc mạng Faster RCNN được xây dựng bao gồm 3 phần chính. Phần đầu tiên là một mạng rút trích đặc trưng cơ bản, phần thứ hai là lớp mạng đề xuất vùng dự tuyển Region Proposal Network (RPN) và phần cuối cùng là lớp mạng dự đoán vị trí và phân loại đối tượng. Khi ảnh đầu vào được đưa qua phần mạng rút trích đặc trưng, nó sẽ cho ra một bản đồ đặc trưng (feature map). Sau đó, bản đồ đặc trưng này sẽ được đưa qua lớp mạng RPN để tạo ra các vùng dự tuyển. Các vùng dự tuyển sẽ được đưa về cùng kích thước thông qua lớp Roi Pooling. Sau đó, việc phân loại đối tượng cũng như dự đoán vị trí sẽ được thực hiện trên các vùng dự tuyển này.

Cải tiến lớn nhất của Faster RCNN so với mạng Fast RCNN đến từ việc sử dụng lớp mạng RPN để thay thế cho giải thuật tìm kiếm vét cạn. Điều này đã cải thiện đáng kể tốc độ chạy của mô hình.

![Faster-R-CNN-Architecture-9](https://user-images.githubusercontent.com/13607004/233851041-d69a4ae1-4dbe-45b5-a604-0ea257a8255a.png)

<i> Kiến trúc mạng Faster RCNN </i>

Mạng Faster RCNN có nhiều ưu điểm, trong đó đáng chú ý nhất là tốc độ và độ chính xác được cải thiện đáng kể so với phiên bản trước đó. Tuy nhiên, một nhược điểm của kiến trúc này là việc sử dụng một lớp bản đồ đặc trưng có thể dẫn đến việc bỏ sót các đối tượng nhỏ và do đó giảm độ chính xác so với các phương pháp học sâu khác.

<b> Mạng Single Shot Multibox Detector (SSD)</b>

Mạng Single Shot Multibox Detector (SSD) là một mạng học sâu được thiết kế để phát hiện và phân loại đối tượng trong hình ảnh. Khác với phương pháp truyền thống sử dụng cửa sổ trượt với kích thước cố định, SSD tạo ra một tập hợp các ô chuẩn (default box) để xác định vị trí và lớp của các đối tượng trong quá trình huấn luyện. Việc sử dụng các ô chuẩn giúp cho mạng có khả năng dự đoán kích thước của các đường bao chữ nhật quanh vị trí của đối tượng một cách chính xác.

SSD áp dụng các ô chuẩn trên nhiều lớp bản đồ đặc trưng với các kích thước khác nhau để phát hiện được những đối tượng có kích thước lớn hoặc nhỏ khác nhau. Điều này giúp cho SSD có khả năng phát hiện đối tượng một cách hiệu quả và đồng thời giảm thiểu số lượng các phép tính cần thiết để xác định vị trí và lớp của đối tượng.

Mạng SSD được thiết kế với kiến trúc đầy đủ từ lớp mạng nền cho tới các lớp dự đoán vị trí và phân loại. Điều này giúp cho mạng có khả năng tích hợp việc phân loại và phát hiện vị trí trong cùng một mạng, tăng độ chính xác và giảm thời gian xử lý so với phương pháp truyền thống.

Tuy nhiên, một điểm hạn chế của SSD là số lượng các ô chuẩn lớn có thể gây khó khăn trong quá trình huấn luyện do đòi hỏi nhiều bộ nhớ hơn.

<img width="1040" alt="Screenshot 2023-04-23 at 23 13 00" src="https://user-images.githubusercontent.com/13607004/233851282-34c2dd2b-2fcc-4a79-b9ca-893b62ab382c.png">

<i>Kiến trúc mạng SSD</i>

Mô hình YOLO (You Only Look Once) 

Mô hình YOLO (You Only Look Once) là một mô hình học sâu được sử dụng cho việc nhận diện đối tượng trong ảnh và video. Nó được thiết kế để nhận diện và phân loại các đối tượng đồng thời trong một khung hình. Mô hình YOLO sử dụng một mạng nơ-ron tích chập để xác định vị trí, kích thước và loại của các đối tượng trong ảnh và đưa ra các dự đoán trong thời gian thực. Với độ chính xác cao và khả năng xử lý nhanh, YOLO đã trở thành một trong những mô hình phổ biến nhất trong lĩnh vực nhận diện đối tượng. YOLO xuất hiện từ năm 2015, đã phát triển qua nhất nhiều phiên bản, chúng ta có thể nhìn thấy các phiên bản như trên hình.           

![231107354-1303dbc2-9948-4e42-90a6-0386f37b7823](https://user-images.githubusercontent.com/13607004/233851547-30dd2283-23a8-44c2-bbc1-e5b73f080096.png)

<i> Sự phát triển của YOLO </i>

- YOLOv1: Phiên bản đầu tiên của mô hình YOLO, đó là YOLOv1 đã được xuất bản bởi Joseph Redmon et al. vào năm 2015. Đây là mô hình phát hiện đối tượng (SSD - single stage object detection) single stage đầu tiên đã tạo ra các mô hình SSD và tất cả các mô hình YOLO tiếp theo.
- YOLOv2: còn được gọi là YOLO 9000 được xuất bản bởi tác giả gốc của YOLOv1, Joseph Redmon. Nó đã cải thiện YOLOv1 bằng cách giới thiệu khái niệm anchor boxes và backbone tốt hơn, đó là Darknet-19.
- YOLOv3: Năm 2018, Joseph Redmon và Ali Farhadi đã xuất bản YOLOv3. YOLOv3 sử dụng backbone Darknet-53, loại bỏ các kết nối dư thừa, pretrain tốt hơn và các kỹ thuật tăng cường hình ảnh để đem lại những cải tiến.
- Ultralytics YOLO Object Detection Models: Tất cả các mô hình phát hiện đối tượng YOLO cho đến YOLOv3 đều được viết bằng ngôn ngữ lập trình C và sử dụng framework Darknet. Những người mới học sẽ gặp khó khăn khi đọc code và tinh chỉnh các mô hình. Cùng khoảng thời gian với YOLOv3, Ultralytics đã phát hành mô hình YOLO (YOLOv3) đầu tiên được triển khai bằng framework PyTorch. Nó cũng dễ tiếp cận và dễ sử dụng hơn cho việc transfer learning. Ngay sau khi xuất bản YOLOv3, Joseph Redmon đã rời khỏi cộng đồng nghiên cứu Thị giác máy tính. YOLOv4 (của Alexey và cộng sự) là mô hình YOLO cuối cùng được viết trên Darknet. Sau đó đã có rất nhiều mô hình YOLO khác nhau. Trong đó YOLOv4, YOLOX, PP-YOLO, YOLOv6 và YOLOv7 là một số mô hình nổi bật. Sau YOLOv3, Ultralytics cũng phát hành YOLOv5 thậm chí còn tốt hơn, nhanh hơn và dễ sử dụng hơn tất cả các mô hình YOLO khác. Tính đến thời điểm hiện tại, Ultralytics đã xuất bản YOLOv8, đây có lẽ là mô hình YOLO tốt nhất cho đến nay.            

YOLOv8
- Sử dụng kiến trúc mạng nơ-ron tích chập (CNN) mới nhất, bao gồm các khối ResNet, CSP và SPP, để tăng độ chính xác và giảm thời gian huấn luyện.
- Áp dụng kỹ thuật học chuyển tiếp (transfer learning) để tận dụng các trọng số được huấn luyện trước trên các bộ dữ liệu lớn như COCO và ImageNet, giúp tiết kiệm thời gian và tài nguyên.
- Hỗ trợ nhiều định dạng đầu vào và đầu ra khác nhau, bao gồm ảnh, video, webcam, RTSP và ONNX. Ngoài ra, YOLOv8 cũng có thể xuất ra các kết quả dưới dạng JSON, CSV hoặc PASCAL VOC.
- Cung cấp nhiều tùy chọn để tùy biến mô hình theo nhu cầu của người dùng, bao gồm việc thay đổi kích thước ảnh, số lượng lớp, ngưỡng tin cậy và tốc độ khung hình.
- Có thể phát hiện và phân đoạn các đối tượng trong ảnh một cách tự động, sử dụng các phương pháp như phát hiện biên giới (boundary detection), phân vùng ngữ nghĩa (semantic segmentation) và phân vùng thể hiện (instance segmentation).
            
Ưu điểm:
- Có thể phát hiện đối tượng nhanh chóng và chính xác, với tốc độ lên đến 140 khung hình/giây trên GPU và 3 khung hình/giây trên CPU.  

Nhược điểm:
- Cần nhiều tài nguyên để huấn luyện và chạy mô hình, do đó có thể không phù hợp cho các thiết bị nhúng hoặc có dung lượng thấp.
- Có thể gặp khó khăn khi phát hiện các đối tượng nhỏ, che khuất hoặc có hình dạng không đều.
- Có thể bị ảnh hưởng bởi các yếu tố ngoại cảnh như ánh sáng, nhiễu hoặc chuyển động.
            
