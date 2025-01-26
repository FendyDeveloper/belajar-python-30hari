import tkinter as tk

calculation = ''

root = tk.Tk()
root.geometry('300x520')
root.title('Kalkulator')

def calculate(symbol):
    global calculation
    calculation += str(symbol)
    print(f'calculation : {calculation}')
    print(f'symbol : {symbol}')
    if calculation != '':
        endcalculation = calculation[-1]
        not_double = '/+-'
        not_triple = '*'

        for cek_double in not_double:
            if endcalculation == cek_double:
                endcalculation = calculation[-2]
                if endcalculation == cek_double and symbol == cek_double:
                    calculation = calculation[:-1]

        for cek_triple in not_triple:
            if endcalculation == cek_triple:
                calculation = calculation[-3]
                if endcalculation == cek_triple and symbol == cek_triple:
                    calculation = calculation[:-1]
                    print(True)



    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)


def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0, tk.END)

def calculate_output():
    global calculation
    result = str(eval(calculation))
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, result)
    calculation = result

def parentheses():
    global calculation
    start_parentheses = calculation.count('(')
    end_parentheses = calculation.count(')')

    if start_parentheses > end_parentheses:
        calculation += ')'
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)
    else:
        calculation += '('
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, calculation)

def backspace():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)

tombol_bagi = tk.Button(root, text='/', width=5, height=3, command=lambda: calculate('/'))
tombol_bagi.grid(column=0, row=1)
tombol_parentheses = tk.Button(root, text='( )', width=5, height=3, command=parentheses)
tombol_parentheses.grid(column=0, row=2)
tombol_clear = tk.Button(root, text='C', width=5, height=3, command=clear)
tombol_clear.grid(column=0, row=3)
tombol_backspace = tk.Button(root, text='Backspace', width=5, height=3, command=backspace)
tombol_backspace.grid(column=0, row=4)
tombol1 = tk.Button(root, text='1', width=5, height=3, command=lambda: calculate(1))
tombol1.grid(column=1, row=1)
tombol2 = tk.Button(root, text='2', width=5, height=3, command=lambda: calculate(2))
tombol2.grid(column=2, row=1)
tombol3 = tk.Button(root, text='3', width=5, height=3, command=lambda: calculate(3))
tombol3.grid(column=3, row=1)
tombol4 = tk.Button(root, text='x', width=5, height=3, command=lambda: calculate('*'))
tombol4.grid(column=4, row=1)

tombol5 = tk.Button(root, text='4', width=5, height=3, command=lambda: calculate(4))
tombol5.grid(column=1, row=2)
tombol6 = tk.Button(root, text='5', width=5, height=3, command=lambda: calculate(5))
tombol6.grid(column=2, row=2)
tombol7 = tk.Button(root, text='6', width=5, height=3, command=lambda: calculate(6))
tombol7.grid(column=3, row=2)
tombol8 = tk.Button(root, text='-', width=5, height=3, command=lambda: calculate('-'))
tombol8.grid(column=4, row=2)

tombol9 = tk.Button(root, text='7', width=5, height=3, command=lambda: calculate(7))
tombol9.grid(column=1, row=3)
tombol10 = tk.Button(root, text='8', width=5, height=3, command=lambda: calculate(8))
tombol10.grid(column=2, row=3)
tombol11 = tk.Button(root, text='9', width=5, height=3, command=lambda: calculate(9))
tombol11.grid(column=3, row=3)
tombol12 = tk.Button(root, text='+', width=5, height=3, command=lambda: calculate('+'))
tombol12.grid(column=4, row=3)

tombol13 = tk.Button(root, text='0', width=5, height=3, command=lambda: calculate(0))
tombol13.grid(column=1, row=4)
tombol14 = tk.Button(root, text='00', width=5, height=3, command=lambda: calculate(00))
tombol14.grid(column=2, row=4)
tombol15 = tk.Button(root, text='.', width=5, height=3, command=lambda: calculate('.'))
tombol15.grid(column=3, row=4)
tombol16 = tk.Button(root, text='=', width=5, height=3, command=calculate_output)
tombol16.grid(column=4, row=4)

root.mainloop()