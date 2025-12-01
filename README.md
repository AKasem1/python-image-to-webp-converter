```markdown
# 🖼️ Image to WebP Converter

A Python script that converts PNG, JPG, and JPEG images to WebP format for improved website performance. WebP images are typically 25-35% smaller than JPEGs while maintaining comparable quality, resulting in faster page load times and reduced bandwidth usage.

## ✨ Features

- **Single file conversion** - Convert individual images with custom quality settings
- **Batch processing** - Convert entire directories at once
- **Recursive directory scanning** - Process subdirectories automatically
- **Transparency support** - Preserves alpha channels from PNG images
- **File size reporting** - Shows compression percentage for each conversion
- **Interactive prompts** - User-friendly interface with guided input
- **Auto-generated output paths** - Automatically creates WebP filenames from input files

## 📋 Requirements

- Python 3.6 or higher
- Pillow library (PIL)

## 🚀 Installation

1. Clone or download this script to your local machine

2. Install the required dependency:
```
pip install Pillow
```

Or upgrade if already installed:
```
pip install --upgrade Pillow
```

## 💻 Usage

Run the script:
```
python converter.py
```

The script will present you with an interactive menu:

```
==================================================
Image to WebP Converter
==================================================

Conversion options:
1. Convert single file
2. Convert all images in a directory

Enter your choice (1 or 2):
```

### Single File Conversion

1. Select option `1`
2. Enter the path to your image file
3. Enter quality (0-100, or press Enter for default 85)
4. Enter output path (or press Enter to auto-generate)

**Example:**
```
Enter image path (PNG/JPG/JPEG): images/photo.jpg
Enter quality (0-100, default 85): 80
Enter output path (press Enter to auto-generate): [Press Enter]

✓ Converted: images/photo.jpg -> images/photo.webp
  Size: 2,456,789 bytes -> 1,654,321 bytes (32.7% reduction)
```

### Batch Conversion

1. Select option `2`
2. Enter the directory path containing images
3. Enter output directory (or press Enter to use the same directory)
4. Enter quality (0-100, or press Enter for default 85)
5. Choose whether to process subdirectories (y/n)

**Example:**
```
Enter directory path: ./images
Enter output directory (press Enter to use same directory): ./webp_output
Enter quality (0-100, default 85): 85
Process subdirectories? (y/n, default n): y

✓ Converted: images/photo1.jpg -> webp_output/photo1.webp
  Size: 1,234,567 bytes -> 876,543 bytes (29.0% reduction)
✓ Converted: images/vacation/beach.png -> webp_output/beach.webp
  Size: 3,456,789 bytes -> 2,123,456 bytes (38.6% reduction)

==================================================
Conversion complete: 2 successful, 0 failed
```

## ⚙️ Quality Settings

The `quality` parameter controls the trade-off between file size and image quality:

| Quality Range | Use Case | Description |
|--------------|----------|-------------|
| **60-75** | Web optimized | Smaller files, good for thumbnails or background images |
| **80-85** | Recommended | Balanced quality and file size, ideal for most websites |
| **90-95** | High quality | Larger files, use for hero images or photography portfolios |

## 📁 Directory Structure Example

**Before conversion:**
```
project/
├── images/
│   ├── photo1.jpg
│   ├── photo2.png
│   └── products/
│       ├── item1.jpg
│       └── item2.png
```

**After conversion (with recursive=True):**
```
project/
├── images/
│   ├── photo1.jpg
│   ├── photo1.webp     ← New
│   ├── photo2.png
│   ├── photo2.webp     ← New
│   └── products/
│       ├── item1.jpg
│       ├── item1.webp  ← New
│       ├── item2.png
│       └── item2.webp  ← New
```

## 🔄 Recursive Processing

When processing directories, you can choose whether to include subdirectories:

- **No (default)**: Only converts images in the specified folder
- **Yes**: Converts images in the folder **and** all subfolders

This is useful for projects with organized folder structures like `/products/category1/`, `/products/category2/`, etc.

## 🐛 Error Handling

The script includes robust error handling:
- Invalid file paths are detected and reported
- Unsupported image formats are skipped
- Conversion errors are logged without stopping batch processing
- File size calculations handle large files correctly

## 📝 Supported Formats

**Input formats:**
- PNG (.png)
- JPEG (.jpg, .jpeg)

**Output format:**
- WebP (.webp)

**Special features:**
- Preserves transparency from PNG images
- Automatically converts color modes for compatibility

## 🌐 Use Cases

- **E-commerce websites**: Reduce product image sizes for faster loading
- **Blogs and media sites**: Optimize photos and graphics
- **Portfolio websites**: Maintain quality while improving performance
- **Mobile applications**: Reduce bandwidth usage for image-heavy apps

## 📊 Performance Benefits

WebP offers significant advantages over traditional formats:
- **25-35% smaller file sizes** compared to JPEG
- **Faster page load times** improving user experience
- **Better Core Web Vitals scores** for SEO
- **Reduced bandwidth costs** for high-traffic websites

---

**Made with ❤️ for better web performance**
```
