#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create a 32x32 image with transparent background
size = 32
img = Image.new('RGBA', (size, size), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw rounded rectangle for black background
radius = 6
draw.rounded_rectangle([(0, 0), (size, size)], radius=radius, fill='black')

# Try to use bold fonts
font_paths = [
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',  # macOS Bold
    '/Library/Fonts/Arial Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',  # Linux
    'C:\\Windows\\Fonts\\arialbd.ttf',  # Windows Bold
]

font = None
for font_path in font_paths:
    if os.path.exists(font_path):
        try:
            font = ImageFont.truetype(font_path, 24)
            break
        except:
            continue

# If no font found, use default
if font is None:
    font = ImageFont.load_default()

# Get text bounding box to center it
text = "D"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Calculate position to center the text properly
# Account for the bbox offsets to get true centering
x = (size - text_width) // 2 - bbox[0] + 1  # Move slightly right
y = (size - text_height) // 2 - bbox[1]

# Draw the white "D"
draw.text((x, y), text, fill='white', font=font)

# Save as ICO
img.save('images/d.ico', format='ICO')
print("Created images/d.ico successfully!")
