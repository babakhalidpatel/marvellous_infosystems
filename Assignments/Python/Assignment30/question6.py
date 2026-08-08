# write a script that scedules a following task
# Print Lunch time every day at 1 pm
# print wrap up work every day at 6 pm

def print_lunch_time():
    print("Lunch time...")

def print_wrap_up_work():
    print("Wrap up work...")

def main():
    import schedule
    import time

    # Schedule the print_lunch_time function to run every day at 1:00 PM
    schedule.every().day.at("13:00").do(print_lunch_time)

    # Schedule the print_wrap_up_work function to run every day at 6:00 PM
    schedule.every().day.at("18:00").do(print_wrap_up_work)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting


if __name__ == "__main__":
    main()

