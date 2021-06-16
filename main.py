from colorama import init, Fore, Back
init()
try:
    print(Fore.GREEN + "Welcome to BMI calculator!" + Fore.RESET)

    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    bmi = float("{0:.2f}".format(weight / ((height / 100) * (height / 100))))

except ZeroDivisionError:
    print("Please enter positive value!")
except ValueError:
    print("Please enter valid data!")

else:
    if (bmi < 16.99):
        print("Your BMI:", bmi)
        print(Fore.RED + "Severe underweight" + Fore.RESET)

    elif (bmi >= 16 and bmi < 18.49):
        print("Your BMI:", bmi)
        print(Fore.YELLOW + "Insufficient (deficiency) body weight" + Fore.RESET)

    elif (bmi >= 18.5 and bmi < 24.99):
        print("Your BMI:", bmi)
        print(Fore.GREEN + "Norm" + Fore.RESET)

    elif (bmi >= 25 and bmi < 29.99):
        print("Your BMI:", bmi)
        print(Fore.YELLOW + "Overweight (pre-obesity)" + Fore.RESET)

    elif (bmi >= 30 and bmi < 34.99):
        print("Your BMI:", bmi)
        print(Fore.RED + "First degree obesity" + Fore.RESET)

    elif (bmi >= 35 and bmi < 39.99):
        print("Your BMI:", bmi)
        print(Fore.RED + "Second degree obesity" + Fore.RESET)

    elif (bmi < 40):
        print("Your BMI:", bmi)
        print(Fore.RED + "Third degree obesity (morbid)" + Fore.RESET)

