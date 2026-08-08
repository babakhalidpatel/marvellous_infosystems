#write a python program that schedules a function to print
# coding kar...
# every 30 minutes

def print_message():
    print("coding kar...")

def main():
    import schedule
    import time

    # Schedule the print_message function to run every 30 minutes
    schedule.every(30).minutes.do(print_message)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting
if __name__ == "__main__":
    main()

