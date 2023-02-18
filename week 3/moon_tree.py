
from draw2d import start_drawing, draw_oval, draw_line, draw_text, finish_drawing,draw_arc,draw_rectangle, draw_polygon
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_moon(canvas,700,400,)
    draw_cloud(canvas,scene_width,scene_height)
    draw_less_cloud(canvas,scene_width,scene_height)
    draw_pine_tree(canvas, 500, 150, 250)
    draw_pine_tree(canvas, 400,150,200)
    draw_pine_tree(canvas, 450,100,150)
    draw_pine_tree(canvas, 525,125,100)
    draw_pine_tree(canvas, 550,100,50)
    draw_bird(canvas, 100, 305)
    draw_bird(canvas, 150, 311)
    draw_bird(canvas, 200, 317)
    draw_bird(canvas, 225, 333)
    draw_bird(canvas, 180, 320)
    draw_snow(canvas,scene_width,scene_height)
    draw_grid(canvas,scene_width, scene_height,50)

    
    #draw_pine_tree(canvas, tree_center_x,
    #        tree_bottom, tree_height)

    finish_drawing(canvas)

# Define your functions such as
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="lightsteelblue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")

def draw_pine_tree(canvas, center_x, bottom, height):
       # Draw a pine tree.
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    bottom_trunk=bottom
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left,bottom_trunk, trunk_right, trunk_top,
            outline="brown", width=1, fill="tan3")
       
    skirt_width = height / 2

    skirt_left = center_x - skirt_width / 2
    skirt_bottom=trunk_top
    skirt_height = height - trunk_height
    skirt_center=center_x
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, skirt_left, skirt_bottom,skirt_center,skirt_top,skirt_right,skirt_bottom,
    outline="green4", width=1, fill="dark green")
    
def draw_cloud(canvas, scene_width, scene_height):
    half_height = round(scene_height / 3)
    min_diam = 20
    max_diam = 40

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(200):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(scene_height - half_height, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="slategray", fill="slategray")

def draw_less_cloud(canvas, scene_width, scene_height):
    half_height = round(scene_height / 4)
    min_diam = 10
    max_diam = 20

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(scene_height - half_height, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="slategray", fill="slategray")
    
def draw_snow(canvas, scene_width, scene_height):
    half_height = round(scene_height / 1)
    min_diam = 1
    max_diam = 2

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(5000):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(scene_height - half_height, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="white", fill="white")

def draw_moon(canvas,x,y):  
    diameter = 100
    draw_oval(canvas, x, y, x + diameter, y + diameter, outline="linen", fill="linen")   

def draw_bird(canvas, x, y):
    draw_arc(canvas, x, y, x + 25, y + 15, start=0, extent=180,width=1, outline="black", fill="black")
    draw_arc(canvas, x + 25, y, x + 50, y + 15, start=0, extent=180,width=1, outline="black", fill="black")

def draw_grid(canvas, width, height, interval, color="black"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(0, width, interval):
        draw_line(canvas, x, 0, x, height, fill="black")
        draw_text(canvas, x, label_y, f"{x}", fill="black")

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill="black")
        draw_text(canvas, label_x, y, f"{y}", fill="black")
        # Call the main function so that
# this program will start executing.

main()