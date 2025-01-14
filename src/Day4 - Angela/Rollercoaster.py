print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Yay! You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age < 45:
        bill = 12
        print("Adult tickets are $12.")
    elif age < 55:
        bill = 0
        print("Have a safe ride! Tickets on us.")
    else:
        print("You can't ride")
    want_photos = input("Do you want to take photos? Y or N ")
    if want_photos == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")

else:
    print("You have to grow taller to ride!")
