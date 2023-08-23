import tkinter as tk

app = tk.Tk()
app.title("Meta Invoice Renamer")
app.geometry("400x200")

# button to select a directory
select_button = tk.Button(app, text="Select Directory")
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


app.mainloop()
