import os
import pysrt
import webvtt
from Levenshtein import ratio
import argparse

def read_lyrics(file_path):
    """Đọc nội dung file lyrics"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def process_srt(input_file, lyrics_file, output_file):
    """Xử lý file SRT"""
    subs = pysrt.open(input_file)
    lyrics = read_lyrics(lyrics_file)
    
    # Tạo mapping giữa lyrics và subtitles
    for sub in subs:
        best_match = None
        best_ratio = 0
        
        for lyric in lyrics:
            similarity = ratio(sub.text.lower(), lyric.lower())
            if similarity > best_ratio and similarity > 0.7:  # Ngưỡng tương đồng 70%
                best_ratio = similarity
                best_match = lyric
        
        if best_match:
            sub.text = best_match
    
    subs.save(output_file, encoding='utf-8')

def process_vtt(input_file, lyrics_file, output_file):
    """Xử lý file VTT"""
    vtt = webvtt.read(input_file)
    lyrics = read_lyrics(lyrics_file)
    
    # Tạo mapping giữa lyrics và subtitles
    for caption in vtt:
        best_match = None
        best_ratio = 0
        
        for lyric in lyrics:
            similarity = ratio(caption.text.lower(), lyric.lower())
            if similarity > best_ratio and similarity > 0.7:  # Ngưỡng tương đồng 70%
                best_ratio = similarity
                best_match = lyric
        
        if best_match:
            caption.text = best_match
    
    vtt.save(output_file)

def main():
    parser = argparse.ArgumentParser(description='Cải thiện nội dung file SRT/VTT dựa trên lyrics')
    parser.add_argument('input_file', help='File SRT hoặc VTT đầu vào')
    parser.add_argument('lyrics_file', help='File lyrics (txt)')
    parser.add_argument('output_file', help='File SRT hoặc VTT đầu ra')
    
    args = parser.parse_args()
    
    input_ext = os.path.splitext(args.input_file)[1].lower()
    
    if input_ext == '.srt':
        process_srt(args.input_file, args.lyrics_file, args.output_file)
    elif input_ext == '.vtt':
        process_vtt(args.input_file, args.lyrics_file, args.output_file)
    else:
        print("Định dạng file không được hỗ trợ. Vui lòng sử dụng file .srt hoặc .vtt")

if __name__ == '__main__':
    main() 