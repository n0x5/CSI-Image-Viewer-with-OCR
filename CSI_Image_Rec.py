import PIL.Image
import PIL.ImageTk
import pytesseract
from tkinter import *
import os
import argparse
from mss import mss

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

pytesseract.pytesseract.tesseract_cmd  = os.path.join(os.path.dirname(__file__), 'Tesseract-OCR', 'tesseract.exe')
image2 = args.filename
size = 500, 500

image_load = PIL.Image.open(image2)
image_load_resize = PIL.Image.open(image2)
image_load_resize.thumbnail(size, PIL.Image.ANTIALIAS)
img_text = pytesseract.image_to_string(image_load)

window = Tk()
window.title("Image Rec CSI level")
window.geometry("1000x900")

windowBackground = '#E3DCA8'

window.configure(bg=windowBackground)

instruction = Label(text='Image Rec CSI level', bg=windowBackground)
instruction.place(x=115, y=10)

img = PIL.ImageTk.PhotoImage(image_load_resize)
text1 = Label(image = img, width=400)
text1.pack(side=LEFT)
text2 = Text( width=300)
text2.pack(side=RIGHT)
text2.insert('1.0', img_text)
scrollbar = Scrollbar(text2, orient='vertical', command=text2.yview)
text2['yscrollcommand'] = scrollbar.set
scrollbar.place(x=500, y=10, height=500)

def save_single():
    with open(image2+'.txt', 'w') as img_file:
        img_file.write(img_text)

def save_dir():
    endpoint1 = os.path.split(image2)
    endpoint = endpoint1[0]
    for subdir, dirs, files in os.walk(endpoint):
        for fn in files:
            file2 = os.path.join(subdir, fn)
            try:
                if not os.path.isfile(file2+'.txt'):
                    image_load3 = PIL.Image.open(file2)
                    img_text3 = pytesseract.image_to_string(image_load3)
                    with open(file2+'.txt', 'w') as img_file2:
                        img_file2.write(img_text3)
            except Exception:
                pass
            
# the screenshot works but doesn't load in view atm for some reason
def screenshot(text1, text2):
    window.iconify()
    with mss() as sct:
        screen = sct.shot()
        screen2 = sct.shot()
        image_load_screen = PIL.Image.open(screen)
        img_text_screen = pytesseract.image_to_string(image_load_screen)
        text1.forget()
        image_load_resize_screen = PIL.Image.open(screen2)
        img_screen = PIL.ImageTk.PhotoImage(image_load_resize_screen)
        text1 = Label(image = img_screen, width=400)
        text1.pack(side=LEFT)
        text2.forget()
        text2 = Text( width=300)
        text2.pack(side=RIGHT)
        text2.insert('1.0', img_text_screen)
        scrollbar = Scrollbar(text2, orient='vertical', command=text2.yview)
        text2['yscrollcommand'] = scrollbar.set
        scrollbar.place(x=500, y=10, height=500)
    window.deiconify()

button_single = Button(window, text="Save text to .csi file", command=save_single,  width = '30', height = '4')
button_all = Button(window, text="Scan all images in directory and save", command=save_dir,  width = '30', height = '4')
button_screenshot = Button(window, text="Screenshot & OCR", command= lambda: screenshot(text1, text2), width = '30', height = '4')

button_single.place(x=20, y=800)
button_all.place(x=300, y=800)
button_screenshot.place(x=600, y=800)

window.mainloop()
