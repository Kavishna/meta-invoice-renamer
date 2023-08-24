import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from PyPDF2 import PdfReader, PdfWriter
import os
import re


def extract_ref_number(pdf_path):
    # reguler expression finds text start with 'Reference Number:'
    ref_pattern = r"Reference Number: ([A-Z0-9]+)"

    with open(pdf_path, "rb") as pdf_file:
        reader = PdfReader(pdf_file)
        page = reader.pages[0]  # get first page of pdf
        text = page.extract_text()  # convert first page into string

        match = re.search(ref_pattern, text)  # find the pattern
        if match:
            ref_number = match.group(1)
            return ref_number

    return None

# function extracts a reference number if it's present; otherwise, it returns "none".


def extract_ref_number(pdf_path):
    # reguler expression finds text start with 'Reference Number:'
    ref_pattern = r"Reference Number: ([A-Z0-9]+)"

    with open(pdf_path, "rb") as pdf_file:
        reader = PdfReader(pdf_file)
        page = reader.pages[0]  # get first page of pdf
        text = page.extract_text()  # convert first page into string

        match = re.search(ref_pattern, text)  # find the pattern
        if match:
            ref_number = match.group(1)
            return ref_number

    return None


def update_file_count(directory):
    # finds pdf files
    pdf_files = [file for file in os.listdir(
        directory) if file.lower().endswith(".pdf")]

    if pdf_files:
        # if pdf files are found enable rename button
        rename_button.config(state="normal")

        file_count_message = "1 pdf is found" if len(
            pdf_files) == 1 else f"{len(pdf_files)} pdf's are found"

        # update the file count
        file_count_label.config(
            text=file_count_message, fg='white')
        return

    if not pdf_files:  # if pdf files are not found
        rename_button.config(state='disabled')  # disable the rename button
        messagebox.showwarning(
            "No PDFs", "No PDF files found in the selected directory.")  # show a warning
        file_count_label.config(
            text="No PDF files.", fg='red')  # set the file count lable


def select_directory():
    # prompt file directory
    directory_path = filedialog.askdirectory(title="Select a Directory")
    if directory_path:
        update_file_count(directory_path)
        selected_directory_label.config(
            text=f"Selected Directory: {directory_path}")
        app.selected_directory = directory_path  # Store the selected directory


app = tk.Tk()
app.title("Meta Invoice Renamer")
app.geometry("400x200")

# button to select a directory
select_button = tk.Button(app, text="Select Directory",
                          command=select_directory)
select_button.pack(pady=20)

# lable shows directory path
selected_directory_label = tk.Label(
    app, text="Selected Directory: None", fg='yellow')
selected_directory_label.pack()

# lable shows pdf file count
file_count_label = tk.Label(app, text="No selected directory")
file_count_label.pack()

# rename button
rename_button = tk.Button(app, text="Rename", state='disabled')
rename_button.pack(pady=5)

# Initialize the selected directory
app.selected_directory = None

app.mainloop()
