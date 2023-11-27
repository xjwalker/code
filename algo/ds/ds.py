class Stack:

    def __init__(self):
        self.values = []

    def pop(self):
        if len(self.values) == 0:
            return

        last_item = self.values[len(self.values) - 1]
        self.values = self.values[0:len(self.values) - 1]  # slice

        return last_item

    def push(self, value):
        self.values.append(value)

    def print(self):
        values = ''
        for value in self.values:
            values += f"{value} "

        return values


if __name__ == '__main__':
    pila = Stack()

    pila.push(1)
    pila.push(2)
    pila.push(3)
    pila.push(4)

    print(pila.print())
    pila.pop()
    pila.pop()
    print(pila.print())
