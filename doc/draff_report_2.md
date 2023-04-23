# CHƯƠNG 2: CÁC CÔNG TRÌNH LIÊN QUAN
Bài toán nhận dạng biển số xe là một trong những bài toán quan trọng trong lĩnh vực nhận diện văn bản ngoại cảnh. Vì vậy, các nghiên cứu liên quan đến hai bài toán này thường có sự tương quan mật thiết. Trong những năm gần đây, bài toán nhận diện biển số xe đã được quan tâm nhiều và có sự phát triển đáng kể. Thông thường, bài toán nhận dạng biển số xe bao gồm một số bước cơ bản như sau:

![Untitled](https://user-images.githubusercontent.com/13607004/233845181-e2a76ae9-1727-4aca-b81d-e0c664c1c911.png)

<i> Các bước cơ bản của một hệ thống nhận diện biển số xe </i>

Từ những bước trên, có ba bài toán chính cần được giải quyết trong việc nhận dạng biển số xe: phát hiện vị trí của biển số trên hình, phân đoạn các ký tự trong biển số và nhận diện chuỗi ký tự trên biển số. Dựa trên những nghiên cứu mới đây, đề tài nhận thấy rằng hướng tiếp cận nhận dạng chuỗi ký tự trên biển số mà không phải qua bước phân đoạn ký tự rất tiềm năng, vì có nhiều ưu điểm hơn. Do đó, đề tài tập trung vào khảo sát các công trình liên quan đến phát hiện vị trí của biển số và nhận diện ký tự trên biển số. Ngoài ra, trong số các nghiên cứu gần đây còn đề cập đến việc kết hợp xử lý cả hai quá trình phát hiện và nhận dạng một cách đồng thời, tạo ra một phương pháp tổng thể hiệu quả hơn để giải quyết bài toán này.

## 2.1 Phát hiện bảng số xe
### 2.1.1 Các phương pháp trích xuất đặc trưng thủ công
Trong quá khứ, các phương pháp trích đặc trưng thủ công được sử dụng phổ biến trong việc phân tích ảnh. Những đặc trưng thường được sử dụng bao gồm các đặc trưng cơ bản như góc, cạnh, vân ảnh, màu sắc và mức sáng. Các phương pháp phổ biến để trích xuất các đặc trưng này bao gồm việc nhị phân hóa ảnh, sử dụng thuật toán SIFT, HOG, phân tích thành phần liên thông và hình thái học. Sau đó, các đặc trưng này được đưa qua các bộ phân loại như AdaBoost, SVM để phân loại.

Các phương pháp trích xuất đặc trưng cơ bản thường đơn giản, dễ hiện thực và nhanh chóng, đặc biệt là khi kết hợp nhiều đặc trưng với nhau, kết quả có thể đạt được độ chính xác tương đối cao. Tuy nhiên, các phương pháp này có nhược điểm là khá nhạy cảm với sự thay đổi mức sáng, nhiễu và mờ. Hơn nữa, việc thiết kế bộ rút trích đặc trưng còn phụ thuộc khá nhiều vào tập dữ liệu, do đó cần phải đảm bảo tập dữ liệu đủ đa dạng để đảm bảo tính chính xác của phương pháp trích xuất.


            
            
            
            
            
            
            
