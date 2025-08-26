# File Organizer 🗂️

Automatically organize files in a folder (like Downloads) by extension into subfolders.

## Features

- Organizes files by their extension into separate folders
- Handles files with no extension (places them in a "no_extension" folder)
- Prevents overwriting existing files
- Provides clear feedback on the organization process
- Error handling for invalid directories

## How to Use

1. Run the script:
   ```bash
   python file_organizer.py
   ```

2. When prompted, enter the path to the directory you want to organize (e.g., your Downloads folder)

3. The script will create subfolders for each file extension and move the files accordingly

## Example

Before running the script:
```
Downloads/
├── document.pdf
├── image.jpg
├── script.py
├── archive.zip
└── README
```

After running the script:
```
Downloads/
├── pdf/
│   └── document.pdf
├── jpg/
│   └── image.jpg
├── py/
│   └── script.py
├── zip/
│   └── archive.zip
└── no_extension/
    └── README
```

## Requirements

- Python 3.x
- No external dependencies (uses only built-in `os` and `shutil` modules)