import tkinter as tk


def show_selection():
    selected = listbox.get(listbox.curselection())
    print("wybarany element", selected)


app = tk.Tk()
app.title("Przykład 3")

listbox = tk.Listbox(app)
listbox.insert(1, "Element 1")
listbox.insert(2, "Element 2")
listbox.insert(3, "Element 3")
listbox.pack()

button = tk.Button(app, text="Pokaz wybrane", command=show_selection)
button.pack(side='bottom')

app.mainloop()