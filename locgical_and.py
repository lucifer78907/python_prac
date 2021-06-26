#AND --- TRUE only and only if both the inputs are true (1).
age = int(input("Enter a age"))
if age<=0:
    print("Invalid Input")
    exit()
if age==18 or age==19:
    print("Just an adult")
elif age<18 and age>=6:
    print("Just a teenager")
elif age<6:
    print("Just a kiddo")
else:
    print("ADULT")