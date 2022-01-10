# Model evaluation using mAP
## Đánh giá model bằng mAP - Object detection
mỗi model Object detection sau khi đào tạo, cần có những thang điểm để đánh giá sự chính xác của nó
hiện tại chúng ta đánh giá một model dựa trên: loss function, IOU avg, mAP, đánh giá trực quan
nhiều bài báo cũng như các trang web lớn thường sử dụng mAP như là thước đo chính.
## khái niệm và cách tính AP,mAP.
## 1.1. Một vài khái niệm cần nắm trong việc đánh giá một model object detection.
- IOU( Intersection over union)
Intersection over Union là chỉ số đánh giá được sử dụng để đo độ chính xác của phát hiện đối tượng trên tập dữ liệu cụ thể.
Chỉ số này thường được gặp trong các Object Detection Challenge.
IOU thường được đánh giá hiệu năng của các bộ phát hiện đối tượng như HOG + Linear SVM và mạng nơ ron tích chập (R-CNN, FastR-CNN, YOLO,…).
Để áp dụng được IoU để đánh giá cần:
– Đường bao thực (ground-truth bounding box): là đường bao mà chúng ta gán cho vật thể bằng labelImg tool
– Đường bao dự đoán (predicted bouding box): là đường bao chúng ta sử dụng file Weights sau khi đào tạo để nhận dạng.
Dưới đây là ví dụ về đường bao thực và đường bao được dự đoán. Đường bao được dự đoán được vẽ bằng màu vàng, trong khi đó đường bao thực được vẽ bằng màu xanh lá. Mục tiêu ta là tính toán IoU (Intersection over Union) giữa hai đường bao
<div align='center'>
  <img src="./img/1_1_IOU.png" width="60%">
</div>
Tỷ lệ này là IoU (Intersection over union) là tỉ lệ giữa đo lường mức độ giao nhau giữa hai đường bao (thường là đường bao dự đoán và đường bao thực) để nhằm xác định hai khung hình có bị đè chồng lên nhau không.
Tỷ lệ này được tính dựa trên phần diện tích giao nhau gữa 2 đường bao với phần tổng diện tích giao nhau và không giao nhau giữa chúng.
<div align='center'>
  <img src="./img/1_2_IOU_2.png" width="60%">
</div>
Các tiêu chí được dùng để đánh giá:
– Đối tượng được nhận dạng đúng với tỉ lệ IOU > 0.5 (True positive : TP)
<div align='center'>
  <img src="./img/7-2-300x169.png" width="60%">
</div>
– Đối tượng được nhận dạng sai với tỉ lệ IOU < 0.5 (False positive : FP)
<div align='center'>
  <img src="./img/8-2-300x169.png" width="60%">
</div>
– Đối tượng không được nhận dạng (False negative: FN)