while True:
    name = input("Enter customer name: ")
    total = 0
    while True:
        print("Enter your item amount and quantity:")
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items? (yes/no): ")
        if repeat == "no" or repeat=="NO":
            break
    
    print("-" * 40)
    print("Name:", name)
    print("Amount to be paid:", total)
    print("-" * 40)
    print("*********** HAPPY SHOPPING **************")

    repeat1 = input("Do you want to go to the next customer? (yes/no): ")
    if repeat1 == "no" or repeat1=="NO":
        break
