# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	F1Q5dl.py
# ------------------------------------
# Purpose:  The purpose of this program is to draw the brazillian flag

from PIL import Image, ImageDraw

# def draw_flag():
#     
#     symbol = Image.open("circle.png")
#     print(symbol.size)
#     picture = Image.new("RGB", (800, 560), (4, 156, 73))
#     draw=ImageDraw.Draw(picture)
#     draw.polygon([(50, 280), (400, 50), (750, 280), (400, 510),], (254, 224, 0), (254, 224, 0))
#     picture.paste(symbol, (249, 129))
#     sw, sh = symbol.size
#     return picture

# draw_flag().show()

def draw_picture():
    '''
    This function draws the background
    '''
    picture = Image.new("RGB", (800, 560), (4, 156, 73))
    draw=ImageDraw.Draw(picture)
    draw.polygon([(50, 280), (400, 50), (750, 280), (400, 510),], (254, 224, 0), (254, 224, 0))
    return picture
    
def draw_symbol():
    picture = Image.new("RGB", (800, 560), (0,255,0))
    symbol = Image.open("circle.png")
    picture.paste(symbol, (249, 129))
    return picture

def draw_flag():
    '''
    This function draws the flag
    '''
    picture = draw_picture()
    flag = draw_symbol()
    width, height = picture.size
    for y in range(height):
        for x in range(width):
            if flag.getpixel((x,y)) == (0, 255, 0):
                flag.putpixel((x,y), picture.getpixel((x,y)))
    return flag

def main():
    '''
    This function attempts to fix a visual artifacts in the png
    '''
    picture = draw_flag()
    draw=ImageDraw.Draw(picture)
    tester = Image.open("circle.png")
    print(tester.size)
    draw.ellipse([(249,129), (551,431)], None, (254, 244, 0))
    return picture

main().show()

