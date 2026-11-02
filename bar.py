class Bar:
    def __init__(self, name, value, catagory):
        if name is None or catagory is None or value <0:
            raise ValueError()
        self.name = name
        self.value = value
        self.catagory = catagory
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def get_catagory(self):
        return self.catagory
    def __lt__(self, other):
        return self.value<other.value
if __name__ == "__main__":
    first = Bar("Apex Arena", 1200, "Action")
    second = Bar("Space Builders", 1500, "Sandbox")
    print(first < second)  # compare two objects. Expected True

    bars = [first, second]
    bars.sort(reverse=True) # calls __lt__ to sort
    for bar in bars:
        print(bar.get_name(), bar.get_value())