print("Welcome to the shopping cart.")

shopping_list = []
prices = []
option_list = ["1. Add item" , "2. View cart" , "3. Remove item" , "4. Compute total" , "5. Quit"]
quit = 0

while quit != 5:
    print("Please select one of the following: ")
    for i in option_list:
        print(i)
    quit = int(input("Please enter an action: "))

    if quit == 1:
       new_item = input("What would you like to add? ")
       shopping_list.append(new_item)
       print(f"{new_item} has been added to your cart. ")

    if quit == 2:
        print(f"The items in your shopping cart are: ")
        for i in shopping_list:
            print(i)