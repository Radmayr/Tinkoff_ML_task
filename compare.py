#!/usr/bin/env python
# coding: utf-8

# In[24]:


from Levenshtein import *


# In[39]:


def result():
    value = path.get()
    try:
        result = comparison(value)
        win_res = tk.Tk()
        win_res.geometry("500x600+150+150")
        win_res.title('Результаты')
        label = tk.Label(win_res, text='Результаты')
        label.pack()
        with open('results.txt', 'w', encoding='utf8') as f:
            for i in result:
                f.write(i + '\n')
                label = tk.Label(win_res, text=i)
                label.pack()
    except: 
        win_res = tk.Tk()
        win_res.title('Результаты')
        label = tk.Label(win_res, text='Проблема с файлом\n Попробуй что-то другое')
        label.pack()
        

def delete_entry():
    path.delete(0, 'end')
    


# In[40]:


import tkinter as tk


# In[41]:


win = tk.Tk()
win.title('Сравнение скриптов python')
win.geometry("400x100+100+100")
tk.Label(win, text='Файл со скриптами').grid(row=0, column=0)
path = tk.Entry(win)
path.grid(row=0, column=1)

tk.Button(win, text='Сравнить', command=result).grid(row=0, column=2)
tk.Button(win, text='Удалить', command=delete_entry).grid(row=1, column=1)

win.mainloop()


# In[ ]:




