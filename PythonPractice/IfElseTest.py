indianDishes=["Samosa","Mirchi Bajji","Pakodi"]
chineseDishes=["Manchuria","Noodles"]

dish=input("Enter Dish:")

if dish in indianDishes:
    print("Indian Dish ",dish)
elif dish in chineseDishes:
    print("Chinese dish ",dish)
else:
    print("Unable to decide the dish: ",dish)
