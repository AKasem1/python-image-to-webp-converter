from PIL import Image
import os
from pathlib import Path

def convert_to_webp(input_path, output_path=None, quality=85):
    """
    Convert PNG/JPG/JPEG image to WebP format
    
    Args:
        input_path: Path to the input image
        output_path: Path for output file (optional, auto-generated if not provided)
        quality: WebP quality level (0-100), lower = smaller file size
    """
    try:
        # Open the image
        image = Image.open(input_path)
        
        # Convert to RGB mode if necessary (WebP doesn't support all modes)
        if image.mode in ("RGBA", "LA", "P"):
            # Keep transparency for RGBA
            pass
        else:
            image = image.convert('RGB')
        
        # Generate output path from input path if not provided
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.webp'
        
        # Save as WebP with quality settings
        image.save(output_path, 'webp', quality=quality, optimize=True)
        
        # Calculate file size reduction
        original_size = os.path.getsize(input_path)
        webp_size = os.path.getsize(output_path)
        reduction = ((original_size - webp_size) / original_size) * 100
        
        print(f"✓ Converted: {input_path} -> {output_path}")
        print(f"  Size: {original_size:,} bytes -> {webp_size:,} bytes ({reduction:.1f}% reduction)")
        
        return True
    except Exception as e:
        print(f"✗ Error converting {input_path}: {str(e)}")
        return False

def batch_convert(directory, output_dir=None, quality=85, recursive=False):
    """
    Convert all PNG/JPG/JPEG images in a directory to WebP
    
    Args:
        directory: Input directory path
        output_dir: Output directory (optional, uses input directory if not provided)
        quality: WebP quality level (0-100)
        recursive: Process subdirectories if True
    """
    supported_formats = ('.png', '.jpg', '.jpeg')
    pattern = '**/*' if recursive else '*'
    
    # Create output directory if specified
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    converted = 0
    failed = 0
    
    # Find all image files
    for file_path in Path(directory).glob(pattern):
        if file_path.suffix.lower() in supported_formats:
            # Determine output path
            if output_dir:
                output_path = os.path.join(output_dir, file_path.stem + '.webp')
            else:
                output_path = file_path.with_suffix('.webp')
            
            if convert_to_webp(str(file_path), str(output_path), quality):
                converted += 1
            else:
                failed += 1
    
    print(f"\n{'='*50}")
    print(f"Conversion complete: {converted} successful, {failed} failed")

if __name__ == "__main__":
    print("=" * 50)
    print("Image to WebP Converter")
    print("=" * 50)
    
    # Get conversion type
    print("\nConversion options:")
    print("1. Convert single file")
    print("2. Convert all images in a directory")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    if choice == "1":
        # Single file conversion
        input_path = input("Enter image path (PNG/JPG/JPEG): ").strip()
        
        if not os.path.isfile(input_path):
            print(f"Error: '{input_path}' is not a valid file")
        else:
            quality_input = input("Enter quality (0-100, default 85): ").strip()
            quality = int(quality_input) if quality_input else 85
            
            output_path_input = input("Enter output path (press Enter to auto-generate): ").strip()
            output_path = output_path_input if output_path_input else None
            
            convert_to_webp(input_path, output_path, quality)
    
    elif choice == "2":
        # Batch conversion
        directory = input("Enter directory path: ").strip()
        
        if not os.path.isdir(directory):
            print(f"Error: '{directory}' is not a valid directory")
        else:
            output_dir_input = input("Enter output directory (press Enter to use same directory): ").strip()
            output_dir = output_dir_input if output_dir_input else None
            
            quality_input = input("Enter quality (0-100, default 85): ").strip()
            quality = int(quality_input) if quality_input else 85
            
            recursive_input = input("Process subdirectories? (y/n, default n): ").strip().lower()
            recursive = recursive_input == 'y'
            
            batch_convert(directory, output_dir, quality, recursive)
    
    else:
        print("Invalid choice. Please run the script again and select 1 or 2.")
