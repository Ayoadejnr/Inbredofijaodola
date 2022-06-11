length = float(input("Length: "))
breadth = float(input("Breadth: "))
copies = int(input("How many copies?: "))
calculate = ((length * breadth * 150) / 144) * copies
print(f"Total: {calculate}")