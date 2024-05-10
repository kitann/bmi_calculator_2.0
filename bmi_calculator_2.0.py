# accept user input for weight and height
weight = input("Enter Weight: ")
height = int(input("Enter HEIGH: "))

# calculate BMI
bmi = weight / (height * height)

if bmi <= 18.5:
  print(f"Your BMI is {bmi}, you are UNDERWEIGHT")
elif bmi < 25:
  print(f"Your BMI is {bmi}, You have a NORMAL WEIGHT")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are OVERWEIGHT")
elif bmi < 35:
  print(f"Your BMI is {bmi}, You are CLINICALLY OBESE")
else:
  print("Your are OBESE")

