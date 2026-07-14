# The gate of numbers
#since all even number are divisible by 2 when a number is divided by 2 and there is no remainder it is an even number 
number = int(input('Enter a number: '))
if number % 2 ==0:
    print('The number you entered is an even number')
else:
    print('The number is an odd number')

#Quest 2 - The Academy Exams
#  
marks = int(input('Enter your score between 0-100: '))
x = marks 
if x >= 50:
    print('You passed the Exams')
else:
    print('You failed')


#Quest 3-The wizard Grades
#let x be the marks scored by the students  

mark = float(input('Enter your marks between 0 and 100: '))
x = mark
if x>=100 and  x<=80:
    print('You had grade A')
elif x>=79 and  x<=70:
    print("You had grade B")
elif x>=69 and  x<=60:
    print('You had grade C')
elif x>=59 and  x<=50:
    print('You had grade D')
elif x<=50:
    print('You had grade F')

#quest 4 the village of ages 

age= int(input('Enter your age: '))
# let variable age be an variable x 
age = x
if  x>=12 and x<=0:
     print('Child')
elif x>=19 and  x<=13:
    print('Teenager')
elif x>=59 and x<=20:
    print('Adult')
else:
     print('Senior')

#Quest 6 The magric Calculation 
operator=input('Enter an operator(+,-,*/): ')
num_1=float(input('Enter your first number: '))
num_2=float(input('Enter your second number: '))
if operator =='+':
    result = num_1 + num_2
    print(result)
elif operator =='-':
    result = num_1-num_2
    print(result)
elif operator=='*':
    result=num_1*num_2
    print(result)
elif operator=='/':
    result=num_1 / num_2

#guess the secret number which is 7
check_guess =float(input('Enter the secret number: '))
if check_guess == 7:
    print('Congratulation')
elif check_guess >7:
    print('Too high')
elif check_guess <7:
    print('Too low')

#the royal bank
#I am still not getting functions that well ,for this activity i was equired to use it











#final boss
username=str(input('Enter the username: '))
password=input('Enter the password')
if username == 'admin' and password == 'python123':
    print('Login Successful')
else:
    print('Access Denied')




