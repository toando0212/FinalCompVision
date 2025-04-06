from PIL import Image

def check_image_mode(image_path):
    try:
        # Mở ảnh
        img = Image.open(image_path)
        # Kiểm tra mode của ảnh
        if img.mode == "RGBA":
            return "Ảnh là dạng RGBA"
        elif img.mode == "L":
            return "Ảnh là dạng Grayscale"
        else:
            return f"Ảnh có mode khác: {img.mode}"
    except Exception as e:
        return f"Lỗi khi xử lý ảnh: {e}"

# Ví dụ sử dụng
image_path =  r"E:\HANDS-VNOnDB\Processed_Images_Paragraphs\20140603_0003_BCCTC_tg_0.png"  # Thay bằng đường dẫn ảnh của bạn
result = check_image_mode(image_path)
print(result)
