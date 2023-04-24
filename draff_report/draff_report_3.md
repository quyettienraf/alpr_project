# CHƯƠNG 3: CƠ SỞ LÝ THUYẾT

Chương này giải thích các kiến thức nền tảng liên quan đến phương pháp học sâu, đây là cơ sở để xây dựng các phương pháp mới được đề xuất.
  
## 3.1 Mạng nơ-ron truyền thẳng
Các kiến trúc mạng học sâu hiện nay đều được bắt nguồn từ mạng nơ-ron truyền thẳng. Mạng nơ-ron truyền thẳng có thể được coi là một hàm số phi tuyến tính $f_W(x)$, trong đó dữ liệu đầu vào là một vector $x_i$, và nhãn tương ứng của dữ liệu đó là $y_i$. Cấu trúc của mạng nơ-ron truyền thẳng bao gồm nhiều đơn vị nơ-ron kết nối với nhau theo thứ tự. 

<img width="782" alt="Screenshot 2023-04-24 at 04 16 02" src="https://user-images.githubusercontent.com/13607004/233866721-953d4002-9c62-40a0-a219-6741644c7426.png">
<i> Cấu trúc một nơ-ron </i>


Mỗi đơn vị này bao gồm vector dữ liệu đầu vào $x_i$, ma trận trọng số (weights) $w_ij$, hệ số bias $b_i$, hàm tính tổng trọng số và hàm kích hoạt. Hàm tính tổng trọng số được định nghĩa bởi công thức tính tổng của tích hai giá trị, vector đầu vào và ma trận trọng số tương ứng, kết hợp với bias. Hàm kích hoạt là một hàm phi tuyến tính được áp dụng lên kết quả tính tổng trọng số.

### 3.1.1 Hàm kích hoạt
- Sigmoid
- Tanh
- ReLU
- Leaky ReLU
- Maxout
- ELU

### 3.1.2 Hàm lỗi
Trong quá trình huấn luyện mạng nơ-ron, mục tiêu là giảm thiểu sai số giữa kết quả dự đoán và nhãn. Để làm điều này, hàm lỗi được sử dụng để phạt mô hình mỗi khi nó dự đoán sai, với mức độ phạt tỷ lệ thuận với mức độ sai. Hàm lỗi cần đáp ứng hai tính chất quan trọng: trả về giá trị không âm và có đạo hàm liên tục. Có nhiều hàm lỗi khác nhau được sử dụng cho các bài toán khác nhau, nhưng đối với bài toán phát hiện và nhận dạng, thì một số hàm lỗi thông thường được sử dụng, bao gồm Mean Square Error (MSE), Cross Entropy, Smooth-L1, và CTC.

- Hàm lỗi Mean Square Error (MSE)
- Hàm lỗi Cross Entropy
- Hàm lỗi Smooth-L1
- Hàm lỗi CTC

### 3.1.3 Quá trình tối ưu hóa

## 3.2 Mạng nơ-ron tích chập

### 3.2.1 Tính chất mạng nơ-ron tích chập

### 3.2.2 Lấy mẫu (Subsampling hay pooling)

## 3.3 Mạng nơ-ron đệ quy



