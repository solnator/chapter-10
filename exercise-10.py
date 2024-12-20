# ### Question 1
# i=[]
# for i in range(1, 100):
#     if i % 3 == 0:
#         print([i], end=" ")
#         # print(i)

# ### Question 2
# weight=float(input("Enter weight in kilogram: "))
# print("The weight in kilogram is: {:.1f}".format(weight))

# ### Question 3
# word=input("Enter a word: ")
# sorted_word=''.join(sorted(word))
# print(sorted_word)

# ### Question 4   ### with copilot
# products = ["Apples", "Oranges", "Bananas", "Grapes",\
#     "Peaches", "Plums", "Mangoes", "Cherries", "Kiwi", "Pears"]
# prices = [2.75, 20.25, 3.50, 4.00, 7.89, 5.50, 15.00, 12.75, 9.99, 135.00]

# # Apply 11% discount
# discounted_prices = [price * 0.89 for price in prices]

# for product, price in zip(products, discounted_prices):
#     print(f"{product:10} $ {price:6.2f}")

# ### Question 5
# from random import choice
# suits=['Hearts','Diamonds','Clubs','Spades']
# values=['One','Two','Three','Four','Five','Six','Seven',\
#     'Eight','Nine','Ten','Jack','Queen','King','Ace']
# ## List comperhension and format method to create the card names.
# card_names=['{} of {}'.format(value,suit)for suit in suits for value in values]
# print(card_names)

# ### Question 6
# list1 = [1, 2, 3, 4, 7, 8, 5]
# list2 = [5, 4, 7, 6, 3, 2, 9]

# has_common=False
# for x in list1:
#     if x in list2:
#         has_common=True

# if has_common:
#     print("The two lists have at least one item common.")
# else:
#     print('The two lists ha no items in common.')

# ### Question 7
# list=[int("1"*i)for i in range(1,101)]
# print(list)

# ### Question 8
# for i in range(1,1000):
#     if i%7==0 :
#         if str(i).endswith('6'):
#             print(i)

### Question 9   With ChatGPT
numbers = [num for num in range(1, 10001) if '3' in str(num)]
count=len(numbers)
print(f"Count of numbers between 1 and 10,000 containing the digit '3': {count}")