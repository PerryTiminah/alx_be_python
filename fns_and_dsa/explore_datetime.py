from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days, base_date):
    future_date = base_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

if __name__ == "__main__":
    current = display_current_datetime()

    try:
        user_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(user_input, current)
    except ValueError:
        print("Please enter a valid integer for number of days.")
