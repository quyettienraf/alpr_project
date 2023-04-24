# Đề tài: Nghiên cứu đánh giá tối ưu phương pháp nhận dạng biển số xe tự động trên hệ thống nhúng
## Mã đề tài: 2021KHDL-E12

# CHƯƠNG 1: GIỚI THIỆU
## 1.1 Giới thiệu đề tài

Với sự phát triển nhanh chóng của kinh tế và xã hội, nước ta đang đối mặt với nhiều thách thức phức tạp, trong đó tình trạng giao thông quá tải và hỗn loạn đang là vấn đề nghiêm trọng tại các trung tâm kinh tế lớn của cả nước. Những tác động tiêu cực của vấn đề này đang gây ra những thiệt hại lớn cho nền kinh tế cũng như đời sống xã hội. Để giải quyết vấn đề này, cần có sự nâng cao ý thức và chấp hành giao thông của người dân, đồng thời cần thiết phải tập trung vào việc giám sát và quản lý giao thông.

Tuy nhiên, việc giám sát và quản lý giao thông hiện nay vẫn chủ yếu dựa trên phương pháp thủ công, trong khi số lượng phương tiện giao thông ngày càng tăng đòi hỏi cần có các giải pháp tự động hơn để giảm thiểu sức lao động của con người. Điều này đã được áp dụng từ lâu ở những nước phát triển và hiện nay, với yêu cầu đưa công nghệ vào cuộc sống và sản xuất, việc giải quyết bài toán giám sát giao thông tự động trở nên cực kỳ cấp bách.

Trong đó, bài toán nhận diện biển số xe là một trong những bài toán quan trọng để giúp quản lý phương tiện giao thông một cách hiệu quả. Tuy nhiên, để giải quyết bài toán này cần phải áp dụng các công nghệ mới như trí tuệ nhân tạo, học sâu, xử lý ảnh, và có những phương pháp đánh giá và xử lý dữ liệu để đạt được độ chính xác cao. Vì vậy, việc nghiên cứu và giải quyết bài toán này là cực kỳ cần thiết để đóng góp vào giải quyết vấn đề giao thông chung hiện nay.
  
Vấn đề phát hiện và nhận diện biển số xe là một trong những hướng nghiên cứu đã được quan tâm trong lĩnh vực thị giác máy tính từ lâu. Tuy nhiên, hiện nay với sự phát triển mạnh mẽ của phương pháp học sâu (deep learning), đã mở ra một hướng tiếp cận mới cho vấn đề này. Các mạng nơ-ron trong học sâu như Convolution Neural Networks (CNN), Recurrent Neural Networks (RNN) cùng với các kiến trúc mạng như LeNet[7], ImageNet [8], Fast R-CNN [9]... đang được phổ biến và được sử dụng trong nhiều ứng dụng thực tế. Đặc biệt, các kết quả đạt được thông qua các cuộc thi và nghiên cứu trong giới học thuật đều rất ấn tượng. Những phương pháp này giúp cho việc phát hiện và nhận diện biển số xe trở nên chính xác hơn, nhanh hơn và hiệu quả hơn. Việc áp dụng phương pháp học sâu này không chỉ giải quyết được bài toán giám sát giao thông tự động mà còn có thể ứng dụng trong nhiều lĩnh vực khác.
  
Vấn đề nhận diện biển số xe là một trong những hướng nghiên cứu quan trọng trong lĩnh vực thị giác máy tính. Tuy nhiên, nó cũng đang gặp phải một số khó khăn thách thức. 
- Đầu tiên là các yếu tố do môi trường, chẳng hạn như độ phức tạp của khung cảnh chứa biển số xe, gây khó khăn cho việc phân biệt biển số xe với các đối tượng khác. Ngoài ra, độ sáng và độ nhạy sáng của các thiết bị cảm biến cũng ảnh hưởng đến kết quả phát hiện và nhận dạng.

- Các yếu tố do quá trình thu nhận hình ảnh gồm độ mờ, chất lượng ảnh thấp và độ biến dạng của ảnh. Việc căn chỉnh tiêu cự của máy quay và sự chuyển động của máy quay hoặc vật thể gây ra độ mờ. Hình ảnh hay video trải qua quá trình nén và giải nén cũng sẽ dẫn đến giảm chất lượng hình ảnh. Cuối cùng, với nhiều góc độ của máy quay, hình ảnh thu được sẽ bị biến dạng.

- Ngoài ra, quá trình huấn luyện mạng deep learning cần nhiều dữ liệu để đảm bảo tính tổng quát và độ chính xác tốt. Tuy nhiên, việc thu thập và gán nhãn số lượng lớn dữ liệu là công việc tốn nhiều thời gian và công sức. 

  - Việc huấn luyện mạng cũng tốn nhiều thời gian, đặc biệt là với các mạng lớn và phức tạp. Hơn nữa, để tìm được bộ siêu tham số phù hợp với kiến trúc mạng, ta phải thực hiện việc huấn luyện lại mạng với mỗi một tham số truyền vào.
  
Dựa vào khảo sát của các đề tài hiện nay về nhận diện biển số xe, có thể nhận thấy rằng vẫn còn một số vấn đề đáng chú ý. 

- Một trong những giới hạn của các phương pháp nhận diện ký tự ứng dụng học sâu là khả năng phát hiện các ký tự có góc xoay bất kỳ. Đa phần các phương pháp hiện tại chỉ đạt được hiệu quả tối ưu với các góc xoay không quá lớn.

- Hơn nữa, đa phần các phương pháp sử dụng học sâu vẫn chưa được chứng minh là có thể áp dụng với biển số xe ở Việt Nam. Các dạng biển số xe mà các phương pháp hiện tại có thể nhận diện đều có kích thước tương đối đồng nhất và cách bố trí các ký tự không quá phức tạp, khác với biển số xe ở Việt Nam có độ phức tạp cao hơn và có nhiều dạng biển số khác nhau.

- Cuối cùng, tốc độ xử lý của các giải thuật hiện nay vẫn chưa đạt đến thời gian thực, tức là việc xử lý và nhận diện biển số xe vẫn tốn nhiều thời gian.

Trước những khó khăn nêu trên, cần có sự cải tiến và kết hợp các phương pháp hiện tại để tạo ra một phương pháp nhận diện biển số xe hiệu quả, có thể giải quyết các vấn đề đang tồn tại. Đồng thời, đề tài cũng mong muốn có thể giải quyết được các vấn đề còn tồn tại của các đề tài đi trước đó.

Trong bài toán nhận dạng biển số xe, thời gian phản hồi nhanh và độ chính xác cao là rất quan trọng để đảm bảo an toàn giao thông và quản lý tốt việc điều khiển phương tiện. Sử dụng hệ thống edge computing có thể cải thiện các yếu tố này bởi vì nó cho phép xử lý dữ liệu cục bộ tại nguồn phát sinh mà không phải truyền dữ liệu tới một trung tâm xử lý tập trung (centralized processing center) ở xa. Kết quả là giảm thiểu độ trễ và tăng tốc độ xử lý, đồng thời giảm tải băng thông mạng và chi phí lưu trữ dữ liệu. Hơn nữa, hệ thống edge computing có thể hoạt động độc lập và đảm bảo tính sẵn sàng cao, ngay cả khi kết nối mạng bị gián đoạn hoặc mất mát. Từ đó, việc áp dụng hệ thống edge computing vào bài toán nhận dạng biển số xe sẽ giúp cải thiện hiệu suất và độ tin cậy của hệ thống.

## 1.2 Mục tiêu của đề tài

Đề tài này tập trung vào việc đánh giá và cải thiện phương pháp nhận dạng biển số xe tự động trên hệ thống nhúng. Bằng việc kết hợp các kỹ thuật xử lý ảnh, mục tiêu là tạo ra một hệ thống nhận dạng biển số xe tự động có độ chính xác cao và tốc độ xử lý nhanh hơn so với các phương pháp khác, đạt độ chính xác trên 90% cho việc phát hiện biển số và trên 80% cho việc nhận diện chuỗi biển số, đồng thời cải thiện thời gian xử lý của mô hình để đảm bảo thực hiện ở thời gian thực. Đề tài này sẽ đưa ra các kết quả thực nghiệm và đánh giá hiệu quả của phương pháp được đề xuất.
  
  
## 1.3 Ý nghĩa của đề tài
### 1.3.1 Ý nghĩa thực tiễn

Phương pháp được đề xuất trong đề tài có thể áp dụng trong nhiều ứng dụng, như giám sát giao thông tự động, bãi giữ xe thông minh, trạm thu phí tự động và nhiều ứng dụng khác. Sử dụng phương pháp này có thể giúp giảm thời gian và công sức của con người, đồng thời giảm tình trạng kẹt xe và tăng sự tiện lợi cho người tham gia giao thông. Một trong những yếu tố quan trọng để đạt được hiệu quả cao của phương pháp là xây dựng được tập dữ liệu chính xác, đa dạng và phù hợp với các điều kiện thực tế tại Việt Nam. Các ứng dụng được phát triển từ phương pháp này sẽ mang lại lợi ích cho cả xã hội và góp phần nâng cao chất lượng cuộc sống của người dân.

### 1.3.2 Ý nghĩa khoa học
Đề tài đóng góp một phương pháp mới trong việc phát hiện và nhận diện biển số xe hiệu quả, với mục tiêu tăng độ chính xác và giải quyết các vấn đề còn tồn tại của các phương pháp đi trước. Nghiên cứu này có thể cung cấp cơ sở cho các nghiên cứu trong nước về sau, đặc biệt là trong lĩnh vực ứng dụng các hệ thống nhúng. Tập dữ liệu chính xác, đa dạng và sát với điều kiện thực tế của nước ta cũng được xem là một đóng góp đáng kể của nghiên cứu này.
  
## 1.4 Phạm vi của đề tài
Trong đề tài, tập dữ liệu được sử dụng để huấn luyện và kiểm tra mô hình chỉ bao gồm các hình ảnh biển số xe được chụp theo phương ngang, không bị che khuất, không bị hư hỏng, tróc sơn, rỉ sét và có độ mờ và độ biến dạng thấp. Vị trí của camera để thu thập hình ảnh là cố định hoặc di động với góc lệch không quá lớn. Hình ảnh có thể bị nhiễu từ thời tiết như mưa, sương mù, vv., nhưng vẫn có thể nhận dạng được đầy đủ các ký tự bằng mắt thường. Trong đề tài, chỉ sử dụng các biển số xe máy và ô tô phổ biến tại Việt Nam, tuân thủ theo Thông tư 58/2020/TT-BCA về kích thước, ký hiệu và bố trí của biển số xe. Các biển số xe của các nước khác sẽ không được xem xét trong đề tài. 

## 1.5 Bố cục luận văn
Báo cáo này gồm 7 chương, trong đó Chương 2 tập trung vào giới thiệu các nghiên cứu liên quan đến bài toán phát hiện và nhận dạng biển số xe, cùng với các phương pháp giải quyết được áp dụng trong lĩnh vực này. Chương 3 cung cấp những kiến thức cơ bản để đặt nền móng cho các mô hình được đề xuất trong Chương 4. Chương 5 bao gồm thông tin về các thí nghiệm thực hiện, các chỉ tiêu đánh giá và kết quả đánh giá của các phương pháp, đồng thời cũng đưa ra một số nhận xét dựa trên kết quả đạt được. Chương 6 đưa ra kết luận chung của báo cáo và trình bày những hướng phát triển tiềm năng trong tương lai. Cuối cùng, Chương 7 trình bày danh sách các tài liệu tham khảo được sử dụng trong đề tài.









