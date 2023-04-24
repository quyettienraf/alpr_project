# CHƯƠNG 4: MÔ HÌNH ĐỀ XUẤT

## 4.1 Tổng quan

## 4.2 Phát hiện biển số xe

## 4.3 Trích xuất vùng biển số xe

## 4.4 Nhận dạng biển số xe

# CHƯƠNG 5: THÍ NGHIỆM

## 5.1 Tiêu chí đánh giá

## 5.2 Chuẩn bị dữ liệu

Các tập dữ liệu biển số xe không phổ biến và có nguồn gốc từ các quốc gia khác nhau. Những tập dữ liệu tiêu biểu bao gồm CCPD [2], UFPR-ALPR [24], AOLP [25] và PKUData [26]. Tuy nhiên, các tập dữ liệu này không phù hợp cho việc sử dụng ở Việt Nam do khác biệt về kích thước và bố trí.

Do đó, tập dữ liệu chính được sử dụng cho đề tài sẽ được thu thập từ thực tế và sinh tự động. Việc thu thập dữ liệu từ thực tế sẽ được thực hiện trong những điều kiện khác nhau, bao gồm góc độ của camera, điều kiện chiếu sáng, độ phân giải của camera, vv. Tập dữ liệu sẽ được chia thành hai phần riêng biệt, bao gồm tập huấn luyện và tập kiểm thử.

Tập huấn luyện được sử dụng để tối ưu hệ thống nhận diện bằng cách điều chỉnh các thông số phù hợp. Trong khi đó, tập kiểm thử được sử dụng để đánh giá kết quả của phương pháp nhận diện sau khi đã được huấn luyện. Cả hai tập dữ liệu đều sẽ được gán nhãn với vùng có biển số xe xuất hiện và các ký tự trong các biển số đó để phục vụ cho việc nhận diện.

## 5.2.1 Quy định về biển số xe Việt Nam

- Biển số xe ô tô:
- Biển số xe máy:

## 5.2.2 Xây dựng tập biển số từ dữ liệu thực tế

Một số thông tin về tập dữ liệu:
- Tổng số lượng ảnh là
- Số lượng biển số xe
- Tổng số lượng các ký tự
- Biển số xe bao gồm các ký tự sau: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, G, H, K, L, M, N, P, R, S, T, U, V, X, Y, Z

Sau khi thu thập tập dữ liệu, chúng tôi sẽ gán nhãn thông tin về vị trí và chuỗi ký tự của biển số. Vị trí của biển số sẽ được xác định bằng cách ghi nhận tọa độ của bốn góc của biển số. Khi huấn luyện mô hình phát hiện, chúng tôi sẽ chuyển đổi bốn góc này thành một đường bao chữ nhật lớn nhất để bao phủ vùng biển số. Trong quá trình đánh nhãn vị trí, chúng tôi sẽ đánh dấu các đường bao sao cho vẫn có thể nhìn thấy được cạnh của biển số. Điều này giúp mô hình hạn chế sai sót phân loại giữa biển số và các đối tượng khác có chứa chuỗi ký tự tương tự.

Chuỗi ký tự của biển số chỉ bao gồm các chữ cái và số. Các ký tự khác như dấu gạch ngang "-" và dấu chấm "." sẽ được bỏ qua trong quá trình đánh nhãn. Để phân biệt giữa biển số ngắn và biển số dài, chúng tôi sẽ thêm dấu gạch dưới "_" vào chuỗi ký tự cho biển số ngắn. Bằng cách này, chúng tôi có thể xác định và phân loại các biển số ngắn và dài một cách chính xác. 

## 5.2.3 Sinh tập biển số
Trong quá trình huấn luyện mạng học sâu, việc có đủ dữ liệu để huấn luyện mạng đóng vai trò quan trọng để đạt được độ chính xác cao. Tuy nhiên, việc thu thập và gán nhãn cho số lượng lớn dữ liệu là một công việc khó khăn và tốn nhiều thời gian. Do đó, việc tạo dữ liệu tự động để bổ sung cho dữ liệu huấn luyện là cần thiết. Tuy nhiên, dữ liệu được tạo ra tự động cần phải có tính đa dạng và tương tự như dữ liệu thực để giúp mạng học sâu có khả năng tổng quát hóa cao.

Quy trình tạo dữ liệu tự động bao gồm các bước sau:

- Bước 1: Thu thập ảnh nền mẫu từ thực tế cũng như từ các tập dữ liệu công khai trên Internet. Ảnh nền mẫu được sử dụng để tạo ra các bức ảnh mới với các biến đổi khác nhau.
- Bước 2: Tạo ra biển số xe bằng cách tạo phần biển số đơn giản bao gồm nền trắng và viền bao. Chuỗi ký tự được sinh ngẫu nhiên với font chữ có sẵn và theo định dạng đã được quy định ở trên sau đó được chèn vào phần biển số. Việc tạo ra các biển số xe ngẫu nhiên giúp tăng tính đa dạng của dữ liệu huấn luyện.
- Bước 3: Điều chỉnh độ sáng tối, độ mờ và thêm nhiễu cho các biển số xe để tạo ra các ảnh mới với tính đa dạng cao hơn. Việc điều chỉnh các tham số này giúp giảm sự trùng lắp và giảm thiểu overfitting.
- Bước 4: Áp dụng phép biến đổi phối cảnh để gắn các biển số xe vào ảnh nền mẫu. Việc tạo ra các ảnh mới với các phối cảnh khác nhau giúp tăng tính đa dạng của dữ liệu huấn luyện.

## 5.2.4 Làm giàu dữ liệu

Trong quá trình huấn luyện mạng học sâu, dữ liệu chính là yếu tố quan trọng ảnh hưởng đến hiệu quả của mạng. Tuy nhiên, việc thu thập và gán nhãn cho một lượng lớn dữ liệu khá khó khăn và tốn nhiều thời gian và công sức. Do đó, việc tạo ra dữ liệu tự động để bổ sung cho dữ liệu huấn luyện là cần thiết.

Quy trình để sinh dữ liệu tự động bao gồm nhiều bước. Đầu tiên, ta thu thập các ảnh nền mẫu từ thực tế và từ các tập dữ liệu công khai trên Internet. Sau đó, ta tạo ra phần biển số đơn giản bao gồm nền trắng và viền bao, và sinh ngẫu nhiên chuỗi ký tự với font chữ có sẵn và theo định dạng đã được quy định. Tiếp theo, ta điều chỉnh độ sáng tối, độ mờ và thêm nhiễu cho phần biển số.

Để làm giàu dữ liệu, ta sử dụng các phép biến đổi màu sắc và hình học. Các phép biến đổi chủ yếu bao gồm: biến đổi màu ngẫu nhiên, biến đổi ảnh xám ngẫu nhiên, phép biến đổi xoay và phối cảnh, cắt ảnh ngẫu nhiên, thêm nhiễu và mờ, và chuẩn hóa ảnh. Dữ liệu để huấn luyện sẽ được qua đầy đủ các phép biến đổi này. Trong khi đó, tập đánh giá và kiểm thử ảnh chỉ được chuẩn hóa.

Các phép biến đổi đều có xác suất xảy ra lớn hơn 0.5. Tuy nhiên, một số phép biến đổi như thêm nhiễu và làm có xác suất thấp hơn trong khoảng 0.1. Với phép biến đổi hình học, góc xoay không quá 30 độ và ta cần đảm bảo rằng phần biển số không bị mất hoặc bị che khuất trong quá trình biến đổi.

