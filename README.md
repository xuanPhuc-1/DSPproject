# MÔ PHỎNG ĐA PHƯƠNG PHÁP XỬ LÝ NHIỄU TRONG TÍN HIỆU SỐ

Báo cáo này được thực hiện với mục đích tìm hiểu, mô phỏng và đánh giá hiệu suất của bốn phương pháp chính trong việc xử lý nhiễu trong tín hiệu số. Cụ thể chúng ta sẽ tập trung vào: Biến đổi Fourier Nhanh (FFT), Bộ lọc thông thấp (LPF), Biến đổi Wavelet và Bộ phát hiện hoạt động giọng nói (Voice Activity Detector), từ đó hiểu rõ ưu điểm và hạn chế của từng phương pháp để xác định phương pháp nào là phù hợp nhất trong các tình huống cụ thể.

## Bắt Đầu

Hướng dẫn cài đặt và chạy dự án trên máy cục bộ. Dưới đây là hướng dẫn cụ thể cho mỗi hệ điều hành:

### Linux / macOS

1. Clone dự án về máy của bạn:

   ```bash
   git clone https://github.com/xuanPhuc-1/DSPproject
   ```

2. Di chuyển vào thư mục dự án:

   ```bash
   cd DSPproject
   ```

3. Cài đặt dependencies:

   ```bash
   python3 -m pip install requirement.txt
   ```

4. Chạy dự án:

   ```bash
   python3 ./FinalMenuWindow.py
   ```

### Windows (PowerShell)

1. Clone dự án về máy của bạn:

   ```bash
   git clone https://github.com/xuanPhuc-1/DSPproject
   ```

2. Di chuyển vào thư mục dự án:

   ```bash
   cd DSPproject
   ```

3. Cài đặt dependencies:

   ```bash
   pip install requirement.txt
   ```

4. Chạy dự án:

   ```bash
   python FinalMenuWindow.py
   ```

Chắc chắn rằng bạn đã cài đặt Python trước khi thực hiện các bước trên.

Bạn có thể tìm thêm thông tin về cách cài đặt Python cho từng hệ điều hành tại [https://python.org/].

### Yêu Cầu

Note: Nên sử dụng Python 3.6 trở lên. Cụ thể, phiên bản Python được sử dụng trong dự án này là **Python 3.8**

## Sử Dụng

Cách sử dụng đã nằm trong báo cáo của dự án.

## Liên Hệ

qua email hoặc các kênh truyền thông xã hội.

- Email: [Ngô Lê Xuân Phúc](mailto:20021568@vnu.edu.vn)

- Email: [Nguyễn Phương Nga](mailto:20021558@vnu.edu.vn)

## Người Đóng Góp

- [Ngô Lê Xuân Phúc](https://github.com/xuanPhuc-1)
- [Nguyễn Phương Nga](https://github.com/phuongnga28)

## Thư Viện Được Sử Dụng

![numpy](https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg)
![PyQt5](https://upload.wikimedia.org/wikipedia/commons/e/e6/Python_and_Qt.svg)

Danh sách các thư viện và phiên bản tương ứng:

- numpy 1.24.4
- PyQt5 5.15.10
- PyQt5-Qt5 5.15.2
- PyQt5-sip 12.13.0
- pyqtgraph 0.13.3
- PyWavelets 1.4.1
- setuptools 41.2.0
