from storage import load_data



def list_transactions():
    data = load_data()
    for r in data:
        print(
            f"ID: {r['id']:<2} | "
            f"{r['type']:<7} | "
            f"{r['amount']:<7.2f} | "
            f"{r['category']:<12} | "
            f"{r['date']} | "
            f"{r['comment']}"
        )




def get_stats():
    data = load_data()


    income = 0
    expense = 0

    for r in data:
        if r["type"] == "income":
            income += r["amount"]
        elif r["type"] == "expense":
            expense += r["amount"]

    print("📊 STATISTICS")
    print(f"Income:  {income:.2f}")
    print(f"Expense: {expense:.2f}")
    print(f"Balance: {income - expense:.2f}")
    return income, expense

def print_transactions(data):
    if not data:
        print("Нет транзакций")
        return

    print("-" * 90)
    print(f"{'ID':<4} {'TYPE':<8} {'AMOUNT':<10} {'CATEGORY':<15} {'DATE':<12} COMMENT")
    print("-" * 90)

    for r in data:
        print(
            f"{r['id']:<4} "
            f"{r['type']:<8} "
            f"{r['amount']:<10.2f} "
            f"{r['category']:<15} "
            f"{r['date']:<12} "
            f"{r['comment']}"
        )

    print("-" * 90)


def top_categories():
    data = load_data()
    categories = {}

    for i in data:
        categories[i["category"]] = i["amount"]

    return sorted(categories.items() , key = lambda x: x[1] , reverse=True)[:5]

def print_top_categories():
    data = top_categories()

    print('top_categories\n')

    for key,value in data:
        print(f"{key}: {value}")