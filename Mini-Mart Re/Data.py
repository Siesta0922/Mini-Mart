art = "____________________________________________________\n ___  ___                    ___  ___           _\n |  \/  (_)     (_)          |  \/  |          | |  \n | \  / |_ _ __  _   ______  | \  / | __ _ _ __| |_ \n | |\/| | | '_ \| | |______| | |\/| |/ _` | '__| __| \n | |  | | | | | | |          | |  | | (_| | |  | |_  \n |_|  |_|_|_| |_|_|          |_|  |_|\__,_|_|   \__| \n ____________________________________________________"

class Product:
    def __init__ (initialize, name, price):
        initialize.name = name
        initialize.price = price

Snacks = [
    Product ("Chips", 19.50),
    Product ("Candy pack", 38.50),
    Product ("Wafer pack", 59.50),
    Product ("Siopao", 43.00),
]

Beverage = [
    Product ("Juice", 15.00),
    Product ("Soft Drink", 34.50),
    Product ("Water Bottle", 13.50),
    Product ("Coffee Drink", 23.50),

]

Cleaning_Items = [
    Product("Bleach", 22.95),
    Product("Soap Detergent", 91.00),
    Product("Fabric Softerner", 69.30),
    Product("Powdered Detergent", 28.00),
]

Sanitary_Items = [
    Product("Toothpaste", 145.00),
    Product("Shampoo", 60.00),
    Product("Bar Soap", 115.00),
    Product("Pads", 121.00),
]