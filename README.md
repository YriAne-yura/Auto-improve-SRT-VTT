# Auto-improve SRT/VTT

A tool to automatically improve SRT or VTT subtitle files based on lyrics text files.

## Installation

1. Install Python 3.7 or higher
2. Install python3-venv (for Ubuntu/Debian):
```bash
sudo apt install python3-venv
```

3. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

4. Install required libraries:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you're in the virtual environment (you should see `(venv)` at the start of your command prompt)

2. Run the program with the following syntax:
```bash
python main.py input_file.srt lyrics.txt output_file.srt
```

or for VTT files:
```bash
python main.py input_file.vtt lyrics.txt output_file.vtt
```

### Parameters:
- `input_file`: Input SRT or VTT file to improve
- `lyrics_file`: Text file containing accurate lyrics
- `output_file`: Output SRT or VTT file with improved content

## How it works

The program will:
1. Read both the lyrics and subtitle files
2. Compare each subtitle line with lyrics using the Levenshtein algorithm
3. Find the best matches between subtitles and lyrics based on similarity
4. Replace subtitle content with matching lyrics if similarity > 50%
5. Save the result to the output file

## Features
- Supports both SRT and VTT formats
- Maintains original timing and formatting
- Uses Levenshtein distance for text similarity matching
- Configurable similarity threshold (default: 50%)
- Prevents duplicate lyrics usage
- Prioritizes matches with higher similarity

## See also
For Vietnamese documentation, please see [README.vi.md](README.vi.md) 