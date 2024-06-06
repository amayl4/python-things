import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("My first GUI")

label = tk.Label(root, text="hello world", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

root.mainloop()