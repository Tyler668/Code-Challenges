# Design a store using OOP methodology

# Attributes to a store

# Name
# Location
# departments of products
# A store needs product supply


class LatLon():
    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"


class Department:
    def __init__(self, name, products = [('Product A', 4), ('Product B', 7),  ('Product C', 9) ]):
        self.name = name
        self.products = [Product(*p) for p in products]  # Good line

    def __str__(self):
        return f"No products available in the {self.name} department yet"


class Store(LatLon):
    def __init__(self, name, lat, lon, departments):
        self.name = name
        self.location = LatLon(lat, lon)
        self.departments = departments

    def __str__(self):
        return f"Store {self.name}, {self.location.latitude}, {self.location.longitude}, {self.departments}"


store = Store('Lambda Store', 120, 156, [
              'Clothing', 'Cookware', 'Books', 'Sporting Goods'])


# print('The user selected ', store.departments[x])
# print(store)


while True:
    selection = input('Select a department number: ')

    if selection == "exit":
        print("Get out of my store")
        break

    try:
        selection = int(selection)
        if selection >= len(store.departments):
            print("Department does not exist")
        elif selection <= 0:
            print("Departments can't be negative")
        else:
            print('The user selected', store.departments[selection])

    except ValueError:
        print("Must enter a number")
