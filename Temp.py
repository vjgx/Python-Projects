class Temperature:
    def celsius_to_farenheit():
      c=int(input("Enter temperature in celsius:"))
      farenheit = c*(9/5)+32
      print("Temperature in farenheit is:",farenheit)
    
    def farenheit_to_celsius():
      f = int(input("Enter the temperature in farenheit:"))
      celsius =  (f - 32) * 5/9
      print("Temeprature in celsius is:",celsius)

temp = Temperature
temp.celsius_to_farenheit()
temp.farenheit_to_celsius()

