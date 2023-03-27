"""
USAGE: python exif_extractor.py image-path tag
"""

import sys
from exif import Image

img_path, tag = sys.argv[1:]

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

print(img.get(tag))
