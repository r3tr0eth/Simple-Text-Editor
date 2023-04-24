# Importar el módulo tkinter
import tkinter as tk
from tkinter import filedialog, messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Editor de texto básico")

# Crear el cuadro de texto donde se escribirá el texto
text = tk.Text(root)
text.pack(expand=True, fill="both")

# Crear una variable para almacenar el nombre del archivo
filename = ""

# Definir las funciones para los comandos del menú
def new_file():
    # Crear un nuevo archivo vacío
    global filename
    filename = ""
    text.delete(1.0, "end")

def open_file():
    # Abrir un archivo existente
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if filename:
        text.delete(1.0, "end")
        with open(filename, "r") as f:
            text.insert(1.0, f.read())

def save_file():
    # Guardar el archivo actual
    global filename
    if filename:
        with open(filename, "w") as f:
            f.write(text.get(1.0, "end"))
    else:
        save_as_file()

def save_as_file():
    # Guardar el archivo con un nuevo nombre
    global filename
    filename = filedialog.asksaveasfilename(filetypes=[("Archivos de texto", "*.txt")], defaultextension=".txt")
    if filename:
        with open(filename, "w") as f:
            f.write(text.get(1.0, "end"))

def exit_app():
    # Salir de la aplicación
    if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
        root.destroy()

def count_words():
    # Contar el número de palabras en el texto
    text_content = text.get(1.0, "end")
    words = text_content.split()
    num_words = len(words)
    messagebox.showinfo("Contador de palabras", f"El texto tiene {num_words} palabras.")

def count_chars():
    # Contar el número de caracteres en el texto
    text_content = text.get(1.0, "end")
    num_chars = len(text_content) - 1 # Se resta 1 por el caracter final \n
    messagebox.showinfo("Contador de caracteres", f"El texto tiene {num_chars} caracteres.")

def count_lines():
    # Contar el número de líneas en el texto
    text_content = text.get(1.0, "end")
    lines = text_content.split("\n")
    num_lines = len(lines) - 1 # Se resta 1 por la línea vacía final
    messagebox.showinfo("Contador de líneas", f"El texto tiene {num_lines} líneas.")

# Crear el menú principal
menu = tk.Menu(root)
root.config(menu=menu)

# Crear el menú archivo con sus opciones
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_command(label="Guardar como", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_app)

# Crear el menú editar con sus opciones
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Contar palabras", command=count_words)
edit_menu.add_command(label="Contar caracteres", command=count_chars)
edit_menu.add_command(label="Contar líneas", command=count_lines)

# Iniciar el bucle principal de la aplicación
root.mainloop()