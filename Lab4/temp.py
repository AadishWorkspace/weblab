class Inv:
    def __init__(self):
        self.items = {}

    def additem(self, id, name, stock):

        self.items[id] = {
            "name" : name,
            "stock" : stock
        }

    def update(self, id, name, stock):

        self.items[id] = {
            "name" : name,
            "stock" : stock
        }

    def get(self, itemid):
        print(self.items.get(itemid))


inv = Inv()

inv.additem(1, "a", 1)
inv.additem(2, "b",2)

inv.update(1, "c", 2)

inv.get(1)

