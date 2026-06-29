try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")

    purchased_items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in file:
        line = line.strip()

        # Skip blank lines
        if line == "":
            continue

        data = line.split()

        # Check for discount line
        if data[0].lower() == "discount":
            discount = int(data[1])

        else:
            purchased_items += 1

            # Check if item is free
            if data[1].lower() == "free":
                free_items += 1
                price = 0
            else:
                price = int(data[1])

            amount += price

    file.close()

    final_amount = amount - discount

    print("No of items purchased:", purchased_items - free_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("Error: File not found.")

except ValueError:
    print("Error: Invalid data in file.")

except Exception as e:
    print("Error:", e)