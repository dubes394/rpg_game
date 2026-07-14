class chai:
    origin = "india" #properties = variables in class

print(chai.origin)

chai.is_hot = True
print(chai.is_hot)

masala = chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False
print ("Class: ", chai.is_hot)
print(f"Masala {masala.is_hot}")  