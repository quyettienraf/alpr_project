# draft_report
# Đề tài: Nghiên cứu đánh giá tối ưu phương pháp nhận dạng biển số xe tự động trên hệ thống nhúng
## Mã đề tài: 2021KHDL-E12

# Yêu cầu
- sơ đồ khối mô tả tổng quan
- [x]  bước 1: xác định vùng biển số boudingbox
- [x]  bước 2: nhận dạng vùng kí tự trong biển số
- [x]  bước 3: nhận dạng kí tự trong vùng kí tự
- lựa chọn thuật toán ở mỗi bước
- implement trên thiết bị raspberry pi
- Tối ưu, cải tiến thuật toán
- yêu cầu chi tiết của thuật toán
- deeplearning CNN: yolo, mobinet, resnet
- dùng yolo với dataset của bài báo khác
- cân nhắc dựa trên độ chính xác và tối ưu độ tính toán
- so sánh các phương pháp với nhau hoặc so sánh cái mình làm với cả những cái ngta làm
- Cải tiên thuật toán nhận dạng tình huống khó trong dataset
- bài toán nhiều biển số trong 1 ảnh
- tạo ra 1 dataset đã được làm giàu
- thêm 1 chương về cài đặt thử nghiệm
- làm thêm giao diện website
- bổ sung thêm các bài báo
- liệt kê các thuật toán nhận dạng theo xử lý ảnh truyền thống và dùng deeplearning
- so sánh cùng ngữ cảnh các phương pháp

# Mục lục
- Chương 1: Tổng quan về nhận dạng
- Chương 2: Xử lý ảnh và OpenCV
- Chương 3: Tổng quan về hệ thống nhúng
- Chương 4: Bài toán nhận dạng biển số xe
- Chương 5: Kết quả và hướng phát triển
- Kết luận
- Tài liệu tham khảo
- Phụ lục
- Danh mục các hình vẽ
- Danh mục các bảng

# Mở đầu
Ô tô và xe máy là phương tiện giao thông không thể thiếu trong đời sống hiện đại, tuy nhiên, việc quản lý xe cộ vẫn là một thách thức đối với chính quyền và cơ quan chức năng. Trong đó, việc nhận dạng biển số xe tự động đang trở thành một công nghệ được sử dụng phổ biến nhằm giúp quản lý xe cộ dễ dàng hơn.

Nhận dạng biển số xe tự động (ALPR - Automatic License Plate Recognition) là một công nghệ đang được phát triển mạnh mẽ và được sử dụng rộng rãi trên toàn cầu. Tuy nhiên, hiệu suất của công nghệ này phụ thuộc rất nhiều vào phương pháp và thuật toán nhận dạng biển số. Trong quá trình phát triển công nghệ, cần phải tìm ra phương pháp và thuật toán tối ưu để đảm bảo độ chính xác và hiệu quả của hệ thống.

Tuy nhiên, công nghệ nhận dạng biển số xe tự động vẫn còn nhiều hạn chế và thách thức, đặc biệt là trong môi trường khắc nghiệt như ánh sáng yếu, mưa bão, địa hình phức tạp,...

Hiện nay, có rất nhiều phương pháp nhận dạng biển số xe tự động được đưa ra, tuy nhiên, độ chính xác và tốc độ xử lý của các phương pháp này vẫn còn khá thấp. Vì vậy, để đáp ứng yêu cầu ngày càng cao của các ứng dụng thực tế, nghiên cứu và phát triển các phương pháp nhận dạng biển số xe tự động hiệu quả và tối ưu là điều cần thiết.

Trong báo cáo này, tôi tập trung vào việc đánh giá và cải thiện phương pháp nhận dạng biển số xe tự động trên hệ thống nhúng. Bằng việc kết hợp các kỹ thuật xử lý ảnh, đã tạo ra một hệ thống nhận dạng biển số xe tự động có độ chính xác cao và tốc độ xử lý nhanh hơn so với các phương pháp khác. Báo cáo này sẽ đưa ra các kết quả thực nghiệm và đánh giá hiệu quả của phương pháp được đề xuất.

Hy vọng rằng nghiên cứu này sẽ cung cấp một đóng góp quan trọng trong việc phát triển các phương pháp nhận dạng biển số xe tự động hiệu quả và tối ưu hơn trong tương lai, từ đó giúp cho việc ứng dụng công nghệ xử lý ảnh vào các lĩnh vực như an ninh giao thông, giám sát bãi đỗ xe, quản lý đỗ xe trở nên dễ dàng và chính xác hơn.
