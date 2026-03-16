# Function to check FizzBuzz logic
def fizzbuzz_logic(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# Main program
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, 51):
    result = fizzbuzz_logic(i)
    print(result)

    if result == "FizzBuzz":
        fizzbuzz_count += 1
    elif result == "Fizz":
        fizz_count += 1
    elif result == "Buzz":
        buzz_count += 1

# Print counts
print("\n--- Count Summary ---")
print("Fizz count:", fizz_count)
print("Buzz count:", buzz_count)
print("FizzBuzz count:", fizzbuzz_count)


