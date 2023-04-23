
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
Ảnh trong thực tế là một ảnh liên tục về không gian và giá trị độ sáng. Dể có thể xử lý ảnh bằng máy tính cần thiết phải số hóa ảnh. Trong quá trình số hóa, người ta biến đổi tín hiệu liên tục sang tín hiệu rời rạc thông qua quá trình lấy mẫu (rời rạc hóa về không gian) và lượng hóa thành phần giá trị. Trong quá trình này người ta sử dụng khái niệm Pixel để biểu diễn các phần tử của bức ảnh. Ở đây cũng cần phân biệt khái niệm pixel hay đề cập đến trong các hệ thống đồ họa máy tính. Để tránh nhầm lẫn ta tạm thời gọi khái niệm pixel này là pixel thiết bị.

Khái niệm pixel thiết bị có thể xem xét như sau: Khi ta quan sát màn hình (trong chế độ đồ họa), màn hình không liên tục mà gồm nhiều điểm nhỏ, gọi là pixel. Mỗi pixel bao gồm một cặp tọa độ x,y và màu. Cặp tọa đọ x, y tạo nên độ phân giải (resolution). Như màn hình máy tính có nhiều độ phân giải khác nhau, hiện tại phổ biến là màn hình HD (High Definition) có độ phân giải là 1280 x 720 pixels hay màn hình Full HD (Full High Definition) có độ phân giải là 1920 x 1080.

![so-sanh-do-phan-giai-hd-va-full-hd-2](https://user-images.githubusercontent.com/13607004/233827520-f0cf4a59-c037-4cc7-b574-225dd6b2a693.jpg)
<i> Hình ảnh thể hiện một điểm ảnh </i>


