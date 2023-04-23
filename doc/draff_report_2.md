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
            
## 2.2. Nhận diện biển số xe
### 2.2.1. Phương pháp so trùng mẫu (Template matching)
Phương pháp so trùng mẫu được sử dụng để phân loại các đối tượng dựa trên sự tương tự giữa chúng và một mẫu được cho trước. Trong bài toán nhận diện biển số xe, mẫu được sử dụng là một tập hợp các ký tự. Phương pháp này thường được áp dụng trên ảnh xám hoặc ảnh nhị phân.

Các độ đo khoảng cách như khoảng cách Mahalanobis, khoảng cách Jaccard và khoảng cách Hamming được sử dụng để so sánh các đối tượng với mẫu. Độ chính xác của phương pháp này phụ thuộc vào độ tương đồng giữa đối tượng và mẫu.

Mặc dù phương pháp so trùng mẫu đơn giản và dễ thực hiện, nhưng nó cũng có những hạn chế. Trong thực tế, kích thước của các ký tự phải cố định để áp dụng phương pháp này. Ngoài ra, phương pháp này cũng rất nhạy cảm với nhiễu, sự thay đổi mức sáng và góc quay của đối tượng. Vì vậy, việc áp dụng phương pháp này trong các bài toán thực tế có thể gặp khó khăn.

### 2.2.2 Phương pháp học sâu
Các phương pháp nhận diện biển số xe thường hoạt động trên tập dữ liệu là hình ảnh biển số xe đã được cắt sẵn. Tập dữ liệu này chỉ chứa thông tin về chuỗi ký tự trên biển số xe mà không có thông tin về vị trí của từng ký tự trong hình. Ngoài ra, các chuỗi ký tự này thường chỉ nằm trên một hàng.

Mạng ConvNet-RNN [4]:
Phương pháp nhận diện biển số xe sử dụng kiến trúc mạng gồm lớp mạng VGG [14] và lớp mạng RNN. Đầu tiên, ảnh đầu vào được đưa qua lớp mạng VGG [14] để trích xuất đặc trưng. Sau đó, các đặc trưng được chuyển thành các vector và đưa vào lớp RNN để nhận dạng các ký tự tương ứng.

Phương pháp này có hiệu quả tốt hơn so với phương pháp cửa sổ trượt và không yêu cầu phân đoạn dữ liệu huấn luyện trước. Tuy nhiên, phương pháp này có hạn chế là tỷ lệ nhận dạng sai khá cao cho các cặp ký tự M và N, D và Q, T và Y, C và G.

<img width="380" alt="Screenshot 2023-04-24 at 03 39 29" src="https://user-images.githubusercontent.com/13607004/233865146-e28a45ac-c64d-414f-b56e-388bc5c092e5.png">


<i> Mạng ConvNet-RNN </i>

Mạng CRNN [1]:
Phương pháp này sử dụng hai lớp mạng chính: một lớp mạng neural network tích chập (CNN) để trích xuất đặc trưng và một lớp mạng Long-Short Term Memory (LSTM) cho việc nhận dạng các ký tự. Lớp mạng LSTM được thiết kế để chạy độc lập theo hai chiều (gọi là Bidirectional LSTM hoặc BiLSTM). Đầu vào cho lớp BiLSTM là bản đồ đặc trưng được biến đổi từ đầu ra của lớp CNN. Cuối cùng, lớp BiLSTM được kết nối với hàm lỗi Connectionist Temporal Classification (CTC), cho phép chuyển đổi các vector đặc trưng thành chuỗi các xác suất và tìm ra được chuỗi có tổng xác suất là lớn nhất. Hàm lỗi CTC được sử dụng thay cho giải thuật Hidden Markov Model (HMM), và được cho là hiệu quả hơn HMM hoặc HMM kết hợp học sâu.

Phương pháp này có tính tổng quát tương đối cao và có thể áp dụng cho các văn bản ngoại cảnh, bản nhạc và các tập dữ liệu khác. Nó chỉ sử dụng tập dữ liệu sinh tự động để huấn luyện nhưng vẫn đạt được kết quả tốt trên các tập dữ liệu thực khác. Tuy nhiên, nhược điểm của phương pháp này là chỉ có thể nhận dạng được chuỗi dữ liệu trên cùng một hàng.

![The-architecture-of-a-convolutional-recurrent-neural-network-is-composed-of-three](https://user-images.githubusercontent.com/13607004/233864826-a9ea8983-e7f7-43a9-b9d3-250c58df1c4a.png)

<i> Mạng CRNN <i>
            
## 2.3 Mô hình kết hợp phát hiện và nhận diện biển số xe
### 2.3.1. Hướng tuần tự
Hướng tuần tự là một phương pháp trong việc xử lý ảnh mà có sự tách biệt giữa quá trình phát hiện và quá trình nhận diện. Trong đó quá trình phát hiện và quá trình nhận diện được thực hiện riêng biệt, nhưng có thể có sự tương tác giữa chúng.
Phương pháp của Masood và đồng sự [17]:
Phương pháp này sử dụng 3 mạng neural convolutional (CNN) để thực hiện quá trình phát hiện và nhận dạng biển số xe. Mạng đầu tiên được sử dụng để phát hiện và phân loại biển số xe, mạng thứ hai được sử dụng để phát hiện các ký tự trên biển số, và mạng cuối cùng được sử dụng để nhận dạng các ký tự đó. Phương pháp này đã đạt được độ chính xác khá cao trên các tập dữ liệu biển số xe của Mỹ và châu Âu, lần lượt là 93,44% và 94,55%. Tuy nhiên, mô hình mà phương pháp này đề xuất khá lớn với 3 mạng neural tách biệt, dẫn đến thời gian huấn luyện sẽ tốn nhiều thời gian.
            
Phương pháp của Li Hui và đồng sự [18]:
Phương pháp này áp dụng một mạng phân loại CNN để tạo ra bản đồ xác suất của các pixel có khả năng là ký tự trong biển số xe. Bản đồ xác suất này sau đó được gom nhóm lại bằng giải thuật Non-Maxima Suppression (NMS) và Run-Length Smoothing Algorithm (RLSA) để tạo ra các nhóm pixel liên quan đến các ký tự trong biển số xe. Từ các nhóm pixel này, đường bao của biển số xe được tạo ra thông qua giải thuật phân tích các thành phần liên kết (CCA). Sau đó, vùng biển số được trích xuất từ các nhóm pixel này và đưa qua mô hình tương tự như phương pháp [1] để nhận diện chuỗi biển số xe.
Ưu điểm của phương pháp này là đạt được độ chính xác khá cao so với các phương pháp trước đó với tỷ lệ 97.56%. Tuy nhiên, bước trích xuất biển số xe vẫn phải được thực hiện bằng cách thủ công, do đó có thể dẫn đến sai sót và ảnh hưởng đến độ chính xác của bước nhận dạng phía sau.
            
### 2.3.2 Hướng tích hợp
Hướng tích hợp là hướng tiếp cận trong xử lý ảnh mà việc phát hiện và nhận diện đối tượng được kết hợp lại để cùng hoạt động trên cùng một mạng. Trong hướng này, thông tin giữa quá trình phát hiện và nhận diện được chia sẻ thông qua bộ phân loại trung gian, giúp cải thiện độ chính xác và tốc độ xử lý.

Một số phương pháp tích hợp sử dụng bước tiền xử lý để xác định vùng quan tâm (ROI - Region of Interest) trước khi thực hiện phát hiện và nhận diện. Quá trình này giúp tập trung phân tích vào vùng quan tâm để tăng tốc độ xử lý và giảm độ phức tạp của mô hình. Tuy nhiên, việc xác định ROI đòi hỏi kiến thức chuyên môn và kinh nghiệm để đảm bảo độ chính xác và tránh sai sót trong quá trình xử lý.
            
Phương pháp của Li Hui và đồng sự [5]:
Phương pháp này sử dụng kiến trúc mạng duy nhất bao gồm các phần: lớp mạng trích xuất đặc trưng cấp thấp, tạo vùng chứa biển số, xử lý vùng chứa biển số, phát hiện và nhận dạng biển số xe. Phương pháp này lấy ý tưởng kết hợp các mạng có sẵn thành một mạng duy nhất để giảm thiểu các bước trung gian, đặc biệt là bước phân đoạn ký tự. Nó hoạt động tốt trong các điều kiện tự nhiên như ban ngày, ban đêm, mưa và nắng.

Tuy nhiên, quá trình nhận dạng ký tự chỉ hoạt động với chuỗi ký tự trên một hàng. Chiến thuật huấn luyện tương đối phức tạp và yêu cầu một lượng lớn dữ liệu. Do đó, phương pháp này đòi hỏi sự đầu tư nghiêm túc và chú ý đến các thách thức về tính toàn vẹn và độ chính xác của dữ liệu.

<img width="801" alt="Screenshot 2023-04-24 at 03 51 09" src="https://user-images.githubusercontent.com/13607004/233865626-c10dc87a-21f5-40ba-a4ed-b276158442ae.png">
            
<i> Kiến trúc tổng quan của mô hình [5] </i>            
         
            
            
            
            
            
            
            
            
            
