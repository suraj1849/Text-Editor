import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            text_editor.delete("1.0", tk.END)
            text_editor.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text_editor.get("1.0", tk.END))

def set_font_size(size):
    current_font = font.Font(text_editor, text_editor.cget("font"))
    text_editor.configure(font=(current_font.actual()['family'], size))

def set_font_style(style):
    current_font = font.Font(text_editor, text_editor.cget("font"))
    text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], style))

def set_bold():
    current_font = font.Font(text_editor, text_editor.cget("font"))
    if 'bold' in current_font.actual()['weight']:
        text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'normal'))
    else:
        text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'bold'))

def set_italic():
    current_font = font.Font(text_editor, text_editor.cget("font"))
    if 'italic' in current_font.actual()['slant']:
        text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'roman'))
    else:
        text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'italic'))

def set_underline():
    current_font = font.Font(text_editor, text_editor.cget("font"))
    if 'underline' in current_font.actual()['underline']:
        text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], current_font.actual()['weight'], current_font.actual()['slant']))
    else:
        text_editor.configure(font=(current_font.actual()['family'], current_font.actual()['size'], current_font.actual()['weight'], 'underline'))

def change_text_color():
    color = colorchooser.askcolor(title="Select Text Color")
    if color[1]:
        text_editor.configure(fg=color[1])

def about():
    messagebox.showinfo("About", "This is a simple text editor created using Python and Tkinter.")

root = tk.Tk()
root.title("Text Editor")

text_editor = tk.Text(root)
text_editor.pack()

# Toolbar
toolbar = tk.Frame(root)
toolbar.pack(fill=tk.X)

bold_button = tk.Button(toolbar, text="Bold", command=set_bold)
bold_button.pack(side=tk.LEFT, padx=5)

italic_button = tk.Button(toolbar, text="Italic", command=set_italic)
italic_button.pack(side=tk.LEFT, padx=5)

underline_button = tk.Button(toolbar, text="Underline", command=set_underline)
underline_button.pack(side=tk.LEFT, padx=5)

font_size_label = tk.Label(toolbar, text="Font Size:")
font_size_label.pack(side=tk.LEFT, padx=5)
font_size_entry = tk.Entry(toolbar, width=5)
font_size_entry.pack(side=tk.LEFT)

set_font_size_button = tk.Button(toolbar, text="Set", command=lambda: set_font_size(int(font_size_entry.get())))
set_font_size_button.pack(side=tk.LEFT, padx=5)

font_style_label = tk.Label(toolbar, text="Font Style:")
font_style_label.pack(side=tk.LEFT, padx=5)
font_style_entry = tk.Entry(toolbar, width=10)
font_style_entry.pack(side=tk.LEFT)

set_font_style_button = tk.Button(toolbar, text="Set", command=lambda: set_font_style(font_style_entry.get()))
set_font_style_button.pack(side=tk.LEFT, padx=5)

color_button = tk.Button(toolbar, text="Text Color", command=change_text_color)
color_button.pack(side=tk.LEFT, padx=5)

# Menu Bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Bold", command=set_bold)
format_menu.add_command(label="Italic", command=set_italic)
format_menu.add_command(label="Underline", command=set_underline)
format_menu.add_separator()
format_menu.add_command(label="Set Font Size", command=lambda: set_font_size(int(font_size_entry.get())))
format_menu.add_command(label="Set Font Style", command=lambda: set_font_style(font_style_entry.get()))
format_menu.add_separator()
format_menu.add_command(label="Text Color", command=change_text_color)
menu_bar.add_cascade(label="Format", menu=format_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Customizations
root.configure(bg="#f2f2f2")  # Set background color
toolbar.configure(bg="#f2f2f2")  # Set toolbar background color

bold_button.configure(bg="#f2f2f2", activebackground="#f2f2f2")  # Set button colors
italic_button.configure(bg="#f2f2f2", activebackground="#f2f2f2")
underline_button.configure(bg="#f2f2f2", activebackground="#f2f2f2")
set_font_size_button.configure(bg="#f2f2f2", activebackground="#f2f2f2")
set_font_style_button.configure(bg="#f2f2f2", activebackground="#f2f2f2")
color_button.configure(bg="#f2f2f2", activebackground="#f2f2f2")

font_size_label.configure(bg="#f2f2f2")  # Set label colors
font_style_label.configure(bg="#f2f2f2")

# Text Editor Customizations
text_editor.configure(bg="white", fg="black")  # Set text editor colors

root.mainloop()
