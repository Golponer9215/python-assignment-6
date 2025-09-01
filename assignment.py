# assignment 
# ======================
# FUNCTIONS & SCOPE TASKS
# ======================

# 1
def task1_sum_of_two_numbers(a, b):
    """
    Task 1:
    Write a function that accepts two numbers (a and b) as parameters
    and returns their sum.
    Test the function by calling it with different numbers.
    """
    x=a+b
    return x
ans=task1_sum_of_two_numbers(3,9)
print(ans)
pass
    



# 2
def task2_square_number(n):
    """
    Task 2:
    Write a function that accepts a number and returns its square.
    Example: square_number(5) → 25
    """
    y=n**2
    return y
ans2=task2_square_number(10)
print(ans2)
pass


# 3
def task3_greet_user(name):
    """
    Task 3:
    Write a function that accepts a person's name as a parameter
    and prints a greeting message like: "Hello, John!"
    """
    print(f"Good night {name}")
task3_greet_user("Mr Bankat")    
pass


# 4
def task4_area_of_rectangle(length, width):
    """
    Task 4:
    Write a function that accepts the length and width of a rectangle
    and returns its area.
    Formula: area = length * width
    """
    if length <0 or width <0:
        return "Error : lenght and width cannot be negative"
    area= length * width
    return area
print(task4_area_of_rectangle(4,6))
pass


# 5
def task5_perimeter_of_square(side):
    """
    Task 5:
    Write a function that accepts the side length of a square
    and returns its perimeter.
    Formula: perimeter = 4 * side
    """
    if side <=0:
        return "Error"

    perimeter= 4*side
    return perimeter
print(task5_perimeter_of_square(65))
pass


# 6
def task6_celsius_to_fahrenheit(celsius):
    """
    Task 6:
    Write a function that converts a temperature from Celsius to Fahrenheit.
    Formula: (celsius * 9/5) + 32
    """
    fahrenheit =(celsius * 9/5) +32
    return fahrenheit
print(task6_celsius_to_fahrenheit(0))    
pass


# 7
def task7_find_max(a, b, c):
    """
    Task 7:
    Write a function that accepts three numbers as parameters
    and returns the largest number.
    """
    max_num= max(a,b,c)
    return max_num
print(task7_find_max(9,2,11))
pass


# 8
def task8_even_or_odd(n):
    """
    Task 8:
    Write a function that accepts a number and returns
    "Even" if the number is even, and "Odd" if the number is odd.
    """
    if n%2==0:
        return "Even"
    else:
        return "Odd"
print(task8_even_or_odd(9))    
pass


# 9
def task9_count_vowels(word):
    """
    Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
    """
    vowels=("a","e","i","o","u")
    return sum(1 for char in word.lower() if char in vowels)
print(task9_count_vowels("peel"))    
pass


# 10
def task10_multiply_list(numbers):
    """
    Task 10:
    Write a function that accepts a list of numbers as a parameter
    and returns the product of all the numbers in the list.
    Example: multiply_list([1, 2, 3, 4]) → 24
    """
    prod=1
    for num in numbers:
        prod *= num
    return prod    
numbers=[1,2,3,4]    
print(task10_multiply_list(numbers))    
pass


# 11
def task11_reverse_string(text):
    """
    Task 11:
    Write a function that accepts a string as a parameter
    and returns the string reversed.
    Example: reverse_string("hello") → "olleh"
    """
    print(f"{text [::-1]}")

task11_reverse_string("Bankat")    
pass


# 12
def task12_is_prime(n):
    """
    Task 12:
    Write a function that accepts a number as a parameter
    and returns True if the number is prime, otherwise False.
    """
    if  n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(task12_is_prime(23))
pass


# 13
myname="Gotom"
def task13_scope_demo():
    """
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
    """
    myname="Golpwana"
    print("inside variable=",myname)

print("outside variable",myname)    
task13_scope_demo()
pass


# 14
def task14_sum_list(numbers):
    """
    Task 14:
    Write a function that accepts a list of numbers
    and returns the sum of all the elements in the list.
    Do not use Python's built-in sum() function.
    """
    total=0
    for i in nums:
        total+=i
    return total     
nums=[1,2,3,4,5,6]
print(task14_sum_list(nums))
pass


# 15
def task15_average_of_list(numbers):
    """
    Task 15:
    Write a function that accepts a list of numbers
    and returns the average.
    Formula: average = sum of numbers / count of numbers
    """
    total=sum(numbers)
    count=len(numbers)
    if count ==0:
        return None
    return total/count
numbers=[1,2,8,9]
average=task15_average_of_list(numbers)
print("Average: ",average)

pass


# 16
def task16_factorial(n):
    """
    Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
    """
    result =1
    for i in range(1,n+1):
        result *=i
    return result
num=10
print(task16_factorial(num))
pass


# 17
def task17_palindrome_check(word):
    """
    Task 17:
    Write a function that checks if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    Example: palindrome_check("madam") → True
    """
    return word ==word[::-1]
print(task17_palindrome_check("hello"))
print(task17_palindrome_check("madam"))
print(task17_palindrome_check("dad"))
pass


# 18
def task18_convert_minutes_to_hours(minutes):
    """
    Task 18:
    Write a function that accepts minutes as input
    and converts it into hours and minutes.
    Example: 130 minutes → "2 hour(s) 10 minute(s)"
    """
    hours= minutes // 60
    remaining_minutes = minutes % 60
    print(f"{hours} hours and {remaining_minutes} minutes")

minutes=int(input('Enter minutes: '))
task18_convert_minutes_to_hours(minutes)
pass


# 19
def task19_find_min(numbers):
    """
    Task 19:
    Write a function that accepts a list of numbers
    and returns the smallest number.
    Do not use Python's built-in min() function.
    """
    smallest= numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
numbers=[900,0,3,4,5,6,7]
print(task19_find_min(numbers))
pass


# 20
def task20_simple_interest(principal, rate, time):
    """
    Task 20:
    Write a function that calculates simple interest.
    Formula: (principal * rate * time) / 100
    """
    return (principal * rate * time )/100
interest=task20_simple_interest(1000,5,5)
print(interest)
pass


# 21
def task21_calculator(a, b, operation):
    """
    Task 21:
    Write a function that works like a simple calculator.
    It should accept two numbers and an operation (+, -, *, /)
    and return the result.
    Example: calculator(4, 2, "+") → 6
    """
    if operation== "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        if b !=0:
            return a/b
        else:
            return "Error: Division by zero"
    else:
       return "Error: Invalid"
result= task21_calculator(4,34,"*")
print(result)
pass


# 22
def task22_string_length(text):
    """
    Task 22:
    Write a function that accepts a string
    and returns its length without using len().
    """
    str_len=0
    for i in text:
        str_len+=1
    return str_len    
print(task22_string_length("hello"))
pass


# 23
def task23_grade_student(score):
    """
    Task 23:
    Write a function that accepts a score (0–100)
    and returns the grade based on this scale:
    A: 70–100
    B: 60–69
    C: 50–59
    D: 40–49
    E: 30–39
    F: 0–29
    """
    if score >=70 and score <=100:
        return "Grade A"
    elif score >=60 and score <=69:
        return "Grade B"
    elif score >=50 and score <=59:
        return "Grade C"
    elif score >= 40 and score <=49:
        return "Grade D"
    elif score >=30 and score <=39:
        return "Grade E"
    elif score >=0 and score <=29:
        return "Grade F"
    else:
        return "Invalid Operation"
print(task23_grade_student(0))    
pass


# 24
def task24_swap_values(a, b):
    """
    Task 24:
    Write a function that accepts two values
    and returns them swapped.
    Example: swap_values(3, 7) → (7, 3)
    """
    return b,a
print(task24_swap_values(8,6))
pass


# 25
count=0
def task25_scope_counter():
    """
    Task 25:
    Create a counter function that uses a global variable.
    Each time the function is called, it should increase
    the counter by 1 and print the current count.
    This demonstrates modifying global variables inside functions.
    """
    global count
    count += 1
    print(count)
task25_scope_counter()    
task25_scope_counter()
task25_scope_counter()
task25_scope_counter()
task25_scope_counter()
task25_scope_counter()

pass


# ================================
# ADDITIONAL 25 FUNCTION TASKS
# ================================

# 26
def task26_calculate_bmi(weight, height):
    """
    Task 26:
    Write a function that accepts weight (kg) and height (m),
    and returns the Body Mass Index (BMI).
    Formula: BMI = weight / (height^2)
    Round the result to 2 decimal places.
    """
    bmi= weight / (height **2)
    return (round(bmi,2))
print(task26_calculate_bmi(70,1.75))
pass


# 27
def task27_discounted_price(price, discount_percent):
    """
    Task 27:
    Write a function that accepts an item's price and discount percentage,
    and returns the final price after discount.
    Example: discounted_price(1000, 20) → 800
    """
    discount= price *(discount_percent/100) 
    discounted_price=price-discount
    return discounted_price
print(task27_discounted_price(1000,20))
pass


# 28
def task28_movie_ticket_price(age):
    """
    Task 28:
    Write a function that determines ticket price based on age:
    - Age < 12: 500
    - 12 <= Age < 18: 700
    - 18 <= Age < 60: 1000
    - Age >= 60: 600
    Return the ticket price.
    """
    if age <12 :
        return "Ticket price is 500"
    elif age <=12 and age <18:
        return "Ticket price is 700"
    elif age <=18 and age <60:
        return "Ticket price is 1000"
    elif age >=60:
        return "Ticket price is 600"
    else:
        return "Invalid input"

print(task28_movie_ticket_price(9))    
pass


# 29
def task29_shopping_total(prices):
    """
    Task 29:
    Write a function that accepts a list of item prices
    and returns the total cost of all items.
    """
    return sum(prices)
items={"Bread":50,"milk":70,"butter":50}
prices=list(items.values()) 
print(task29_shopping_total(prices))     
pass


# 30
def task30_convert_to_seconds(hours, minutes, seconds):
    """
    Task 30:
    Write a function that accepts hours, minutes, and seconds
    and converts the entire time to total seconds.
    Example: 1h 1m 1s → 3661 seconds
    """
    total_seconds = (hours *3600) + (minutes * 60) + seconds
    return total_seconds
print(task30_convert_to_seconds(1,1,1))
pass


# 31
def task31_find_median(numbers):
    """
    Task 31:
    Write a function that accepts a list of numbers
    and returns the median value.
    (Hint: Sort the list first, then handle odd/even length cases.)
    """
    sorted_numbers =sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 ==0:
        median =(sorted_numbers[length // 2-1] + sorted_numbers[length // 2])/2
    else:
        median = sorted_numbers[length//2]
    
    return median
print(task31_find_median([1,2,3,4,5,6,7,8,9]))
pass


# 32
def task32_parking_fee(hours):
    """
    Task 32:
    Write a function that calculates parking fees:
    - First 2 hours: 200 Naira flat
    - Every additional hour: 100 Naira
    Example: parking_fee(5) → 200 + 3*100 = 500
    """
    if hours<= 2:
        return 200
    else:
        return 200 + (hours-2) *100

print(task32_parking_fee(5))
pass


# 33
def task33_word_count(sentence):
    """
    Task 33:
    Write a function that accepts a sentence
    and returns the number of words in it.
    Example: "I love Python" → 3
    """
    return len(sentence.split())
print(task33_word_count("I love me"))
pass


# 34
def task34_capitalize_names(names):
    """
    Task 34:
    Write a function that accepts a list of names in lowercase
    and returns a new list with each name capitalized.
    Example: ["john", "mary"] → ["John", "Mary"]
    """
    capitalised_names=[]
    for name in names :
        name = name.capitalize()
        capitalised_names.append(name)
    return capitalised_names
print(task34_capitalize_names(["sarah","yousuf"]))
pass


# 35
def task35_student_pass_fail(score):
    """
    Task 35:
    Write a function that accepts a student's score
    and returns "Pass" if score >= 50, otherwise "Fail".
    """
    if score >=50:
        return "Pass"
    else:
        return "Fail"
print(task35_student_pass_fail(46))
pass


# 36
def task36_calculate_fine(days_late):
    """
    Task 36:
    Write a function that calculates library book fine:
    - First 5 days: 20 per day
    - 6–10 days: 50 per day
    - Beyond 10 days: 100 per day
    Example: calculate_fine(7) → 5*20 + 2*50 = 200
    """
    if days_late <=5:
        return days_late *2
    elif days_late <=10:
        return 5*20 +(days_late -5) *10
    else:
        return 5 * 20 + 5* 50 +(days_late-10)*100
print(task36_calculate_fine(6))    
pass


# 37
def task37_convert_currency(amount, rate):
    """
    Task 37:
    Write a function that converts money from one currency to another
    using a given conversion rate.
    Example: convert_currency(100, 1500) → 150000
    """
    return amount * rate
print(task37_convert_currency(100,1500))
pass


# 38
def task38_gas_station_bill(liters, price_per_liter):
    """
    Task 38:
    Write a function that accepts the number of liters purchased
    and the price per liter, then returns the total cost.
    """
    return liters * price_per_liter
print(task38_gas_station_bill(50,120))
pass


# 39
def task39_is_leap_year(year):
    """
    Task 39:
    Write a function that accepts a year and returns True if it is a leap year,
    otherwise False.
    Rule: Year divisible by 4 → leap year, but divisible by 100 → not leap,
    unless divisible by 400.
    """
    return year %4 ==0 and (year % 100 !=0 or year % 400 ==0)
print(task39_is_leap_year(2025))
pass


# 40
def task40_password_strength(password):
    """
    Task 40:
    Write a function that checks password strength:
    - Length >= 8
    - Contains at least one digit
    - Contains at least one uppercase letter
    Return "Strong" if all conditions are met, otherwise "Weak".
    """
    if  (len(password) >=8 and any(char.isdigit() for char in password) and any (char.isupper() for char in password)):
        return "Strong"
    else:
        return "Weak"
print(task40_password_strength("sbhfkfuewyroi978HHk"))    
pass


# 41
def task41_shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
    """
    Task 41:
    Write a function to calculate the total price of a shirt order.
    - If quantity >= discount_threshold, apply discount_rate.
    Example: shirt_order(12, 2000) → discounted price
    """
    total_price= quantity * price_per_shirt
    if quantity >= discount_threshold:
        total_price *=(1- discount_rate)
    return total_price    
print(task41_shirt_order(300,10))
pass


# 42
def task42_find_mode(numbers):
    """
    Task 42:
    Write a function that finds the mode (most frequent number) in a list.
    If there are multiple modes, return any one of them.
    """
   # from collections import counter
    #counts = counter(numbers)
   # return max(counts,key=counts.get)
#print(task42_find_mode([1,2,3,33,4,7,3,4,5,6,6,7,7,8]))
pass


# 43
def task43_student_average(scores):
    """
    Task 43:
    Write a function that accepts a dictionary of subject:score
    and returns the student's average score.
    Example: {"math": 80, "english": 70} → 75.0
    """
    return sum(scores.values())/ len(scores)
print(task43_student_average({"math":80,"english":70}))
pass


# 44
def task44_calculate_age(current_year, birth_year):
    """
    Task 44:
    Write a function that accepts current year and birth year,
    and returns the age.
    Example: calculate_age(2025, 2000) → 25
    """
    return current_year- birth_year
print(task44_calculate_age(2025,1995))
pass


# 45
def task45_salary_after_tax(salary, tax_rate=0.15):
    """
    Task 45:
    Write a function that calculates net salary after deducting tax.
    Example: salary_after_tax(100000) → 85000
    """
    return salary * (1-tax_rate)
print(task45_salary_after_tax(100000))
pass


# 46
def task46_water_bill(units):
    """
    Task 46:
    Write a function to calculate water bill based on units:
    - First 30 units → 50 per unit
    - Next 20 units → 75 per unit
    - Beyond 50 units → 100 per unit
    """
    if units <=30:
        return units * 0.50
    elif units <=50:
        return 30 *0.50 +(units -30) * 0.75
    else:
        return 30 * 0.50 + 20 *0.75 +(units-50) *1.00

print(task46_water_bill(70))    
pass


# 47
def task47_find_longest_word(sentence):
    """
    Task 47:
    Write a function that accepts a sentence
    and returns the longest word in it.
    Example: "I love programming" → "programming"
    """
    words = sentence.split()
    return max(words, key=len)
print(task47_find_longest_word("my name is gotom"))
pass


# 48
def task48_banking_withdraw(balance, withdraw_amount):
    """
    Task 48:
    Write a function to simulate ATM withdrawal.
    - If withdraw_amount <= balance, return new balance
    - Otherwise return "Insufficient funds"
    """
    if withdraw_amount <= balance:
        return balance - withdraw_amount
    else:
        return "Insuficient Funds"
print(task48_banking_withdraw(10000,3569))
pass


# 49
def task49_calculate_grade_point(score):
    """
    Task 49:
    Write a function that converts score (0–100) into grade points:
    - 70–100 → 5
    - 60–69 → 4
    - 50–59 → 3
    - 45–49 → 2
    - 40–44 → 1
    - <40 → 0
    """
    if score >=70 and score <=100:
        return 5
    elif score >=60 and score <=69:
        return 4
    elif score >=50 and score <=59:
        return 3
    elif score >=40 and score <=49:
        return 2
    elif score >=30 and score <=39:
        return 1
    else:
        return 0
print(task49_calculate_grade_point(45))    
pass


# 50
def task50_weather_advice(temperature, raining):
    """
    Task 50:
    Write a function that gives advice based on weather:
    - If raining → "Take an umbrella"
    - Else if temperature > 30 → "Wear light clothes"
    - Else if temperature < 15 → "Wear a jacket"
    - Else → "Weather is fine"
    """
    if raining :
        return " Take an umbrella"
    elif temperature >30:
        return "Wear light clothes"
    elif temperature > 15:
        return "Wear a Jacket"
    else:
        return "Weather is fine"
print(task50_weather_advice(0,0))    
pass
