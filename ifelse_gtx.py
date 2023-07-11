marks = int(input("Please enter your marks!\t"))

if marks <= 1 or marks >= 100: 
    print("Warrning! You have entered wrong marks enter correct marks!")
elif marks >= 50 and marks <= 100:
    print("Congratulations! You are Pass \nWe see you next year!")
else:
    print("Sorry! you are Fail Needs improvement \nWe see you next year!")