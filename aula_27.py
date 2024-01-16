import tkinter as tk
from tkinter import messagebox

def create_data():
    item = entry_data.get()
    if item:
        espace_list.insert(tk.END, item)
        espace_list.delete(0, item)

def read_data():
    selecao = espace_list.curselection()
    if selecao:
        item = espace_list.get(selecao)
        messagebox.showwarning('Dado: ', item)

def delete_data():
    selecao = espace_list.curselection()
    if selecao:
        espace_list.delete(selecao)

def update_data():
    selecao = espace_list.curselection()
    if selecao:
        new = entry_data.get()
    if new:
        espace_list.delete(selecao)
        espace_list.insert(selecao[0], new)
        espace_list.delete(0, tk.END)

root = tk.Tk()
root.title('CRUD')
root.geometry('200x450') 

label_titulo = tk.Label(root, text = 'CRUD BÁSICO EM PYTHON')
label_titulo.pack()

entry_data = tk.Entry(root)
entry_data.pack()

create_btn = tk.Button(root, text = 'create', command = create_data)
create_btn.pack()

read_btn = tk.Button(root, text = 'read', command = read_data)
read_btn.pack()

update_btn = tk.Button(root, text = 'update', command = update_data)
update_btn.pack()

delete_btn = tk.Button(root, text = 'delete', command = delete_data)
delete_btn.pack()

espace_list = tk.Listbox(root)
espace_list.pack()

root.mainloop()
