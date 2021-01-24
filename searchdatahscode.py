from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import sqlite3

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)

def setting():
    return True

'''
def getrow(e):
	# Delete whatever is in the entry box
	ent.delete(0, END)

	# Add clicked list item to entry box
	ent.insert(0, ent.get(ANCHOR))
'''

'''
def search():
    q2 = q.get()
    query = "SELECT description , hscode FROM ItemsInfo WHERE description LIKE '%"+q2+"%' OR hscode LIKE '"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)
'''    


def getrow(e):
    rowid = trv.identify_row(e.y)
    item = trv.item(trv.focus())
    #ent.delete(0, END)
    q.set(item['values'][1])
    #print('double clicked')

def check(e):
    q2 = q.get()
    query = "SELECT description , hscode FROM TariffTbll WHERE description LIKE '%"+q2+"%' OR hscode LIKE '"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    mydb.commit()
    update(rows)
mydb = sqlite3.connect('TariffInfo.db')
cursor = mydb.cursor()

root = Tk()
q = StringVar()

style = ttk.Style()
style.theme_use()
style.configure("style.Treeview", font=('arial', 13,'bold'),)
style.configure("style.Treeview.Heading", font=('arial', 14),background='blue')
style.configure("Treeview",
                rowheight=30,
                )
#style.map('Treeview', background=[('selected', 'blue')])
#style.configure(background='blue')


wrapper1 = ttk.LabelFrame(root, text="كودى كةرستةى يان جورى كةرستةى بنفيسة")
wrapper2 = ttk.LabelFrame(root, text="ItemList")

wrapper1.pack(fill='both', expand="yes", padx=20, pady=2)
wrapper2.pack(fill='both', expand="yes", padx=20, pady=2)

#creat vertical scrollbar
tree_scroll = Scrollbar(wrapper2)
tree_scroll.pack(side=LEFT,fill=Y)



trv = ttk.Treeview(wrapper2, columns=(1,2), show="headings", height=13, style="style.Treeview",yscrollcommand=tree_scroll.set)
trv.pack()

# trv.bind('<Double 1>' getrow)

#configure scrollbar
tree_scroll.config(command=trv.yview)
#trv width and text orientation
trv.column(1,width=350, anchor=E)
trv.column(2,width=120, anchor=CENTER)
#trv.column(3, width=60, anchor=CENTER)

#trv.heading(1, text="Unit")
trv.heading(1, text="Description")
trv.heading(2, text="H.S Code")
#trv.heading(3, text="Unit")



query="SELECT description, hscode FROM TariffTbll"
cursor.execute(query)
rows = cursor.fetchall()
mydb.commit()
update(rows)


ent = ttk.Entry(wrapper1, textvariable=q, justify='right',width=150, font=('arial',16))
ent.pack(side=tk.LEFT, padx=6)



#btn = Button(wrapper1, text="copy", command=search)
#btn.pack(padx=6)

ent.focus()
ent.bind('<KeyRelease>', check)

# setting_image = PhotoImage(file='settings.png')

lbl = Label(root, text="Designed by Hiwa Hossien ",font=('arial',10, 'bold'))
lbl.pack(side=tk.LEFT, padx=10)

bt = ttk.Button(root, text='Settings', command=setting)
bt.pack(side=tk.RIGHT, padx=20)

trv.bind("<<TreeviewSelect>>", getrow)

app_width = 550
app_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2.3 ) - (app_height / 2)
root.title('H.S Code-Search')
root.iconbitmap("searchhss.ico")
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False, False)
#root.config(background='#333')
root.mainloop()
