print("Welcome to the shopping cart.")

shopping_list = []
prices = []
total = 0
option_list = ["1. Add item" , "2. View cart" , "3. Remove item" , "4. Compute total" , "5. Quit"]
quit = 0

while quit != 5:
    print("Please select one of the following: ")
    for i in option_list:
        print(i)
    quit = int(input("Please enter an action: "))

    if quit == 1:
       new_item = input("What would you like to add? ")
       item_prices = float(input(f"What is the price of {new_item}? "))
       shopping_list.append(new_item)
       prices.append(item_prices)
       print(f"{new_item} has been added to your cart. ")

    if quit == 2:
        print(f"The items in your shopping cart are: ")
        for i in range(len(shopping_list)):
            print(f"{i + 1}. {shopping_list[i]} - ${prices[i]:.2f}")

    if quit == 3:
       remove_item = int(input("What would you like to remove from the list? "))
       shopping_list.pop(remove_item -1)
       prices.pop(remove_item -1)
       print("The item has been removed from the cart. ")

    if quit == 4:
        for price in prices:
            total += price
        print(f"{total:.2f} is how much you owe. ")
