# Note:
# Static methods could have been used instead with only two classes (and no constructors), but the code would have been less object-oriented.
# By introducing the Temperature class, a constructor becomes necessary to validate and encapsulate data.
# This allows for the use of OOP concepts such as encapsulation, validation, inheritance, and exception handling.
# User input is skipped to keep the code simple and focused on core OOP functionality.


ABS_ZERO_C = -273.15
ABS_ZERO_F = -459.67


class ExtremeTemperatureError(Exception):
    pass


class Temperature:
    """Temperature object that only accepts valid Celsius ('C') or Fahrenheit ('F') units."""

    def __init__(self, value: float, unit: str):
        unit = unit.upper()
        if unit not in {"C", "F"}:
            raise ValueError("Unit must be 'C' or 'F'.")
        value = float(value)

        # validate against absolute zero
        if unit == 'C' and value < ABS_ZERO_C:
            raise ExtremeTemperatureError("Temperature below absolute zero in Celsius.")
        if unit == 'F' and value < ABS_ZERO_F:
            raise ExtremeTemperatureError("Temperature below absolute zero in Fahrenheit.")

        self.value = value
        self.unit = unit


class TemperatureConverter:
    def __init__(self, temperature: Temperature):
        self.temperature = temperature

    def to_celsius(self) -> Temperature:
        if self.temperature.unit == 'C':
            return self.temperature
        celsius = (self.temperature.value - 32) * 5 / 9
        return Temperature(celsius, 'C')


class ExtendedTemperatureConverter(TemperatureConverter):
    def to_fahrenheit(self) -> Temperature:
        if self.temperature.unit == 'F':
            return self.temperature
        fahrenheit = (self.temperature.value * 9 / 5) + 32
        return Temperature(fahrenheit, 'F')


if __name__ == "__main__":
    try:
        # normal conversions
        t1 = Temperature(32, 'F')
        print(f"{t1.value} °F equals {ExtendedTemperatureConverter(t1).to_celsius().value:.2f} °C")

        t2 = Temperature(0, 'C')
        print(f"{t2.value} °C equals {ExtendedTemperatureConverter(t2).to_fahrenheit().value:.2f} °F")

        # error cases
        t3 = Temperature(-500, 'F')   # below absolute zero
        print(f"{t3.value} °F equals {ExtendedTemperatureConverter(t3).to_celsius().value:.2f} °C")

        t4 = Temperature(-300, 'C')   # below absolute zero
        print(f"{t4.value} °C equals {ExtendedTemperatureConverter(t4).to_fahrenheit().value:.2f} °F")

        t5 = Temperature(60, 'K')   # invalid unit
        print(f"{t5.value} °F equals {ExtendedTemperatureConverter(t5).to_celsius().value:.2f} °C")

    except ExtremeTemperatureError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
