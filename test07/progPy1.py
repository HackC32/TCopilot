print("Hello, World!")

a = 5
b = 10

print("The sum of a and b is:", a + b)


def calculate(a, b):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b if b != 0 else None,
    }

results = calculate(a, b)

print("Calculations for a and b:")
print("  sum:", results["sum"])
print("  difference:", results["difference"])
print("  product:", results["product"])
if results["quotient"] is not None:
    print("  quotient:", results["quotient"])
else:
    print("  quotient: undefined (division by zero)")
