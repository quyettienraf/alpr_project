# Đánh giá các mô hình học máy
https://viblo.asia/p/danh-gia-cac-mo-hinh-hoc-may-RnB5pp4D5PG
### Abstract
Đánh giá mô hình giúp chúng ta chọn lựa được các mô hình phù hợp với bài toán cụ thể. Để có thể áp dụng đúng thước đo đánh giá mô hình phù hợp, chúng ta cần hiểu bản chất, ý nghĩa cũng như các trường hợp sử dụng nó. 
Tập trung phân tích các metric đánh giá đối với: mô hình phân loại (classification), mô hình hồi quy (regression) và xếp hạng (Ranking)

### Confusion Matrix
Confusion matrix (AKA error matrix). Nó thể hiện được có bao nhiêu điểm dữ liệu thực sự thuộc vào một class, và được dự đoán là rơi vào một class.
Ví dụ một bài toán phân loại ảnh đó là mèo hay không, trong dữ liệu dự đoán có 100 ảnh là mèo, 1000 ảnh không phải là mèo. Ở đây, kết quả dự đoán là như sau

Trong 100 ảnh mèo dự đoán đúng 90 ảnh, còn 10 ảnh được dự đoán là không phải. Nếu ta coi cat là “positive” và non-cat là “negative”, thì 90 ảnh được dự đoán là cat, được gọi là True Positive, còn 10 ảnh được dự đoán non-cat kia được gọi là False Negative
Trong 1000 ảnh non-cat, dự đoán đúng được 940 ảnh là non-cat, được gọi là True Negative, còn 60 ảnh bị dự đoán nhầm sang cat được gọi là False Positive

Có thể tới đây nhiều người sẽ khá là lẫn lộn, “True”, “False” rồi “Positive”, “Negative”. Vậy để có một cách dễ nhớ, có một mánh nhỏ như sau

True/False ý chỉ những gì ta đã dự đoán là đúng hay chưa
Positive/Negative chỉ những gì ta dự đoán (có hoặc không) Nói cách khách, nếu thấy chữ True tức là dự đoán là đúng (là cat hay non-cat, chỉ cần đúng), còn False thì ngược lại.
  
### Classification Accuracy
Đây là độ đo của bài toán phân loại mà đơn giản nhất, tính toán bằng cách lấy số dự đoán đúng chia cho toàn bộ các dự đoán. Ví dụ với bài toán Cat/Non-cat như trên, độ chính xác sẽ được tính như sau:

Classification Accuracy = (90+940)/(1000+100) = 93.6%
  
Nhược điểm của cách đánh giá này là chỉ cho ta biết được bao nhiêu phần trăm lượng dữ liệu được phân loại đúng mà không chỉ ra được cụ thể mỗi loại được phân loại như thế nào, lớp nào được phân loại đúng nhiều nhất hay dữ liệu của lớp nào thường bị phân loại nhầm nhất vào các lớp khác.
  
