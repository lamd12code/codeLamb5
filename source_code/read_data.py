import os
import cv2

def read_files_in_directory(directory_path):
    """
    Đọc nội dung của tất cả các tệp video trong thư mục chỉ định và in ra màn hình.
    
    :param directory_path: Đường dẫn đến thư mục
    """
    list_cap = []
    list_filename = []
    try:
        # Kiểm tra xem thư mục có tồn tại không
        if not os.path.exists(directory_path):
            print(f"Thư mục '{directory_path}' không tồn tại.")
            return
        
        # Liệt kê tất cả các tệp video trong thư mục
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Kiểm tra xem đó có phải là tệp video không
            if os.path.isfile(file_path):
                try:
                    # print(file_path)
                    # Mở và đọc nội dung của tệp video
                    cap = cv2.VideoCapture(file_path)
                    if not cap.isOpened():
                        print("Error: Could not open video.")
                        continue
                    list_cap.append(cap)
                    list_filename.append(filename[:-4])
                except Exception as e:
                    print(f"Không thể đọc tệp video '{filename}': {e}")
        return list_cap, list_filename
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn đến thư mục (thay thế bằng đường dẫn thực tế của bạn)
# directory_path = r'E:\ANPR\input_data\video'

# Gọi hàm để đọc các tệp video trong thư mục
# print(read_files_in_directory(directory_path))