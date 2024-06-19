

Bước 1: Tạo folder input_data/video
-    Đây là nơi đưa các video thử nghiệm vào trong mô hình

Bước 2: Tạo folder result_data để lưu các file đầu ra của chương trình

Bước 3: Tạo môi trường: 
-   python -m venv venv 
-   Python3 -m venv venv

Bước 4: Cài các thư viên cần thiết
-   Cái các thư viện trong file setup.txt: pip install -r setup.txt
-   Các các thư viện đặc biệt: 
    -   Gỡ các thư viện bị lỗi: pip uninstall torch torchvision
    -   Cài đặt các thư viện đặc biệt: pip install torch==2.2.2+cpu torchaudio==2.2.2+cpu torchvision==0.17.2+cpu torchmetrics==0.10.3 -f https://download.pytorch.org/whl/torch_stable.html

Bước 5: Chạy file main: python source_code\main.py
