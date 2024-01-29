import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Basic Image Viewer")

# Function to open an image file
def open_image():
    file_path = filedialog.askopenfilename(initialdir="./images", title="Select an Image", filetypes=(("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All Files", "*.*")))
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

# Create and configure a label to display the image
label = tk.Label(root)
label.pack()

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Add an "Open" option to the menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open Image", command=open_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Run the application
root.mainloop()
