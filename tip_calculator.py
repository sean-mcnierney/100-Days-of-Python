print("Welcome to the tip calculator!")

float_payment = float(input("What was the total bill? $"))

tip_percentage = int(input("How much would you like to tip?, 10, 12, or 15? ")) / 100

tip_amount =  float_payment * tip_percentage

total_amount = float_payment + tip_amount

num_of_people = int(input("How many people will split the bill?"))

total_per_person = total_amount / num_of_people

print(f"Each person should pay: ${total_per_person:.2f}")

#This tip calculator takes in 3 inputs. Total bill, the percentage of tip you would like to give, and how many people are splitting the bill. 
#It will calculate the tip and add it onto the total bill and then divide by how many people are in the party to give the total each person should pay