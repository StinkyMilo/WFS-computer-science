import pyautogui as autopy
# Must use this: chrome://dino
top_left_pos = (350,256+295)
bottom_right_pos = (500,256+295+70)
region_size = (bottom_right_pos[0]-top_left_pos[0],bottom_right_pos[1]-top_left_pos[1])
# Black pixel (326, 664)
jump_pixel = (70,69)
duck_pixel = (50,0)
interval = 4
white = (255,255,255)
black = (0,0,0)
reference_pixel = (0,0)
debug_mode = True
keydown_frames = 0
max_keydown_frames = 4
holding = False
im = autopy.screenshot(region=(top_left_pos[0], top_left_pos[1], region_size[0], region_size[1]))
def point_add(tuple1,tuple2):
    return tuple1[0]+tuple2[0],tuple1[1]+tuple2[1]

def point_sub(tuple1,tuple2):
    return tuple1[0]-tuple2[0],tuple1[1]-tuple2[1]

def get_pixel(image,pos):
    return image.getpixel(pos)


while True:
    # print(point_sub(autopy.position(),top_left_pos))
    im = autopy.screenshot(region=(top_left_pos[0],top_left_pos[1],region_size[0],region_size[1]))
    if holding:
        if keydown_frames<=0:
            holding=False
            autopy.keyUp("down")
        else:
            keydown_frames-=1
    do_press = False
    ref_pixel = get_pixel(im,reference_pixel)
    for i in range(duck_pixel[0], 0, -interval):
        bird_pixel = get_pixel(im, (i, duck_pixel[1]))
        if bird_pixel != ref_pixel:
            autopy.keyDown("down")
            holding = True
            keydown_frames = max_keydown_frames
            break
    if not holding:
        for i in range(jump_pixel[0],0,-interval):
            cactus_pixel = get_pixel(im,(i,jump_pixel[1]))
            if cactus_pixel != ref_pixel:
                do_press=True
                autopy.press("up")
                break