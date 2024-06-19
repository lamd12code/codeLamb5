import cv2
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("C:/Users/DELL/PycharmProjects/ANPR/model/last.pt")

# Define path to the image file
source = "C:/Users/DELL/PycharmProjects/ANPR/z5527464088993_92c5e7508b3da3a051ccf4528bd63ea6.jpg"

# Run inference on the source
results = model(source)  # list of Results objects

# Lấy ảnh gốc
img = cv2.imread(source)

# Duyệt qua các kết quả phát hiện đối tượng
for result in results:
    boxes = result.boxes.xyxy.numpy()  # Lấy tọa độ hộp giới hạn (bounding box)
    confidences = result.boxes.conf.numpy()  # Lấy độ tin cậy của hộp giới hạn
    classes = result.boxes.cls.numpy()  # Lấy lớp của hộp giới hạn

    # Vẽ các hộp giới hạn trên ảnh
    for i, (box, confidence, cls) in enumerate(zip(boxes, confidences, classes)):
        x1, y1, x2, y2 = map(int, box)
        label = f"Class: {int(cls)}, Conf: {confidence:.2f}"
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

# Lưu ảnh kết quả
result_path = "C:/Users/DELL/PycharmProjects/ANPR/result_image.jpg"
cv2.imwrite(result_path, img)

# Hiển thị ảnh kết quả
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

