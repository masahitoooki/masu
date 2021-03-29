# -*- coding: utf-8 -*-
import tkinter as tk
import random

root = tk.Tk()
root.title("お言葉")
root.geometry("400x200")

words = ('まず生き残れ 儲けるのはそれからだ。', 
'夢は大きく、失敗は大胆に。', 
'困難の中に、機会がある。',
'おしゃべりは後にしてくれ。パンプが冷めちまう',
'筋肉がNOと叫んだら、私はYESと答える。',
'活動的な馬鹿より恐ろしいものはない。',
'最も大きな危険は勝利の瞬間にある。',
)

def outputWords(event): 

    value = txtBox.get()
    txtBox.configure(state='normal', width=30)

    # 既に文字があれば削除する
    if value: 
        txtBox.delete(0, tk.END)

    txtBox.insert(tk.END, random.choice(words))
    txtBox.configure(state='readonly')

# ラベルを追加
label = tk.Label(root, text="大事な言葉を伝えよう")
label.pack()

# テキストボックスを追加
txtBox = tk.Entry()
txtBox.configure(state='readonly', width=30)
txtBox.place(x=55, y=80)

# ボタンの追加
button = tk.Button(text='ボタンを押して', width=30)
button.place(x=50, y=120)
button.bind('<Button-1>', outputWords)

root.mainloop()
