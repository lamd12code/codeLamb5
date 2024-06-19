import pandas as pd 

def save_to_csv(data, csv_file_path=r'.\result_data\result_data.csv'):
    # Tạo DataFrame từ dữ liệu
    df = pd.DataFrame(data)
    # Ghi DataFrame vào file CSV
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
    print(f"Data successfully saved to {csv_file_path}")

# Thử lưu file đơn giản
# data = {"ID": 1, "Path":r'D:\ANPR\ANPR\result_data',"Time":123, "License plate":'29AA H9 12345'}
# save_to_csv(data)