def print_stock(Data):
    i = 1
    for item, quantity in Data.items():
        print(f"{i}. {item}: {quantity}")
        i += 1


def remove_stock(Data):
    item = input("enter stock name or id: ").lower()
    if(item.isdigit()):
        item_id = int(item)
        if 1 <= item_id <= len(Data):
            item = list(Data.keys())[item_id - 1]
        else:
            print("Invalid stock id.")
            return 0
    quantity = int(input("enter quantity: "))
    if item in Data:
        if Data[item] - quantity < 0:
            print(f"Cannot remove {quantity} from {item}. Not enough stock.")
            return 0
    Data[item] -= quantity
    if Data[item] == 0:
        del Data[item]
    else:
        print(f"{item} not found in stock.")


def save_stock(Data,filename):
    print(f"Saving stock data to '{filename}'...")
    with open(filename, 'w') as file:
        for item, quantity in Data.items():
            file.write(f"{item},{quantity}\n")
    print("Exiting the program.")


try:
    with open('stock.txt', 'r') as file:
        stock_data = file.read()
    Data={}
    print(stock_data)
    for line in stock_data.splitlines():
        item, quantity = line.split(',')
        Data[item] = int(quantity)
    while True:
        print("enter 1 to add stock\nenter 2 to remove stock\nenter 3 to show stock’s contents\nenter 4 to exit the program")
        choice = int(input("enter your choice: "))
        match choice:
            case 1:
                item = input("enter item name: ").lower()
                quantity = int(input("enter quantity: "))
                Data[item] = Data.get(item, 0) + quantity
            case 2:
                print_stock(Data)
                remove_stock(Data)
            case 3:
                print_stock(Data)
            case 4:
                save_stock(Data, 'stock.txt')
                break
            case _:
                print("Unknown Status")

except FileNotFoundError:
    print("Error: The file 'stock.txt' was not found.")