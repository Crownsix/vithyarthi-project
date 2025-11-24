import tkinter as tk
from tkinter import ttk
from database import add_expense, get_expenses
from analysis import show_graph
from datetime import datetime

def run_gui():
    win = tk.Tk()
    win.title("Smart Expense Tracker")
    win.geometry("500x500")

    tk.Label(win, text="Amount").pack()
    amount_entry = tk.Entry(win)
    amount_entry.pack()

    tk.Label(win, text="Category").pack()
    category_box = ttk.Combobox(win, values=["Food", "Travel", "Shopping", "Bills", "Other"])
    category_box.pack()

    tk.Label(win, text="Date").pack()
    date_entry = tk.Entry(win)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    date_entry.pack()

    def save_expense():
        amt = float(amount_entry.get())
        cat = category_box.get()
        date = date_entry.get()
        add_expense(amt, cat, date)
        tk.Label(win, text="Saved!", fg="green").pack()

    tk.Button(win, text="Add Expense", command=save_expense).pack(pady=10)
    tk.Button(win, text="Show Graph", command=show_graph).pack(pady=10)

    win.mainloop()
