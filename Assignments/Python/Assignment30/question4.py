#wcreate a task that executes a everyday at 9:00 am and prints
# Namskar...
# Use:
# schedule.every().day.at("09:00").do(...)

def print_message():
    print("Namskar...")

def main():
    import schedule
    import time

    # Schedule the print_message function to run every day at 9:00 AM
    schedule.every().day.at("09:00").do(print_message)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting

if __name__ == "__main__":
    main()

