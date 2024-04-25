# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L9Q1dl.py
# ------------------------------------
# Purpose: This program will analyze a picture of a stop sign and correct visual artifcats of the picture

from PIL import Image

def fix_file(file_name):
    """This function defines the programs logic"""

    picture = Image.open(file_name)
    fix_middle(picture)
    fix_top_half(picture)
    make_rect_varyh(picture)
    picture.show()

def fix_middle(picture):
    """This function swaps the the red and green components of each pixel in the middle section"""

    middle_boundary_left = picture.width // 4
    middle_boundary_right = picture.width * 3 // 4

    for x in range(middle_boundary_left, middle_boundary_right):
        for y in range(picture.height):
            r, g, b = picture.getpixel((x,y))
            picture.putpixel((x,y), (g, r, b))

def fix_top_half(picture):
    """This function turns every yellow pixel into a white pixel for the top half of the picture"""

    center_boundary = picture.height // 2

    for x in range(picture.width):
        for y in range(center_boundary+1):
            if picture.getpixel((x,y)) == (255, 255, 0):
                picture.putpixel((x,y), (255, 255, 255))

def make_rect_varyh(picture):
    """This function generates a rectangular color gradient from black to blue on top of the picture"""

    rect_ulc_x = picture.width//10
    rect_ulc_y = picture.height*7 //10
    rectangle_height = picture.height // 20 
    rectangle_width = picture.width*8 // 10
    gradiant_interval = rectangle_width // 255
    b = 0

    for x in range(rect_ulc_x, rect_ulc_x+rectangle_width+1):
        for y in range(rect_ulc_y, rect_ulc_y+rectangle_height+1):
            picture.putpixel((x,y), (0, 0, b))
        if x % gradiant_interval == 0:
            b += 1



            

fix_file("stop_colored.png")


