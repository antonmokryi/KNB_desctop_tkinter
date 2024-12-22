from tkinter import *
import time
from func import hi_off
import random


root = Tk()
root.title("Гра Камінь-Ножиці-Бумага")
root.iconbitmap("icon.ico")
root.geometry("700x500")
root.config(relief="groove",  border="1", highlightthickness="2", highlightcolor="grey",)

hi = Label(text="Вітаю! \n це гра \"КАМІНЬ-НОЖИЦІ-БУМАГА\"",  
    width=40,
    height=10,
    font=("Arial", 14),
    justify="center",
    
    )

hi.pack()
root.after(3000, lambda: hi.destroy())


you = Label(text="Ви:", width=20, height=2, font=("Arial", 14))
comp = Label(text="Комп'ютер:", width=20, height=2, font=("Arial", 14))
label_comp = Label(text=f"", font=("Arial", 14)) 
label_result = Label(text=f"", font=("Arial", 14)) 
label_you = Label(text=f"", font=("Arial", 14)) 

    
btn_noj = Button(root, text="Ножиці", width=10, height=2, command=lambda: game("Ножиці"))
btn_bum = Button(root, text="Бумага", width=10, height=2, command=lambda: game("Бумага"))
btn_kam = Button(root, text="Камінь", width=10, height=2, command=lambda: game("Камінь"))
    
comp.place(x=500, y=0)
you.place(x=0, y=0)
btn_bum.place(x=0, y=200)
btn_noj.place(x=100, y=200)
btn_kam.place(x=200, y=200)
label_comp.place(x=400, y=50)
label_result.place(x=250, y=400)
label_you.place(x=20, y=50)

my_score = 0
comp_score = 0
label_comp_score = Label(text=f"", font=("Arial", 14))
label_user_score = Label(text=f"", font=("Arial", 14))
label_user_score.place(x=20, y=80)
label_comp_score.place(x=400, y=80)

def game(param):
    
    global my_score, comp_score 

    velues = ["Камінь", "Бумага", "Ножиці"]
    value = random.choice(velues)
    
    if param == value:
        label_result.config(text="Нічия")
    elif param == "Камінь" and value == "Ножиці" or param == "Бумага" and value == "Камінь" or param == "Ножиці" and value == "Бумага":
        my_score +=1
        label_result.config(text="Ви перемогли! +1 бал")
    else:
        comp_score +=1
        label_result.config(text="Комп'ютер переміг! +1 бал")

    label_comp.config(text=f"Комп'ютер обрав {value}")
    label_you.config(text=f"Ви обрали {param}")
    label_comp_score.config(text=f"Бали: {comp_score}")
    label_user_score.config(text=f"Бали: {my_score}")


root.mainloop()