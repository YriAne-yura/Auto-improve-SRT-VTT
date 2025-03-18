# Auto-improve SRT/VTT

Công cụ tự động cải thiện nội dung file phụ đề SRT hoặc VTT dựa trên file lyrics.

## Cài đặt

1. Cài đặt Python 3.7 trở lên
2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cách sử dụng

Chạy chương trình với cú pháp:
```bash
python main.py input_file.srt lyrics.txt output_file.srt
```

hoặc cho file VTT:
```bash
python main.py input_file.vtt lyrics.txt output_file.vtt
```

### Tham số:
- `input_file`: File SRT hoặc VTT cần cải thiện
- `lyrics_file`: File text chứa lyrics chính xác
- `output_file`: File SRT hoặc VTT đầu ra đã được cải thiện

## Cách hoạt động

Chương trình sẽ:
1. Đọc file lyrics và file phụ đề
2. So sánh từng dòng phụ đề với lyrics sử dụng thuật toán Levenshtein
3. Thay thế nội dung phụ đề bằng lyrics tương ứng nếu độ tương đồng > 70%
4. Lưu kết quả vào file đầu ra

## Tính năng
- Hỗ trợ cả định dạng SRT và VTT
- Giữ nguyên thời gian và định dạng gốc
- Sử dụng thuật toán Levenshtein để so sánh độ tương đồng text
- Có thể điều chỉnh ngưỡng tương đồng (mặc định: 70%)

## Xem thêm
Để xem tài liệu tiếng Anh, vui lòng xem [README.md](README.md) 