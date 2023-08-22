import math


class VerboseValue:
    """Verbose value."""

    def __init__(self, value):
        """Initialize verbose value."""
        self.value = value

    def show_op(self, op, other, new_value):
        print(f"{self.value} {op} {other} = {new_value}")

    def __add__(self, other):
        new_value = self.value + other
        self.show_op("+", other, new_value)

        return VerboseValue(new_value)

    def __subtract__(self, other):
        new_value = self.value - other
        self.show_op("-", other, new_value)

        return VerboseValue(new_value)

    def __mul__(self, other):
        new_value = self.value * other
        self.show_op("*", other, new_value)

        return VerboseValue(new_value)

    def __truediv__(self, other):
        new_value = self.value / other
        self.show_op("/", other, new_value)

        return VerboseValue(new_value)


def ticks_100ms_to_meters_sec(ticks_100ms, ticks_rev=2048, wheel_rad=2, gear_ratio=5):
    ticks_sec = ticks_100ms * 10
    rev_sec = ticks_sec / ticks_rev
    meters_sec = rev_sec * (2 * math.pi) * wheel_rad

    wheel_meters_sec = meters_sec / gear_ratio
    return wheel_meters_sec


ticks_100ms = 10_000

# Eager eval.
eager_ans = ticks_100ms_to_meters_sec(ticks_100ms)
print(f"Eager: {eager_ans}\n")

# Verbose eval.
y = VerboseValue(ticks_100ms)
y = ticks_100ms_to_meters_sec(y)
print(f"Verbose: {y.value}")
