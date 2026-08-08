# schedule a task that executes every 5 seconds
# The task should write current date and time to a file named:
# marvellous.txt
# new entris should append without removing the existing data in the file
# e.g.
# Task executed at: 25-07-2026 04:30:45 PM

def write_current_datetime_to_file():
    from datetime import datetime

    # Get the current date and time
    now = datetime.now()

    # Format the date and time as "DD-MM-YYYY HH:MM:SS AM/PM"
    formatted_datetime = now.strftime("%d-%m-%Y %I:%M:%S %p")

    # Write the current date and time to the file marvellous.txt
    with open("marvellous.txt", "a") as file:
        file.write(f"Task executed at: {formatted_datetime}\n")

def main():
    import schedule
    import time

    # Schedule the write_current_datetime_to_file function to run every 5 seconds
    schedule.every(5).seconds.do(write_current_datetime_to_file)

    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting

if __name__ == "__main__":
    main()


