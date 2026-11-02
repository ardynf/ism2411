# 1. The first bug I spotted was in the total calculation because the code replaced the total with each sale instead of adding them together. Looking at the code helped me recognize the problem. This tells me that I am learning to pay attention to how variables change and that I need to keep practicing debugging to become more confident.
# 2. The apply_discount(price, tier) function takes two inputs: the original price and the customer's discount tier. It checks whether the tier is gold, silver, bronze, or another value, and then calculates and returns the price after applying the appropriate discount. A colleague could use this function without reading its body as long as they knew what inputs to provide and what result to expect.
# 3. AI Disclosure: I used ChatGPT to help explain Python functions, identify bugs, and understand variable scope. I reviewed the explanations to improve my understanding of the code. The AI use helped me build my understanding because it helped me identify where the errors were, so that I can identify how to fix them.



#exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return (price*rate)

#calling the function

tax1 = calculate_tax(100,0.7)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") #7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") #20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") #7.50

# exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price *0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax=discounted+tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# refactor inro a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5

sales = [120, 80, 250, 175, 90]

# Bug 1 fix: add each sale to the running total
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2 fix: added the missing colon
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3 fix: use < instead of <= so we don't go past
# the last valid index
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# exercise 6

x = 100

def double_it():
    global x
    # x = 999 # local another apple (not the same apple as above)


print(x)
print(double_it())
print(x)

