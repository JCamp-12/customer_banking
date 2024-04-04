"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    my_savings = Account(balance=balance, interest=0)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = round(balance * (interest_rate/100 * months/12), 2)
    # print('interest earned', interest_earned)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    new_balance = round(balance + interest_earned, 2)
    # print('we got the new balance ', new_balance)

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    my_savings.set_balance(new_balance)
    
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    my_savings.set_interest(interest_earned)
    # print('we got the interest earned here ', my_savings.interest)

    # Return the updated balance and interest earned.
    # print('savings', my_savings)
    # print('we got the new balance ', my_savings.balance)
    # print('we got the interest earned here ', my_savings.interest)
    # ADD YOUR CODE HERE
    return my_savings.balance, my_savings.interest

# testing function
# create_savings_account(1000, 5, 12)