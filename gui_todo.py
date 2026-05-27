import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


# =========================
# LOAD TASKS
# =========================
def load_tasks():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# =========================
# SAVE TASKS
# =========================
def save_tasks():

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# =========================
# UPDATE LISTBOX
# =========================
def update_listbox():

    listbox.delete(0, tk.END)

    for task in tasks:

        status = "✓" if task["done"] else "✗"

        display = f"[{status}] {task['title']}"

        listbox.insert(tk.END, display)


# =========================
# ADD TASK
# =========================
def add_task():

    title = entry.get()

    if title == "":
        messagebox.showwarning("Warning", "Tugas tidak boleh kosong!")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)

    save_tasks()

    update_listbox()

    entry.delete(0, tk.END)


# =========================
# DELETE TASK
# =========================
def delete_task():

    try:

        selected = listbox.curselection()[0]

        tasks.pop(selected)

        save_tasks()

        update_listbox()

    except:
        messagebox.showwarning("Warning", "Pilih tugas dulu!")


# =========================
# COMPLETE TASK
# =========================
def complete_task():

    try:

        selected = listbox.curselection()[0]

        tasks[selected]["done"] = True

        save_tasks()

        update_listbox()

    except:
        messagebox.showwarning("Warning", "Pilih tugas dulu!")


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()

root.title("To-Do List App")

root.geometry("500x500")

root.config(bg="#1e1e1e")


# =========================
# TASK STORAGE
# =========================
tasks = load_tasks()


# =========================
# TITLE
# =========================
title = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title.pack(pady=10)


# =========================
# ENTRY
# =========================
entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)

entry.pack(pady=10)


# =========================
# BUTTON FRAME
# =========================
button_frame = tk.Frame(root, bg="#1e1e1e")

button_frame.pack(pady=10)


# ADD BUTTON
add_btn = tk.Button(
    button_frame,
    text="Tambah",
    width=12,
    command=add_task
)

add_btn.grid(row=0, column=0, padx=5)


# COMPLETE BUTTON
complete_btn = tk.Button(
    button_frame,
    text="Selesai",
    width=12,
    command=complete_task
)

complete_btn.grid(row=0, column=1, padx=5)


# DELETE BUTTON
delete_btn = tk.Button(
    button_frame,
    text="Hapus",
    width=12,
    command=delete_task
)

delete_btn.grid(row=0, column=2, padx=5)


# =========================
# LISTBOX
# =========================
listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=15
)

listbox.pack(pady=20)


# =========================
# FIRST LOAD
# =========================
update_listbox()


# =========================
# RUN APP
# =========================
root.mainloop()