import sys
from exif import Image

if len(sys.argv) != 2:
    print("Provide proper image path")
    sys.exit()


img_path = sys.argv[1]

with open(img_path, 'rb') as img_file: # read file
    img = Image(img_file)

img.artist = "Manus"  # assign value to a tag

# save
with open('new_file.jpg', 'wb') as save_file:
    save_file.write(img.get_file())
