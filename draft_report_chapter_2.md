
# Chương II: Tổng quan về hệ thống xử lý ảnh
## 2.1. Tổng quan về xử lý ảnh
Kỹ thuật xử lý ảnh hiện nay đã được ứng dụng rộng rãi trong nhiều lĩnh vực, đó là một công nghệ đóng vai trò quan trọng trong sản xuất cũng như đời sống. Ví dụ như trong lĩnh vực vệ tinh, hệ thống xử lý ảnh được sử dụng để phân tích không gian vũ trụ, địa chất, hay trong lĩnh vực y tế, các hệ thống xử lý ảnh được sử dụng để phân tích tế bào sinh học. Đồng thời, các phần mềm hiển thị và xử lý ảnh chuyên dụng như Photoshop hay những ứng dụng trên smartphone như Camera360, các bộ lọc hình ảnh tích hợp sẵn trên các nền tảng mạng xã hội như Facebook, Instagram, Tik Tok, cũng là một trong những ứng dụng phổ biến của kỹ thuật xử lý ảnh hiện nay.

Một hệ thống xử lý ảnh cơ bản bao gồm các chức năng như thu thập và tiền xử lý dữ liệu đầu vào, thực hiện các phép xử lý như lọc, biến đổi, phân tích và đưa ra kết quả cuối cùng. Các hệ thống xử lý ảnh còn được sử dụng để nhận dạng, phân loại và đưa ra quyết định trên thực tế. Trong phạm vi đồ án, tác giả giới hạn trong việc giới thiệu một hệ thống xử lý ảnh ứng dụng nhận dạng và ra quyết định trên thực tế, đó là hệ thống nhận dạng biển số xe.

<img width="526" alt="Screenshot 2023-04-23 at 14 33 32" src="https://user-images.githubusercontent.com/13607004/233826376-3613f5eb-3b4c-4ae3-aa22-9df1a85560dc.png">

<i>Sơ đồ tổng quát một hệ thống xử lý ảnh</i>

Hệ thống xử lý ảnh được giới thiệu trong đồ án bao gồm 3 khối chức năng cơ bản: khối thu nhận ảnh, khối phân tích ảnh và khối nhận dạng. 
- Khối thu nhận ảnh có nhiệm vụ thu nhận ảnh và thực hiện quá trình số hóa để lưu trữ theo định dạng yêu cầu. 
- Khối phân tích ảnh đầu tiên tiến hành bước tiền xử lý ảnh để tăng cường, cải thiện chất lượng ảnh và làm nổi các đặc trưng cơ bản của ảnh hay làm cho ảnh gần giống nhất với trạng thái gốc. Sau đó, thực hiện quá trình phân tích ảnh và trích chọn đặc trưng của ảnh, ví dụ như biên, điểm gấp khúc, điểm kết thúc, điểm chữ thập,... 
- Khối nhận dạng dựa vào các đặc trưng đã thu nhận từ khối phân tích ảnh để thực hiện quá trình nhận dạng và đưa ra các quyết định ứng với các ứng dụng cụ thể. 

### 2.1.1. Một số khái niệm và các vấn đề cơ bản trong xử lý ảnh
#### 2.1.1.1. Một số khái niệm cơ bản: 
<b> a, Phần tử ảnh (Pixel - Picture Element)</b>
Trong thực tế, ảnh là một tín hiệu liên tục về không gian và giá trị độ sáng, để có thể xử lý ảnh bằng máy tính, ta cần số hóa ảnh thông qua quá trình lấy mẫu và lượng hóa thành phần giá trị. Trong quá trình này, ta sử dụng khái niệm Pixel để biểu diễn các phần tử của bức ảnh. Tuy nhiên, để tránh nhầm lẫn, ta cần phân biệt khái niệm pixel trong thực tế và pixel trong các hệ thống đồ họa máy tính.

Khái niệm pixel trong đồ họa máy tính được hiểu như sau: khi ta quan sát màn hình trong chế độ đồ họa, màn hình không hiển thị ảnh liên tục mà được tạo thành bởi nhiều điểm nhỏ gọi là pixel. Mỗi pixel chứa một cặp tọa độ x và y cùng với thông tin về màu sắc. Cặp tọa độ x, y tạo nên độ phân giải của màn hình. Hiện nay, màn hình máy tính có nhiều độ phân giải khác nhau, phổ biến nhất là màn hình HD (High Definition) có độ phân giải 1280 x 720 pixel và màn hình Full HD (Full High Definition) có độ phân giải 1920 x 1080 pixel.

![so-sanh-do-phan-giai-hd-va-full-hd-2](https://user-images.githubusercontent.com/13607004/233827520-f0cf4a59-c037-4cc7-b574-225dd6b2a693.jpg)

<i> Hình ảnh thể hiện một điểm ảnh </i>

<b> b, Ảnh màu (Color image) </b>
Ảnh màu chứa thông tin màu cho mỗi phần tử của ảnh. Thông thường giá trị màu này dựa trên các không gian màu (color space) trong đó không gian màu thường được sử dụng là RGB tương ứng với 3 kênh màu đỏ (Red) - xanh lá cây (Green) -  xanh da trời (Blue). Tùy thuộc vào số bit được sử dụng để lưu trữ màu ta có số lượng màu khác nhau, ví dụ 8 bit, 16 bit, 24 bit (True Color). Nếu ta sử dụng nhỏ hơn 24 bit để lưu trữ màu thì ta phải so 1 bảng Palette màu, nó tương tự như một bảng Lookup Table cho phép ánh xạ giữa một vị trí trong bảng với một tổ hợp của không gian màu RGB. Ví dụ như sử dụng 8 bit tương ứng với 256 màu thì ta phải có bảng ánh xạ 256 màu đó tương ứng với 256 tổ hợp Red - Green - Blue.

![The_three_primary_colors_of_RGB_Color_Model_(Red,_Green,_Blue)](https://user-images.githubusercontent.com/13607004/233828067-cc5fee54-5f5e-4411-ab34-f898cedb6990.png)

<i> Ảnh màu RGB</i>




