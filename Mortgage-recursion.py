# This program calculates the amount of a loan with compounded interest using recursion.
# The function recursively applies monthly interest to the principal for a given number of months.

def compound_interest_recursive(principal, time_in_years, rate, months=0):
    # Base case: if the number of months has reached the total compounded months
    total_months = time_in_years * 12
    if months == total_months:
        return principal
    # Recursive case: apply monthly interest and call the function for the next month
    return compound_interest_recursive(principal * (1 + (rate / 12)), time_in_years, rate, months + 1)

# Driver Code
# Test the function with example values
principal = 4500000
time_in_years = 15
rate = 0.0675
result = compound_interest_recursive(principal, time_in_years, rate)

# Format the result with commas for thousands and rounded to two decimal places
formatted_result = f"${result:,.2f}"

# Print the result
print(f"The final amount after {time_in_years} years is: {formatted_result}")
