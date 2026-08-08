#write a python program that prints
# Jay Ganesh...
# every two seconds
# scheudle.every(2).Secods.do(...)

def print_message():
    print("Jay Ganesh...")

def main():
    import schedule
    import time

    # Schedule the print_message function to run every 2 seconds
    schedule.every(2).seconds.do(print_message)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting

if __name__ == "__main__":
    main()