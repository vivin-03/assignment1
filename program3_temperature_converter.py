print("\n===== TEMPERATURE CONVERTER =====")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter choice (1-6): "))
temp = float(input("Enter temperature value: "))

if choice == 1:
    print("Fahrenheit:", (temp * 9/5) + 32)

elif choice == 2:
    print("Celsius:", (temp - 32) * 5/9)

elif choice == 3:
    print("Kelvin:", temp + 273.15)

elif choice == 4:
    print("Celsius:", temp - 273.15)

elif choice == 5:
    print("Kelvin:", (temp - 32) * 5/9 + 273.15)

elif choice == 6:
    print("Fahrenheit:", (temp - 273.15) * 9/5 + 32)

else:
    print("Invalid option")
