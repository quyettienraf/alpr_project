
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
Ảnh màu là một loại ảnh chứa thông tin về màu sắc của mỗi phần tử trong ảnh. Thông thường, giá trị màu được biểu diễn dựa trên các không gian màu (color space), trong đó không gian màu RGB (Red-Green-Blue) là một trong những không gian màu thường được sử dụng. Trong không gian màu RGB, mỗi pixel được biểu diễn bằng ba giá trị màu đỏ, xanh lá cây và xanh da trời. Số bit được sử dụng để lưu trữ màu ảnh phụ thuộc vào số lượng màu sắc khác nhau cần lưu trữ, ví dụ như 8 bit, 16 bit, hoặc 24 bit (True Color). Nếu ta sử dụng số bit nhỏ hơn 24 bit để lưu trữ màu, ta sẽ phải sử dụng bảng Palette màu, tương tự như một bảng Lookup Table. Bảng Palette màu cho phép ánh xạ giữa một vị trí trong bảng với một tổ hợp màu sắc của không gian màu RGB. Ví dụ, nếu ta sử dụng 8 bit tương ứng với 256 màu sắc khác nhau, ta phải có bảng ánh xạ 256 màu sắc đó tương ứng với 256 tổ hợp Red-Green-Blue.

![The_three_primary_colors_of_RGB_Color_Model_(Red,_Green,_Blue)](https://user-images.githubusercontent.com/13607004/233828067-cc5fee54-5f5e-4411-ab34-f898cedb6990.png)

<i> Ảnh màu RGB</i>

<b> c, Ảnh xám </b>
Ảnh xám (Gray image) là loại ảnh chỉ bao gồm các mức độ xám khác nhau, mỗi điểm ảnh của ảnh xám chỉ chứa thông tin về mức độ sáng tại vị trí đó. Khác với ảnh màu, ảnh xám không có thông tin về màu sắc, chỉ có thông tin về độ sáng. Trong đó, mỗi điểm ảnh được biểu diễn bằng một giá trị số, thường là giá trị từ 0 đến 255, tương ứng với các mức xám từ đen tuyền đến trắng tuyền. Mỗi giá trị số đại diện cho một mức xám khác nhau, với giá trị 0 thường được dùng để biểu diễn màu đen, và giá trị 255 được dùng để biểu diễn màu trắng.
<img width="415" alt="Screenshot 2023-04-23 at 17 11 50" src="https://user-images.githubusercontent.com/13607004/233833696-e8ee6020-d809-4ded-b39f-1388d90738a8.png">

<i> Ảnh được chuyển sang ảnh xám </i>

<b> d, Ảnh nhị phân </b>
Ảnh nhị phân là loại ảnh chỉ bao gồm hai mức xám khác nhau, thường là màu đen và màu trắng. Mỗi điểm ảnh trong bức ảnh nhị phân chỉ có thể có giá trị là 0 hoặc 1, tương ứng với màu đen và màu trắng. Loại ảnh này được sử dụng rất phổ biến trong các ứng dụng xử lý ảnh, như trong nhận dạng ký tự, xử lý ảnh y tế, hoặc xử lý ảnh vệ tinh. Sử dụng ảnh nhị phân giúp giảm thiểu dữ liệu và tăng tốc độ xử lý ảnh, đồng thời cũng giúp đơn giản hóa quá trình xử lý ảnh so với các loại ảnh có nhiều mức xám khác nhau.
![FlZlGsM](https://user-images.githubusercontent.com/13607004/233833958-9d7c58c2-658a-4722-924f-e8a45bddcbfe.png)

<i> so sánh ảnh màu, ảnh xám và ảnh nhị phân </i>

<b> e, Lược đồ mức xám </b>

Lược đồ mức xám (gray level histogram) là một biểu đồ thống kê tần suất xuất hiện của các mức xám trong một bức ảnh. Nó thể hiện số lần xuất hiện của từng mức xám khác nhau trong ảnh, bao gồm cả số lượng pixel có mức xám tối thiểu và mức xám tối đa.

Lược đồ mức xám được sử dụng rộng rãi trong xử lý ảnh và phân tích hình ảnh. Nó có thể cung cấp thông tin quan trọng về phân bố mức xám trong ảnh, giúp đánh giá chất lượng ảnh, phát hiện và phân tích các đối tượng trong ảnh, thực hiện các phép biến đổi ảnh như cân bằng màu sắc và tăng cường độ tương phản, hay chuyển đổi ảnh từ mức xám sang ảnh màu.

Ví dụ, một ảnh đa mức xám sử dụng 8 bit, có 256 mức xám từ 0 tới 255. Lược đồ mức xám sẽ có trục hoành chạy từ 0 đến 255 và trục tung chính là tổng số điểm ảnh có mức xám tương ứng.

![mage-Histogram-diagram-for-a-digital-gray-scale-image-named-Lena](https://user-images.githubusercontent.com/13607004/233834274-29ea3ea2-ac65-4d25-a2e5-2f02d2777052.png)

<i> Lược đồ mức xám của ảnh xám tương ứng </i> 
