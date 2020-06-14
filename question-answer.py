from bs4 import BeautifulSoup
from tkinter import *  
from tkinter import messagebox  
from tkinter import simpledialog  
import requests
import random


window = Tk()  
window.title("Узнать столицу госудрства")  
window.geometry('190x70')    

request = requests.get('http://ostranah.ru/_lists/capitals.php')
bs = BeautifulSoup(request.text, 'html.parser')

coutres = []
coutres_sity = []
dict_y = {}

def clicked():
    try:
               
        messagebox.showinfo('Ответ', f'Столица государства {txt.get()}: {dict_y[txt.get()]}') 
    except:
        lol = simpledialog.askstring("Походу чего-то нет", "Введите страну:", show='')
        lol_2 = simpledialog.askstring("Походу чего-то нет", "Введите город:", show='')
        dict_y[lol] = lol_2
def clicked_2():
    messagebox.showinfo('Вы точно хотите выйти ?', 'Точно ?')
    window.quit()

def game():
    ssx = random.randint(0,len(dict_y))
    if not ssx % 2 == 0:
        ssx+=1
    lol_3 = simpledialog.askstring("Игра", f"Введите город, страны {coutres[ssx]}", show='')
    if str(lol_3) == str(dict_y[coutres[ssx]]):
        messagebox.showinfo('Крутой', 'Поздравляю')
    else:
        messagebox.showerror('Не то', 'Попробуй еще раз')
for elem in bs.find_all('td'):
    coutres_sity.append(elem.text)
    
for i in range(len(coutres_sity)):
    sds = str(coutres_sity[i])
    coutres.append(sds.replace(' ', ''))

for i in range(len(coutres_sity)):
    if i % 2 == 0:
        dict_y[coutres[i]] = coutres[i+1]    

lbl = Label(window, text="Введите имя страны: ")  
lbl.place(x=25,y=0)  
txt = Entry(window,width=25)  
txt.place(x=15,y= 20)  
btn = Button(window, text="Клик!", command=clicked)  
btn.place(x=15,y=40)
btn = Button(window, text="Игра!", command=game)  
btn.place(x=72,y=40)
btn = Button(window, text="Стоп!", command=clicked_2)  
btn.place(x=130,y=40)
 
window.mainloop()
