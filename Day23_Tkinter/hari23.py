import tkinter as tk

# def on_click():
#     label2.config(text=f'Hallo, {entry.get()}')
#
# root = tk.Tk()
# root.title("Basic Calculator")
# root.geometry("300x300")
# # Label
#
# label1 = tk.Label(root, text="Hello, Welcome to Basic Calculator")
# label1.pack(padx=5, pady=5)
#
# # Entry
# entry = tk.Entry(root)
# entry.pack(padx=5, pady=5)
#
# # Button
# button = tk.Button(root, text="Save", command=on_click)
# button.pack(padx=5, pady=5)
#
# label2 = tk.Label(root, text="")
# label2.pack(padx=5, pady=5)
#
# root.mainloop()

def penjumlahan():
    try:
        nilai1 = float(entry1.get())
        nilai2 = float(entry2.get())
        hasil_sum = nilai1 + nilai2
        label.config(text=f'Hasil nya adalah : {hasil_sum}')
    except ValueError:
        label.config(text="Please enter numeric values")
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)


root = tk.Tk()
root.geometry("300x300")
root.title("Calculator Penjumlahan")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

button = tk.Button(root, text="+", command=penjumlahan)
button.grid(row=2, column=1)

label = tk.Label(root, text="")
label.grid(row=3, column=1)

root.mainloop()
