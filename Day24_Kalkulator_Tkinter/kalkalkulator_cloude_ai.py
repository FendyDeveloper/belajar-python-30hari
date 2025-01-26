import tkinter as tk
from tkinter import ttk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        # Warna tema
        self.PRIMARY_COLOR = "#2C3E50"  # Warna background utama
        self.LIGHT_BLUE = "#3498DB"  # Warna tombol operasi
        self.DARK_GRAY = "#34495E"  # Warna tombol angka
        self.WHITE = "#ECF0F1"  # Warna text
        self.ORANGE = "#E67E22"  # Warna tombol equals

        self.root.configure(bg=self.PRIMARY_COLOR)

        # Variabel untuk menyimpan perhitungan
        self.current = ""
        self.expression = ""

        # Membuat display
        self.create_display()

        # Membuat tombol
        self.create_buttons()

    def create_display(self):
        # Frame untuk display
        display_frame = tk.Frame(self.root, bg=self.PRIMARY_COLOR)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Label untuk menampilkan expression
        self.expression_label = tk.Label(
            display_frame,
            text="",
            font=("Arial", 14),
            bg=self.PRIMARY_COLOR,
            fg=self.WHITE,
            anchor="e",
            wraplength=320
        )
        self.expression_label.pack(expand=True, fill="both")

        # Label untuk menampilkan hasil
        self.result_label = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 30, "bold"),
            bg=self.PRIMARY_COLOR,
            fg=self.WHITE,
            anchor="e",
            wraplength=320
        )
        self.result_label.pack(expand=True, fill="both")

    def create_buttons(self):
        # Frame untuk tombol
        button_frame = tk.Frame(self.root, bg=self.PRIMARY_COLOR)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Konfigurasi grid
        button_frame.columnconfigure((0, 1, 2, 3), weight=1)
        button_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Daftar tombol
        buttons = [
            ('C', 0, 0, self.LIGHT_BLUE), ('±', 0, 1, self.LIGHT_BLUE),
            ('%', 0, 2, self.LIGHT_BLUE), ('÷', 0, 3, self.LIGHT_BLUE),
            ('7', 1, 0, self.DARK_GRAY), ('8', 1, 1, self.DARK_GRAY),
            ('9', 1, 2, self.DARK_GRAY), ('×', 1, 3, self.LIGHT_BLUE),
            ('4', 2, 0, self.DARK_GRAY), ('5', 2, 1, self.DARK_GRAY),
            ('6', 2, 2, self.DARK_GRAY), ('-', 2, 3, self.LIGHT_BLUE),
            ('1', 3, 0, self.DARK_GRAY), ('2', 3, 1, self.DARK_GRAY),
            ('3', 3, 2, self.DARK_GRAY), ('+', 3, 3, self.LIGHT_BLUE),
            ('0', 4, 0, self.DARK_GRAY, 2), ('.', 4, 2, self.DARK_GRAY),
            ('=', 4, 3, self.ORANGE)
        ]

        # Membuat tombol
        for button in buttons:
            if len(button) == 5:  # Tombol dengan colspan
                self.create_button(button_frame, button[0], button[1], button[2], button[3], colspan=button[4])
            else:
                self.create_button(button_frame, button[0], button[1], button[2], button[3])

    def create_button(self, parent, text, row, col, bg_color, colspan=1):
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 16, "bold"),
            bg=bg_color,
            fg=self.WHITE,
            border=0,
            borderwidth=0,
            command=lambda: self.button_click(text)
        )
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

        # Hover effect
        button.bind("<Enter>", lambda e: e.widget.configure(bg=self.lighten_color(bg_color)))
        button.bind("<Leave>", lambda e: e.widget.configure(bg=bg_color))

    def button_click(self, value):
        if value == "C":
            self.current = ""
            self.expression = ""
        elif value == "±":
            if self.current and self.current != "0":
                if self.current[0] == "-":
                    self.current = self.current[1:]
                else:
                    self.current = "-" + self.current
        elif value == "%":
            if self.current:
                self.current = str(float(self.current) / 100)
        elif value == "=":
            self.calculate_result()
            self.expression = ""
        else:
            if value in "+-×÷":
                if self.current:
                    self.expression += self.current + " " + value.replace("×", "*").replace("÷", "/") + " "
                    self.current = ""
            else:
                self.current += value

        self.update_display()

    def calculate_result(self):
        try:
            expression = self.expression + self.current
            expression = expression.replace("×", "*").replace("÷", "/")
            self.current = str(eval(expression))
        except:
            self.current = "Error"

    def update_display(self):
        self.expression_label.config(text=self.expression)
        self.result_label.config(text=self.current if self.current else "0")

    def lighten_color(self, color):
        # Fungsi untuk membuat warna lebih terang saat hover
        rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
        rgb = tuple(min(255, c + 20) for c in rgb)
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()