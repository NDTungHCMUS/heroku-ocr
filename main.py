from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

@app.get("/{text}")
async def responseOCR(text):
    # Đường dẫn file input
    input_file_path = './ocr_ok.txt'  # Thay đường dẫn bằng đường dẫn thực tế của file của bạn
    output_file_path = './resultOcr.txt'  # File kết quả

    # Từ khóa cần tìm
    search_keyword = text

    # Mảng lưu kết quả
    result_videos = []

    # Đọc file văn bản
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Đọc tất cả các dòng trong file

    # Tìm kiếm các dòng chứa từ khóa
    for line in lines:
        # Tách video và phần nội dung dựa trên ký tự ':'
        if ' : ' in line:
            video, content = line.split(' : ', 1)
            # Kiểm tra nếu từ khóa xuất hiện trong phần nội dung
            if search_keyword.lower() in content.lower():  # Tìm kiếm không phân biệt hoa thường
                videoStrip = video.strip()
                result_videos.append(f"https://ai-challenge-melody.s3.ap-southeast-1.amazonaws.com/{videoStrip}.jpg")  # Lưu video nếu tìm thấy từ khóa
    return result_videos

# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')
    # origins = ['http://localhost:3000','http://192.168.178.23:3000']

    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=origins,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )