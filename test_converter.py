from temperature_converter import Temperature, ExtendedTemperatureConverter, ExtremeTemperatureError

def demo():
    try:
        # Celsius to Fahrenheit
        celsius_temp = Temperature(500, 'C')
        conv1 = ExtendedTemperatureConverter(celsius_temp)
        print(f"{celsius_temp.value} °C equals {conv1.to_fahrenheit().value:.2f} °F")

        # Fahrenheit to Celsius
        fahrenheit_temp = Temperature(60, 'F')
        conv2 = ExtendedTemperatureConverter(fahrenheit_temp)
        print(f"{fahrenheit_temp.value} °F to {conv2.to_celsius().value:.2f} °C")

        # error case
        bad_temp = Temperature(-500, 'C')  # below absolute zero
        conv3 = ExtendedTemperatureConverter(bad_temp)
        print(f"{bad_temp.value} °C to {conv3.to_fahrenheit().value:.2f} °F")

    except ExtremeTemperatureError as e:
        print("Error:", e)
    except ValueError as e:
        print("Invalid unit:", e)

if __name__ == "__main__":
    demo()
