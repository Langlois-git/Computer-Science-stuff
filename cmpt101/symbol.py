from PIL import Image

picture = Image.open("circle.png")

width, height = picture.size

for x in range(width):
    for y in range(height):
        if picture.getpixel((x,y)) == (0, 255, 0):
            picture.putpixel((x,y), (0, 0, 0))

picture.show()
