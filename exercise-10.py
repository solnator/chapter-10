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

### Question 4
products = ["Apples", "Oranges", "Bananas", "Grapes",\
    "Peaches", "Plums", "Mangoes", "Cherries", "Kiwi", "Pears"]
prices = [2.75, 20.25, 3.50, 4.00, 7.89, 5.50, 15.00, 12.75, 9.99, 135.00]

# Apply 11% discount
discounted_prices = [price * 0.89 for price in prices]

for product, price in zip(products, discounted_prices):
    print(f"{product:10} $ {price:6.2f}")

### Question 5
from random import choice
suits=['Hearts','Diamonds','Clubs','Spades']
values=['One','Two','Three','Four','Five','Six','Seven',\
    'Eight','Nine','Ten','Jack','Queen','King','Ace']
## List comperhension and format method to create the card names.
card_names=['{} of {}'.format(value,suit)for suit in suits for value in values]
print(card_names)

### Question 6
list1 = [1, 2, 3, 4, 7, 8, 5]
list2 = [5, 4, 7, 6, 3, 2, 9]

has_common=False
for x in list1:
    if x in list2:
        has_common=True

if has_common:
    print("The two lists have at least one item common.")
else:
    print('The two lists ha no items in common.')

### Question 7
list=[int("1"*i)for i in range(1,101)]
print(list)

### Question 8
for i in range(1,1000):
    if i%7==0 :
        if str(i).endswith('6'):
            print(i)

### Question 9 
numbers = [num for num in range(1, 10001) if '3' in str(num)]
count=len(numbers)
print(f"Count of numbers between 1 and 10,000 containing the digit '3': {count}")

### Question 10 By myself
for i in range(10,150):
    x=i
    rev=int(str(x)[::-1])
    x+=rev
    if str(i)==str(i)[::-1]:
        print(f'{i} palindrome: {x}')

### Question 10 Half ChatGPT
for num in range(10, 150):
    iterations = 0
    current = num
    while iterations < 20:
        reverse_num = int(str(current)[::-1])
        current += reverse_num
        iterations += 1
        if str(num)==str(num)[::-1]:
            print(f"{num} becomes a palindrome: {current} in {iterations} iterations")
            break

### Question 11 
def generate_palindromes():
    palindromes = []
    for first_half in range(199, 801):  # First 3 digits of the palindrome
        palindrome = int(str(first_half) + str(first_half)[::-1])  # Create palindrome
        palindromes.append(palindrome)
    return palindromes

def find_close_pairs(palindromes):
    for i in range(len(palindromes) - 1):
        if abs(palindromes[i] - palindromes[i + 1]) < 20:  # Check if within 20
            print(f"Pair: {palindromes[i]} and {palindromes[i + 1]}")

# Main program
palindromes = generate_palindromes()
find_close_pairs(palindromes)

### Question 12 With copilot
# Define the flip map for digits
flip_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

def flip_number(num):
    # Convert the number to string and reverse it
    num_str = str(num)
    flipped = ""
    for digit in reversed(num_str):
        if digit not in flip_map:
            return 'invalid'
        flipped += flip_map[digit]
    return flipped

# Loop through all six-digit numbers
for num in range(100000, 1000000):
    flipped_num = flip_number(num)
    if flipped_num != 'invalid':
        print(f"Original: {num}, Flipped: {flipped_num}")

### Question 13
i=3
j=9
x=((i*j)+i+j)
print(x)
## Answer = [19, 29, 39, 49, 59, 69, 79, 89, 99]

### Question 13
def check_property(num):
    digits = [int(d) for d in str(num)]
    product = 1
    for d in digits:
        product *= d
    digit_sum = sum(digits)
    return (product + digit_sum) == num

def find_numbers():
    result = []
    for num in range(1, 50):
        if check_property(num):
            result.append(num)
    return result

numbers = find_numbers()
print(numbers)

### Question 14
def find_smallest_number():
    num = 1
    while True:
        num_str = str(num)
        new_num_str = num_str[1:] + num_str[0]
        new_num = int(new_num_str)

        if new_num == 3 * num:
            return num
        num += 1


result = find_smallest_number()
print(f"The smallest number is: {result}")


### Question 15 
zeros = 0
for num in range(0, 1001):
    zeros += str(num).count("0")
print(f"The total number of zeros from 0 to 1000 is: {zeros}")


### Question 16 
def convert_height(decimal_height):
    
    feet = int(decimal_height)
    fractional_part = decimal_height - feet
    
    inches = round(fractional_part * 12)
    
    print(f"{feet} feet, {inches} inches")

decimal_height = float(input("Enter height in decimal feet: "))
convert_height(decimal_height)

### Question 17
def convert_height_to_inches(height_str):
    try:
        feet, inches = height_str.split("'")
        feet = int(feet.strip())
        inches = int(inches.strip().replace('"', ''))
        
        total_inches = (feet * 12) + inches
        return total_inches
    except ValueError:
        print("Invalid format. Please enter height in the format X'Y\" (e.g., 5'11\").")
        return None

def main():
    while True:
        user_input = input("Enter height in the format X'Y\" (or type 'done' to quit): ").strip()
        if user_input.lower() == 'done':
            print("Goodbye!")
            break
        total_inches = convert_height_to_inches(user_input)
        if total_inches is not None:
            print(f"Total inches: {total_inches}")

main()


### Question 18 With ChatGPT
def calculate_point_difference(score_str):
    try:
        # Split the input into winning and losing scores
        winning_score, losing_score = score_str.split('-')
        winning_score = int(winning_score.strip())
        losing_score = int(losing_score.strip())
        # Calculate the point difference
        point_difference = winning_score - losing_score
        return point_difference
    except ValueError:
        print("Invalid format. Please enter the score in the format winning-losing (e.g., 27-13).")
        return None

def main():
    while True:
        user_input = input("Enter football score in the format winning-losing (or type 'done' to quit): ").strip()
        if user_input.lower() == 'done':
            print("Goodbye!")
            break
        point_difference = calculate_point_difference(user_input)
        if point_difference is not None:
            print(f"Point difference: {point_difference}")

# Run the program
main()

### Question 19 
def main():
    february_count = 0
    day_25_count = 0
    
    while True:
        user_input = input("Enter a birthday in the format month/day (or type 'done' to quit): ").strip()
        if user_input.lower() == 'done':
            print("Goodbye!")
            print(f"Number of birthdays in February: {february_count}")
            print(f"Number of birthdays on the 25th: {day_25_count}")
            break
        try:
            # Parse the month and day
            month, day = user_input.split('/')
            month = int(month.strip())
            day = int(day.strip())
            
            # Check conditions
            if month == 2:
                february_count += 1
            if day == 25:
                day_25_count += 1
        except ValueError:
            print("Invalid format. Please enter the birthday in the format month/day (e.g., 12/25).")

# Run the program
main()

### Question 20 
def convert_date_to_verbose(date_str):
    # Dictionary mapping month numbers to names
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    
    try:
        # Split the input into month, day, and year
        month, day, year = date_str.split('/')
        month_name = months[month]  # Get the month name
        day = int(day)  # Convert day to integer
        year = int(year)  # Convert year to integer
        
        # Convert two-digit year to four-digit year
        if year < 50:
            year += 2000
        else:
            year += 1900
        
        # Return the formatted date
        return f"{month_name} {day}, {year}"
    except (ValueError, KeyError):
        return "Invalid date format. Please enter the date in the format mm/dd/yy."

def main():
    while True:
        user_input = input("Enter a date in the format mm/dd/yy (or type 'done' to quit): ").strip()
        if user_input.lower() == 'done':
            print("Goodbye!")
            break
        result = convert_date_to_verbose(user_input)
        print(result)

# Run the program
main()

### Question 22
def generate_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    while True:
        user_input = input("Enter a number to generate its multiplication table (or type 'done' to quit): ").strip()
        if user_input.lower() == 'done':
            print("Goodbye!")
            break
        try:
            number = int(user_input)
            generate_multiplication_table(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the program
main()
