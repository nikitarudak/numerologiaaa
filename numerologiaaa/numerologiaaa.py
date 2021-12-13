from tkinter import *
from tkinter import ttk, Canvas, Frame, BOTH
from module import *
import re

dictrus = {"А": "1", "Б": "2", "В": "3", "Г": "4", "Д": "5", "Е": "6", "Ё": "7", "Ж": "8", "З": "9", "И": "1", "Й": "2", "К": "3", "Л": "4", "М": "5", "Н": "6", "О": "7", "П": "8", 
           "Р": "9", "С": "1", "Т": "2", "У": "3", "Ф": "4", "Х": "5", "Ц": "6", "Ч": "7", "Ш": "8", "Щ": "9", "Ъ": "1", "Ы": "2", "Ь": "3", "Э": "4", "Ю": "5", "Я": "6"}
dicteng = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9", "J": "1", "K": "2", "L": "3", "M": "4", "N": "5", "O": "6", "P": "7", "Q": "8", 
           "R": "9", "S": "1", "T": "2", "U": "3", "V": "4", "W": "5", "X": "6", "Y": "7", "Z": "8"}

letters_eng = readDictKeys(dicteng)
numb_eng = readDictVal(dicteng)
letters_rus = readDictKeys(dictrus)
numb_rus = readDictVal(dictrus)

def textOutput(event):
    ''' Берет данные из ячеек, проверяет их и выводит их в функцию getNameNumber()
    Выводит текст в lbl4
    '''
    try:
        name = str(ent1.get())
        verif = name.isalpha()
    except ValueError:
        text = "Введите имя"
    if verif == True:
        nameu = name.upper()
        if re.search('[aA-zZ]', name):
            text = getNameNumber(numb_eng, letters_eng, nameu)
        elif re.search('[а-яА-ЯёЁ]', name):
            text = getNameNumber(numb_rus, letters_rus, nameu)
        else:
            text = "Введите имя на русском или латинском языке"
    else:
        text = "Введите имя"
    lbl4.configure(text = text)

window = Tk()
window.title("Нумерология")
window.geometry("600x600")
window.configure(bg = "lightblue")

frm1 = LabelFrame(window)
frm2 = Frame(window, bg = "black")
frm3 = Frame(frm2, bg = "black")
frm4 = Frame(window, bg = 'lightblue')

lbl1 = Label(window, text = "Нумерология", font = "Arial 20", fg = "black", bg = "white")
lbl2 = Label(frm1, text = "Введите имя", font = "Arial 12", fg = "white", bg = "black")
lbl3 = Label(frm4, text = "Решение", font = "Arial 20", fg = "white", bg = "grey")
lbl4 = Label(frm4, text = " ", font = "Arial 15", fg = "white", bg = "lightblue")

ent1 = Entry(frm2, bg = "white", fg = "black", width = 25, font = "Arial 20")

btn = Button(frm3, text = "Рассчитать", font = "Arial 15", bg = "lightyellow", fg = "black")

btn.bind("<Button-1>", textOutput)
ent1.bind("<Return>")

lbl1.pack()
frm1.pack(padx = 20, pady = 60)
lbl2.pack(side = TOP)
frm2.pack()
ent1.pack()
frm3.pack(pady = 30)
btn.pack()
frm4.pack(pady = 20)
lbl3.pack()
lbl4.pack()
window.mainloop()