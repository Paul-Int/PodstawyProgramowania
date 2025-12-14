categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = expenses[0]
max_index = 0

i = 1
while i < len(expenses):
    if expenses[i] > max_expense:
        max_expense = expenses[i]
        max_index = i
    i += 1

print("Most expensive category:", categories[max_index])
print("Expense amount:", max_expense)