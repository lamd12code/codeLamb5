import cv2
from ultralytics import YOLO
from PIL import Image
import easyocr
import os
# Gọi hàm từ 2 file vừa tạo
from read_data import read_files_in_directory
from save_data import save_to_csv

# Tại biến lưu đường dẫn để lưu được các hình ảnh
result_folder = r'.\result_data'

# Load a pretrained YOLO model
license_plate_detector = YOLO(r'.\model\last.pt')

# Khởi tạo EasyOCR reader
reader = easyocr.Reader(['en'])

# Lấy danh sách các tên file và các biến cap phục vụ cho việc đuọc và lưu dứ liệu
list_cap, list_filename = read_files_in_directory(r'.\input_data\video')

# Tạo ra danh sách để chứa các thông tin về file
save_data = []
for id in range(len(list_cap)):
    frame_id = 0
    while list_cap[id].isOpened():
        fps = list_cap[id].get(cv2.CAP_PROP_FPS)
        ret, frame = list_cap[id].read()
        if not ret:
            break

        # Chuyển đổi frame sang định dạng PIL Image
        input_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Nhận diện biển số xe trong frame
        detections = license_plate_detector(input_image)
        license_plate_boxes = detections[0].boxes.data.cpu().numpy()

        for i, box in enumerate(license_plate_boxes):
            x1, y1, x2, y2, conf, cls = box
            license_plate = input_image.crop((x1, y1, x2, y2))

            # Lưu ảnh biển số vào một thư mục tạm thời
            directory_path = f'{result_folder}\{list_filename[id]}' #tạo thư mục nếu như chưa có
            if not os.path.exists(directory_path):
                os.makedirs(directory_path, exist_ok=True)

            plate_filename = f'{directory_path}\license_plate_{frame_id}_{i}.jpg' #lưu ảnh bsx vào thư mục bên trên
            license_plate.save(plate_filename) # hàm lưu
            print(f'Saved to {plate_filename}') #

            # Đọc nội dung biển số sử dụng EasyOCR
            results = reader.readtext(plate_filename)

            # In ra nội dung biển số
            if results:
                data = {"ID": i+1, "Path": plate_filename, "Time": frame_id//fps, 'License plate': results[0][1]}
                print("Data:",data)
                save_data.append(data)
                print(f"Frame {frame_id} - License Plate {i + 1} Text: {results[0][1]}")

        frame_id += 1

    # Giải phóng và đóng video
    list_cap[id].release()

# Lưu thông tin của các file về file CSV (Dùng Excel để có thể mở ra và đọc dữ liệu)
save_to_csv(save_data)
exit()
# cv2.destroyAllWindows() 