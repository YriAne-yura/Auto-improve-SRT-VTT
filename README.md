# Auto-improve SRT/VTT

A tool to automatically improve SRT or VTT subtitle files based on lyrics text files.

## Installation

### Windows

1. Install Python 3.7 or higher from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation
2. Open Command Prompt (cmd) or PowerShell
3. Navigate to the project directory:
```bash
cd path/to/Auto-improve-SRT-VTT
```

4. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

5. Install required libraries:
```bash
pip install -r requirements.txt
```

### Linux (Ubuntu/Debian)

1. Install Python 3.7 or higher:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

2. Install python3-venv:
```bash
sudo apt install python3-venv
```

3. Open terminal and navigate to the project directory:
```bash
cd path/to/Auto-improve-SRT-VTT
```

4. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Install required libraries:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you're in the virtual environment:
   - Windows: You should see `(venv)` at the start of your command prompt
   - Linux: You should see `(venv)` at the start of your terminal prompt

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

## Troubleshooting

### Windows
- If you get "python is not recognized" error, make sure Python is added to PATH
- If you get permission errors, try running Command Prompt as Administrator

### Linux
- If you get permission errors, use `sudo` for installation commands
- If you get "command not found" for python3, install it using `sudo apt install python3`

## See also
For Vietnamese documentation, please see [README.vi.md](README.vi.md) 