class chaiorder:

    def __init__(self, type_, size):
        self.type = type_ 
        self.size = size


    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    

order = chaiorder("ginger", 230)
print(order.summary())

order_two =chaiorder("masala", 400)
print(order_two.summary())
