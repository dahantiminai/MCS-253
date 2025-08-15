class ExtremeTemperatureError(Exception):
    """Raised when a temperature is below absolute zero."""
    def __init__(self, message="Temperature is below absolute zero!"):
        super().__init__(message)


class TemperatureConverter:
    """Parent Class: Fahrenheit to Celsius (one function)."""

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert °F to °C with absolute-zero validation."""
        if fahrenheit < -459.67:
            raise ExtremeTemperatureError("Fahrenheit temperature below absolute zero!")
        celsius = (fahrenheit - 32) * 5 / 9
        if celsius < -273.15:
            raise ExtremeTemperatureError("Celsius temperature below absolute zero!")
        return celsius


class ExtendedTemperatureConverter(TemperatureConverter):
    """Child Class: Celsius to Fahrenheit (one function).""" 

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert °C to °F with absolute-zero validation."""
        if celsius < -273.15:
            raise ExtremeTemperatureError("Celsius temperature below absolute zero!")
        fahrenheit = (celsius * 9 / 5) + 32
        if fahrenheit < -459.67:
            raise ExtremeTemperatureError("Fahrenheit temperature below absolute zero!")
        return fahrenheit


def get_float_or_exit(prompt):
    """
    Prompt for a float. User can type 'exit' to quit.
    Keeps looping on invalid input.
    """
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "exit":
            return None
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a numeric value or type 'exit'.")


def main():
    print("TEMPERATURE CONVERTER")
    print("Type 'exit' to quit at any time.\n")

    while True:
        print("Choose a conversion:\n")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        choice = input("\nEnter your option: ").strip()

        if choice.lower() == "exit":
            print("Goodbye!")
            break

        if choice == "1":
            value = get_float_or_exit("Enter temperature in Fahrenheit: ")
            if value is None:
                print("Goodbye!")
                break
            try:
                c = TemperatureConverter.fahrenheit_to_celsius(value)
                print(f"{value:.2f}°F to {c:.2f}°C\n")
            except ExtremeTemperatureError as e:
                print(f"{e}\n")

        elif choice == "2":
            value = get_float_or_exit("Enter temperature in Celsius: ")
            if value is None:
                print("Goodbye!")
                break
            try:
                f = ExtendedTemperatureConverter.celsius_to_fahrenheit(value)
                print(f"{value:.2f}°C to {f:.2f}°F\n")
            except ExtremeTemperatureError as e:
                print(f"{e}\n")

        else:
            print("Invalid selection. Please enter 1 or 2, or type 'exit' to quit.\n")


if __name__ == "__main__":
    main()
