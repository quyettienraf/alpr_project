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

Công nghệ nhận dạng biển số xe tự động vẫn còn nhiều hạn chế và thách thức, đặc biệt là trong môi trường khắc nghiệt như ánh sáng yếu, mưa bão, địa hình phức tạp,...

Hiện nay, có rất nhiều phương pháp nhận dạng biển số xe tự động được đưa ra, tuy nhiên, độ chính xác và tốc độ xử lý của các phương pháp này vẫn còn khá thấp. Vì vậy, để đáp ứng yêu cầu ngày càng cao của các ứng dụng thực tế, nghiên cứu và phát triển các phương pháp nhận dạng biển số xe tự động hiệu quả và tối ưu là điều cần thiết.

Nghiên cứu này tập trung vào việc đánh giá và cải thiện phương pháp nhận dạng biển số xe tự động trên hệ thống nhúng. Bằng việc kết hợp các kỹ thuật xử lý ảnh, mục tiêu là tạo ra một hệ thống nhận dạng biển số xe tự động có độ chính xác cao và tốc độ xử lý nhanh hơn so với các phương pháp khác. Nghiên cứu này sẽ đưa ra các kết quả thực nghiệm và đánh giá hiệu quả của phương pháp được đề xuất.

Hy vọng rằng nghiên cứu này sẽ cung cấp một đóng góp quan trọng trong việc phát triển các phương pháp nhận dạng biển số xe tự động hiệu quả và tối ưu hơn trong tương lai, từ đó giúp cho việc ứng dụng công nghệ xử lý ảnh vào các lĩnh vực như an ninh giao thông, giám sát, quản lý bãi đỗ xe trở nên dễ dàng và chính xác hơn.

# Chương 1: Giới thiệu đề tài
Lĩnh vực xử lý ảnh số, bao gồm xử lý, phân tích và nhận biết tự động bằng máy tính, đã và đang có sự phát triển mạnh mẽ trong cả lý thuyết và các ứng dụng thực tế. Xử lý ảnh được ứng dụng trong nhiều lĩnh vực quan trọng như: viễn thông, truyền thông, chụp ảnh y tế, sinh học, khoa học vật liệu, robot, sản xuất, các hệ thống cảm biến thông minh, tự động điều khiển, đồ họa, in ấn, ... Sự phát triển mạnh mẽ này có thể được thấy rõ qua số lượng các bài báo, báo cáo khoa học về xử lý ảnh hàng năm cũng như số lượng các đầu sách viết về xử lý ảnh số.

Như chúng ta đã biết, ngày nay xe máy và ô tô là phương tiện giao thông chính và số lượng ngày càng tăng. Vì vậy vấn đề quản lý giao thông, đảm bảo an ninh, thu phí gioa thông, trông bãi giữ xe,... đòi hỏi và cần thiết có sự hỗ trợ của khoa học kĩ thuật. Một trong những sự hỗ trợ đầy hiệu quả đó là làm sao giúp những ngừoi quản lý nhận dạng biển số xe một cách dễ dàng, nhanh chóng và thuận lợi nhất.

Nhận dạng biển số xe trở thành một ứng dụng hữu ích, được đưa vào trong những lĩnh vực như: quản lý giao thông, kiểm tra an ninh, thu phí giao thông, trạm gác cổng, quản lý các bãi giữ xe một cách tự động, ... Nó không chỉ giúp những người quản lý có khả năng bao quát được tất cả khách hàng, đối tượng cần theo dõi của mình mà còn giúp tiết kiệm thời gian làm việc đáng kể. Ngoài ra với phương pháp này sẽ giúp giảm được nhiều người trông giữ xe để phân công họ vào việc khác.

Trong lĩnh vực nhận dạng biển số xe, hệ thống nhúng đang được ưu tiên lựa chọn vì tính đơn giản, hiệu quả và tiết kiệm chi phí. Hệ thống nhúng được thiết kế để chạy các tác vụ như tính toán, điều khiển, với đặc tính tiêu thụ điện năng thấp và kích thước nhỏ gọn. Do đó, việc sử dụng hệ thống nhúng trong ứng dụng nhận dạng biển số xe tự động có thể giúp tối ưu hóa quá trình xử lý và giảm thiểu tài nguyên phần cứng cần thiết, đồng thời tăng tốc độ xử lý và cải thiện độ chính xác của hệ thống.

Từ những lý do trên, em quyết định lựa chọn đề tài "Nghiên cứu đánh giá tối ưu phương pháp nhận dạng biển số xe tự động trên hệ thống nhúng". Việc nghiên cứu này sẽ đóng góp tích cực vào việc giải quyết các vấn đề liên quan đến quản lý giao thông và đảm bảo an ninh giao thông, đồng thời là một ứng dụng tiềm năng của công nghệ nhúng trong lĩnh vực xử lý ảnh số.





