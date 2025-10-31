# 🖼️ Image to PDF Converter
This Python script allows you to resize and optionally compress one or multiple image files (.jpg, .jpeg, .png) into a single PDF file.
It supports both single-file input and folder input and can be run entirely from the command line.

## ✨ Features
- 📁 Accepts folder or single image file as input
- 🔍 Adjustable resize scale (-s)
- 🗜️ Optional compression using JPEG quality (-c, range 1–100)
- 🧩 Combines all images into one PDF output
- ⚙️ Simple CLI interface using argparse

## 🧰 Requirements
Make sure you have Python 3 installed, along with the Pillow library:
```
pip install pillow
```

## 🚀 Usage
Run the script from the terminal using:
```
python app.py -i <input> -o <output.pdf> [-s <scale>] [-c <compression>]
```

### Arguments
|Flag|Description|Required|Default|
|-----------|--------------|-----------|----------|
|-i, --input|Path to an image file or a folder containing images|✅ Yes|—|
|-o, --output|Name of the output PDF file|✅ Yes|—|
|-s, --scale|Resize scale factor (e.g. 0.5 = 50%)|❌ No|0.8|
|-c, --compress|JPEG compression quality (1–100). If omitted, compression is disabled.|❌ No|95|

## 🧩 Examples
### 1. Convert a single image without compression
```
python3 app.py -i photo.png -o output.pdf
```
### 2. Convert all images in a folder, scale to 50%
```
python3 app.py -i images -o result.pdf -s 0.5
```
### 3. Convert and compress images with quality 60
```
python3 app.py -i photos -o compressed.pdf -s 0.5 -c 60
```
### 4. Show help
```
python3 app.py --help
```

## 📄 License
This project is released under the MIT License, giving you full freedom to use, modify, and distribute it — whether for personal, educational, or commercial purposes.
