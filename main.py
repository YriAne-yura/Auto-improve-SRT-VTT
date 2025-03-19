import os
import pysrt
import webvtt
from Levenshtein import ratio
import argparse

def read_lyrics(file_path):
    """Đọc nội dung file lyrics"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def find_best_matches(subs, lyrics, threshold=0.5):
    """Tìm các cặp subtitle-lyrics có độ tương đồng cao nhất"""
    matches = []
    used_lyrics = set()
    used_subs = set()
    
    # Tìm tất cả các cặp có độ tương đồng cao
    for i, sub in enumerate(subs):
        if i in used_subs:
            continue
            
        best_match = None
        best_ratio = 0
        best_lyric_idx = -1
        
        for j, lyric in enumerate(lyrics):
            if j in used_lyrics:
                continue
                
            similarity = ratio(sub.text.lower(), lyric.lower())
            if similarity > best_ratio and similarity > threshold:
                best_ratio = similarity
                best_match = lyric
                best_lyric_idx = j
        
        if best_match:
            matches.append((i, best_lyric_idx, best_ratio))
            used_lyrics.add(best_lyric_idx)
            used_subs.add(i)
    
    # Sắp xếp theo độ tương đồng giảm dần
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches

def process_srt(input_file, lyrics_file, output_file):
    """Xử lý file SRT"""
    subs = pysrt.open(input_file)
    lyrics = read_lyrics(lyrics_file)
    
    # Tìm các cặp có độ tương đồng cao nhất
    matches = find_best_matches(subs, lyrics)
    
    # Áp dụng các thay đổi
    for sub_idx, lyric_idx, ratio in matches:
        print(f"Sửa '{subs[sub_idx].text}' thành '{lyrics[lyric_idx]}' (độ tương đồng: {ratio:.2f})")
        subs[sub_idx].text = lyrics[lyric_idx]
    
    subs.save(output_file, encoding='utf-8')

def process_vtt(input_file, lyrics_file, output_file):
    """Xử lý file VTT"""
    vtt = webvtt.read(input_file)
    lyrics = read_lyrics(lyrics_file)
    
    # Tìm các cặp có độ tương đồng cao nhất
    matches = find_best_matches(vtt, lyrics)
    
    # Áp dụng các thay đổi
    for caption_idx, lyric_idx, ratio in matches:
        print(f"Sửa '{vtt[caption_idx].text}' thành '{lyrics[lyric_idx]}' (độ tương đồng: {ratio:.2f})")
        vtt[caption_idx].text = lyrics[lyric_idx]
    
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