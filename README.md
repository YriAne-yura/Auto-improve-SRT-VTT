# Auto-improve SRT/VTT

A tool to automatically improve SRT or VTT subtitle files based on lyrics text files.

## Installation

1. Install Python 3.7 or higher
2. Install required libraries:
```bash
pip install -r requirements.txt
```

## Usage

Run the program with the following syntax:
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
3. Replace subtitle content with matching lyrics if similarity > 70%
4. Save the result to the output file

## Features
- Supports both SRT and VTT formats
- Maintains original timing and formatting
- Uses Levenshtein distance for text similarity matching
- Configurable similarity threshold (default: 70%)

## See also
For Vietnamese documentation, please see [README.vi.md](README.vi.md) 