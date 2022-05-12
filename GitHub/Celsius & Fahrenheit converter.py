temperature = int(input('Temperature: '))
degree = input("Degree: 'C' celsius / 'F' Fahrenheit? ").upper()
if degree == "C":
    convert = round((temperature * 9/5) + 35, -1)  ##### -1 here rounds up to the nearest Tens
    print(f"{temperature}°C is {convert} in Fahrenheit")
elif degree == "F":
    convert = round((temperature - 32) * 5/9)
    print(f"{temperature}°F is {convert} in celsius")
else:
    print("Wrong Input")
