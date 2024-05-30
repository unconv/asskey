#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import sys

def save_ascii_image(text, output_path, font_path=None, font_size=20, color=(255, 255, 255)):
    lines = text.split("\n")
    first_line = lines[0]
    width = int(len(first_line)*font_size*0.6)
    height = len(lines)*font_size

    # Create a blank image
    img = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Load a font
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.truetype("fonts/CourierPrime-Regular.ttf", font_size)

    # Draw the text
    draw.text((10, 10), text, fill=color, font=font)

    # Save the image
    img.save(output_path)

def create_ascii_art(image_path, ascii_chars=" .-~:+=*#%@", width=160):
    image = Image.open(image_path)
    height = int(width * image.height // image.width * 0.59)
    image = image.resize((width, height), Image.NEAREST)

    ascii_image = ""

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(gray / 256 * len(ascii_chars))
            ascii_image += ascii_chars[index]
        ascii_image += "\n"

    return ascii_image

def save_ascii_art(ascii_image, output_file):
    extension = output_file[-3:]

    if extension == "txt":
        with open(output_file, "w") as f:
            f.write(ascii_image)
    elif output_file == "-" or output_file == "stdout":
        print(ascii_image)
    else:
        save_ascii_image(ascii_image, output_file)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input_image> <output_file>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_file = sys.argv[2]

    ascii_image = create_ascii_art(input_image)

    save_ascii_art(ascii_image, output_file)
