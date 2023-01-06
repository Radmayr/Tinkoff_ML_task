from Levenshtein import *
import tkinter as tk

def result():
    value = path.get()
    try:
        result = comparison(value)
        win_res = tk.Tk()
        win_res.geometry("500x600+150+150")
        win_res.title('Результаты')
        label = tk.Label(win_res, text='Результаты')
        label.pack()
        for i in result:
            label = tk.Label(win_res, text=i)
            label.pack()
        
        def saving():
            saving_path = path_save.get()
            with open(saving_path, 'w', encoding='utf8') as f:
                for i in result:
                    f.write(i + '\n')
            label = tk.Label(win_res, text=f'Результат сохранен в {saving_path}')
            label.pack()   
            
        label = tk.Label(win_res, text='Сохранить в')
        label.pack()
        path_save = tk.Entry(win_res)
        path_save.pack()
        tk.Button(win_res, text='Сохранить', command=saving).pack()
        
               
    except: 
        win_res = tk.Tk()
        win_res.title('Результаты')
        label = tk.Label(win_res, text='Проблема с файлом\n Попробуй что-то другое')
        label.pack()
        

def delete_entry():
    path.delete(0, 'end')


win = tk.Tk()
win.title('Сравнение скриптов python')
win.geometry("400x100+100+100")
tk.Label(win, text='Файл со скриптами').grid(row=0, column=0)
path = tk.Entry(win)
path.grid(row=0, column=1)

tk.Button(win, text='Сравнить', command=result).grid(row=0, column=2)
tk.Button(win, text='Удалить', command=delete_entry).grid(row=1, column=1)

win.mainloop()
    