# DATA 221 - Assignment 1
# Question 1: Controlled Multiplication Loop

# define the threshold limit
threshold = 100
# initialize the product variable
product = 1
# initialize the integer counter
currentNumber = 1

# loop while product is less than or equal to threshold
while product <= threshold:
    # increment the integer
    currentNumber += 1
    # update product using multiplication assignment
    product *= currentNumber

print(f"Final Product: {product}")
print(f"Integer that caused the product to exceed the threshold: {currentNumber}")