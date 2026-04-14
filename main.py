import pandas as pd
import matplotlib.pyplot as plt

# What kind of expenses and what category does it fall to

categories = ["Food", "Transport", "Clothes", "Entertainment", "Other"]

print("\nCategories:")
for cat in categories:
    print("-", cat)

# Expenses list
expenses = []

while True:
    date = input("\nEnter date as (YYYY-MM-DD) or 'exit' to finish: ")
    if date.lower() == 'exit':
        break

    category = input("Enter category: ")
    amount = float(input("Enter amount: $"))
    description = input("What was the item: ")

    expenses.append({
    'date': date,
    'category': category,
    'amount': amount,
    'description': description
    })
    print("Expense added!")

    # Create the bar graph
    df = pd.DataFrame(expenses)
    summary = df.groupby('category')['amount'].sum()

    summary.plot(kind='bar')
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
