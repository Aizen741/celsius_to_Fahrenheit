celsius = float(input("Write the Temperature of your body in Celsius: "))

def Fahr(celsius, fahrenheit = 32):
        return celsius*1.8 + fahrenheit
print("Temperature in fahrenheit is :", Fahr(celsius, fahrenheit = 32), "F)

if (Fahr(celsius,fahrenheit=32)>100):
    print("Dude! Take medicine, you are sick")
else:
    print("Dont worry,Take rest")
