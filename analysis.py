import matplotlib.pyplot as plt
from database import get_expenses
import pandas as pd

def show_graph():
    data = get_expenses()
    df = pd.DataFrame(data, columns=["id", "amount", "category", "date"])

    category_totals = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(6,6))
    category_totals.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expense Breakdown by Category")
    plt.show()
