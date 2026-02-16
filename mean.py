# This script calculates the mean of a list of numbers provided as input.

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == "__main__":
    try:
        # Accept input from the user
        user_input = input("Enter a list of numbers separated by spaces: ")
        # Convert the input string to a list of floats
        numbers = list(map(float, user_input.split()))
        # Calculate the mean
        mean = calculate_mean(numbers)
        print(f"The mean of the numbers is: {mean}")
    except ValueError:
        print("Please enter valid numbers.")