import argparse
from PIL import Image
import os
import io
import sys

def resize_and_compress_to_pdf(input_path, output_pdf, scale=0.8, compress_quality=None):
    images = []

    # Check if input is a folder or a single file
    if os.path.isdir(input_path):
        files = sorted([
            os.path.join(input_path, f)
            for f in os.listdir(input_path)
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ])
    elif os.path.isfile(input_path) and input_path.lower().endswith((".jpg", ".jpeg", ".png")):
        files = [input_path]
    else:
        print("❌ Invalid input! Must be a folder or an image file (.jpg/.jpeg/.png).")
        sys.exit(1)

    if not files:
        print("❌ No image files found.")
        return

    for path in files:
        filename = os.path.basename(path)
        img = Image.open(path)

        # Resize image
        w, h = img.size
        new_size = (int(w * scale), int(h * scale))
        img = img.resize(new_size, Image.LANCZOS)

        # Ensure RGB mode (PDF does not support RGBA)
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Save image to memory buffer with or without compression
        buffer = io.BytesIO()
        quality = compress_quality if compress_quality else 95
        img.save(buffer, format="JPEG", quality=quality, optimize=True)
        buffer.seek(0)

        # Reopen the compressed image
        img_compressed = Image.open(buffer)
        images.append(img_compressed)

        print(f"✅ {filename} -> resized {new_size}, quality={quality}")

    # Save all images as a single PDF
    first_image = images[0]
    other_images = images[1:]
    first_image.save(
        output_pdf,
        save_all=True,
        append_images=other_images,
        quality=compress_quality if compress_quality else 95,
        optimize=True,
    )

    print(f"\n📄 PDF successfully created: {output_pdf}")

def main():
    parser = argparse.ArgumentParser(
        description="Resize and optionally compress image(s) into a single PDF file. Supports both folder and single-file input."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to the input image file or folder.")
    parser.add_argument("-o", "--output", required=True, help="Name of the output PDF file.")
    parser.add_argument("-s", "--scale", type=float, default=0.8, help="Resize scale factor (default: 0.8).")
    parser.add_argument("-c", "--compress", type=int, help="JPEG compression quality (1–100). If omitted, compression is disabled (quality=95).")

    args = parser.parse_args()

    if args.compress is not None and not (1 <= args.compress <= 100):
        print("❌ Compression quality (-c) must be between 1 and 100.")
        sys.exit(1)

    print(f"\n📂 Input: {args.input}")
    print(f"📤 Output: {args.output}")
    print(f"🔍 Scale: {args.scale}")
    if args.compress:
        print(f"🗜️ Compression: Enabled (quality={args.compress})\n")
    else:
        print("🗜️ Compression: Disabled (quality=95)\n")

    resize_and_compress_to_pdf(
        input_path=args.input,
        output_pdf=args.output,
        scale=args.scale,
        compress_quality=args.compress
    )

if __name__ == "__main__":
    main()
