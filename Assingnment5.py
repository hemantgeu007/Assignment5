'''1'''
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

'''2'''
l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
if l == b :
    print("The Dimensions are of Square")
else:
    print("The Dimensions are of Rectangle")

'''3'''
age1 = int(input("Enter the Age of 1st Person"))
age2 = int(input("Enter the Age of 2nd Person"))
age3 = int(input("Enter the Age of 3rd Person"))
if age1 >= age2:
    if age3 >= age1:
        print("Third person is oldest")
        print("Second person is youngest")
    else:
        print("First person is oldest")
        if age3 >= age2:
            print("Second person is youngest")
        else:
            print("Third person is youngest")
else:
    if age3 >= age2:
        print("Third person is oldest")
        print("First person is youngest")
    else:
        print("Second person is oldest")
        if age3 >= age1:
            print("First person is youngest")
        else:
            print("Third person is youngest")

'''Q4'''
point = int(input("Enter your points: "))
if 0 <= point <= 50 :
    print("Sorry! No prize this time")
elif 51 <= point <= 150 :
    print("Congratulations! You won a Wooden dog")
elif 151 <= point <= 180 :
    print("Congratulations! You won a Book")
elif 181 <= point <= 200 :
    print("Congratulations! You won Chocolates")

'''Q5'''
cost = 100
quantity = int(input("Enter the Quantity"))
price = cost * quantity
if price >= 1000 :
    price = price - (price * 0.1)
print("The total cost is ", price)