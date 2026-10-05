age = int(input("Enter your age: "))

if age >= 18:
    print("Valid age. You are eligible for voting.")
elif age > 0 and age < 18:
    print("Valid age, but you are not eligible for voting yet.")
else:
    print("Invalid age entered.")