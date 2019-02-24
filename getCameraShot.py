# coding: utf8

import tkinter as tk
import os
import shutil
import time
import cv2
import lib.kmtz_obj as kmtz_obj
from matplotlib import pyplot as plt
from PIL import ImageTk, Image

def btnGetPhoto(kmtz_obj):

    kmtz_obj.current_img_dir = os.getcwd() + "\\IMG\\" + time.strftime("%d.%m.%Y-%H.%M.%S")
    kmtz_obj.takePhoto()
    kmtz.getCamImage(debug)

    img_left  = ImageTk.PhotoImage(Image.open(kmtz.left_pic_local).resize((512, 368), Image.ANTIALIAS))
    img_right = ImageTk.PhotoImage(Image.open(kmtz.right_pic_local).resize((512, 368), Image.ANTIALIAS))

    img_left_panel.config(image=img_left)
    img_left_panel.image = img_left

    img_right_panel.config(image=img_right)
    img_right_panel.image = img_right

def btnDelPhoto(kmtz_obj):
    shutil.rmtree(kmtz_obj.current_img_dir)
    kmtz_obj.current_img_dir = ""
    print("Remove dir: " + kmtz_obj.current_img_dir)

def btnRotate(kmtz_obj):
    deg_start = int(deg_start_scale.get())
    deg_stop  = int(deg_stop_scale.get())

    kmtz.srvMotorPwrEn(1)
    kmtz.rotateHeadSlow(deg_start, deg_stop, 2)

# CONFIGURATION
kmtz      = kmtz_obj.KMTZ()
debug     = 1

# Show image in the GUI

window = tk.Tk()
window.title("GetCameraShot")
window.configure(background='grey')
window.resizable(width=False, height=False)

# img frame
img_frame = tk.Frame()

img_left  = tk.PhotoImage(width=512, height=384)
img_right = tk.PhotoImage(width=512, height=384)

# left image
img_left_panel = tk.Label(img_frame, image=img_left, bg="white")
img_left_panel.pack(side="left")

# right image
img_right_panel = tk.Label(img_frame, image=img_right, bg="white")
img_right_panel.pack(side="left")

img_frame.pack()

# btn frame
btn_frame = tk.Frame(bd=5)

# for button size in pixels
pixel = tk.PhotoImage(width=1, height=1)

btn_get = tk.Button(
    btn_frame,
    image=pixel,
    text=u"Новый снимок",
    compound="c",
    command= lambda: btnGetPhoto(kmtz),
    bd=3, width=501,height=50)
btn_get.pack()

btn_rotate = tk.Button(
    btn_frame,
    image=pixel,
    text=u"Повернуть",
    compound="c",
    command= lambda: btnRotate(kmtz),
    bd=3, width=501,height=50)
btn_rotate.pack()

btn_del = tk.Button(
    btn_frame,
    image=pixel,
    text=u"Удалить",
    compound="c",
    command= lambda: btnDelPhoto(kmtz),
    bd=3, width=501,height=50)
btn_del.pack()

btn_frame.pack(side="left")

scale_frame = tk.Frame(bd=5)

deg_start_frame = tk.Frame(scale_frame)
deg_start_label = tk.Label(deg_start_frame, image=pixel, text=u"Начальная позиция", height=23, compound="c")
deg_start_label.pack()
deg_start_scale = tk.Scale(deg_start_frame, orient=tk.HORIZONTAL,length=495,from_=0,to=360,tickinterval=50, resolution=5)
deg_start_scale.pack()
deg_start_frame.pack()

deg_stop_frame = tk.Frame(scale_frame)
deg_stop_label = tk.Label(deg_stop_frame, image=pixel, text=u"Конечная позиция", height=23, compound="c")
deg_stop_label.pack()
deg_stop_scale = tk.Scale(deg_stop_frame, orient=tk.HORIZONTAL,length=495,from_=0,to=360,tickinterval=50, resolution=5)
deg_stop_scale.pack()
deg_stop_frame.pack()

scale_frame.pack(side="left")

#Start the GUI
window.mainloop()
