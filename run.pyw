from tkinter import *

from PIL import ImageTk,Image  

root = Tk()
root.title('')

icon = PhotoImage(height=1, width=1)
icon.blank()

canvas = Canvas(root, width=340, height=490)
canvas.pack()
img= (Image.open("unknown.png"))
resized_image = img.resize((368,490), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(10, 10, anchor=NW, image=new_image)


def disable_event():
    pass


# Disable the Close Window Control Icon
root.protocol("WM_DELETE_WINDOW", disable_event)
# root.overrideredirect(True)
root.tk.call('wm', 'iconphoto', root._w, icon)
root.mainloop()
