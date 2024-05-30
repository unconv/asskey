#!/usr/bin/env python3

from openai import OpenAI
from dotenv import load_dotenv
import base64
import sys
import os

from image_to_ascii import save_ascii_art, create_ascii_art

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def create_image(prompt, output_image):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        response_format="b64_json",
    )

    image = base64.b64decode(response.data[0].b64_json)

    with open(output_image, "wb") as f:
        f.write(image)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <output_file> <prompt>")
        sys.exit(1)

    output_file = sys.argv[1]
    prompt = sys.argv[2]

    dalle_file = output_file+".dalle.webp"

    create_image(prompt, dalle_file)
    print(f"Dall-e image saved to {dalle_file}")

    ascii_art = create_ascii_art(dalle_file)
    save_ascii_art(ascii_art, output_file)
    print(f"ASCII art saved to {output_file}")
