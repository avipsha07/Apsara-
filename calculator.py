# Simple Calculator

num1 = int(float(input("0: ")))
num2 = int(float(input("9: ")))

print("\nResults:")
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2 if num2 != 0 else "Undefined (division by zero)")
print("Modulus:", num1 % num2 if num2 != 0 else "Undefined (division by zero)")
print("Integer Division:", num1 // num2 if num2 != 0 else "Undefined (division by zero)")
print("Power:", num1 ** num2)
