### Question 1
i=[]
for i in range(1, 100):
    if i % 3 == 0:
        print([i], end=" ")
        # print(i)

### Question 2
weight=float(input("Enter weight in kilogram: "))
print("The weight in kilogram is: {:.1f}".format(weight))

### Question 3
word=input("Enter a word: ")
sorted_word=''.join(sorted(word))
print(sorted_word)

### Question 4   ### with copilot
products = ["Apples", "Oranges", "Bananas", "Grapes", "Peaches", "Plums", "Mangoes", "Cherries", "Kiwi", "Pears"]
prices = [2.75, 20.25, 3.50, 4.00, 7.89, 5.50, 15.00, 12.75, 9.99, 135.00]

# Apply 11% discount
discounted_prices = [price * 0.89 for price in prices]

for product, price in zip(products, discounted_prices):
    print(f"{product:10} $ {price:6.2f}")


