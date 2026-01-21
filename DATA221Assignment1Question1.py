# Question 1: Controlled Multiplication Loop

threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    currentNumber += 1
    product *= currentNumber

print(f"Final Product: {product}")
print(f"Integer that caused the product to exceed the threshold: {currentNumber}")