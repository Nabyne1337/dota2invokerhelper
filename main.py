import keyboard
from tkinter import messagebox
from time import sleep
#import pymem
def main():
    while True:
        if keyboard.is_pressed('insert'):
            messagebox.showinfo('Статус', 'Скрипт включён')
            while keyboard.is_pressed('insert') != True:
                sleep(0.01)
                if any(filter(keyboard.is_pressed, spells.keys())):
                    input = list(filter(keyboard.is_pressed, spells.keys()))
                    try:
                        keyboard.send(spells[input[0]][0]); keyboard.send(spells[input[0]][1]); keyboard.send(spells[input[0]][2]); sleep(0.1); keyboard.send('r')
                        del(input)
                    except Exception as e:
                        print(repr(e)); break
                if keyboard.is_pressed('insert'): messagebox.showinfo('Статус', 'Скрипт выключен'); break
        if keyboard.is_pressed('end'): messagebox.showinfo('Статус', 'Программа будет закрыта'); break
        
spells = {
    '1': 'qqq',
    '2': 'qqw',
    '3': 'qqe',
    '4': 'wwe',
    '5': 'wwq',
    '6': 'www',
    '7': 'eee',
    '8': 'eew',
    '9': 'eeq',
    '0': 'qwe' 
    }
            
if __name__ == "__main__":
    main()
