Fruits=["Apples","Oranges","Bananas","Kiwis","Pineapples"]
for fruit in Fruits:
    print(fruit)

totalExpense=0
expenses=[1200,3400,1200,300,280,150]
for expense in expenses:
    totalExpense=totalExpense+expense

print("Total Expense:",totalExpense)

lenOfExpense=len(expenses)
for i in range(lenOfExpense):
    print("In ",i+1," month the expense is ",expenses[i])

itemNumber=1
while(itemNumber<=lenOfExpense):
    print("item at ",itemNumber," is ",expenses[itemNumber-1])
    itemNumber=itemNumber+1
