# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Age categorization
if age < 13:
    category = "a Child"
elif age < 20:
    category = "a Teenager"
elif age < 60:
    category = "an Adult"
else:
    category = "a Senior Citizen"

# Personalized message
print("\nHello", name + "!")
print("You are", age, "years old and you are", category + ".")
print("It's great that you enjoy", hobby + "!")