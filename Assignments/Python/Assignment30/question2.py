#write a python program that display
# current date and time every one second
# use the date time mdoule
# Current Date and Time: 25-07-206 04:30:45 PM

def display_current_datetime():
    from datetime import datetime

    # Get the current date and time
    now = datetime.now()

    # Format the date and time as "DD-MM-YYYY HH:MM:SS AM/PM"
    formatted_datetime = now.strftime("%d-%m-%Y %I:%M:%S %p")

    # Display the current date and time
    print(f"Current Date and Time: {formatted_datetime}")

def main():
    import schedule
    import time

    # Schedule the display_current_datetime function to run every 1 second
    schedule.every(1).seconds.do(display_current_datetime)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting

if __name__ == "__main__":
    main()