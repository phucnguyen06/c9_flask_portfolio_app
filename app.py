in_stock = [
    ("t-shirt", "blue", 9.99),
    ("t-shirt", "white", 12.99),
    ("shirt", "blue", 19.99),
    ("shirt", "black", 17.99),
    ("jean","dark blue",49.99)
    ]

in_stock_1 = [
    "t-shirt", "blue", 9.99,
    "t-shirt", "white", 12.99,
    "shirt", "blue", 19.99,
    "shirt", "black", 17.99
    ]

top = []
bottom = []
t_shirt = []

def show_Tshirt():
    for item in top:
        if item[0] == 't-shirt':
            t_shirt.append(top[:2])
    return t_shirt

def show_top():
    print("Here's top products: ")
    for item in top:
        for thing in item:
            print(thing)
        
def show_bottom():
    print("Here's bottom products: ")
    for item in bottom:
        print(item)

while True:
    try:
        search = input("Search: ")
    except ValueError:
        pass
    else:
        if search == 'top':
            top.append(in_stock[:4])
            show_top()
            continue
        elif search == 'home':
            show_top()
            show_bottom()
            break
        elif search == 'bottom':
            bottom.append(in_stock[-1])
            show_bottom()
            continue
        else:
            print(False)

