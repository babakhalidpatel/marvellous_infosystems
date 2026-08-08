# write a python program that performs file backup every hour
# the program
# Accept the source file path
# Accept the destination file path
# Copy the contents of source file to destination file
# and the current date and time to backup filename
# write the backup operation details into:
#backup_log.txt
# example backfile name

#Data_25_07_2026_14_30_45.txt
#Example log entry
# Backup operation performed at: 25-07-2026 14:30:45
# use the shutil module to perform file copy operation

def backup_file(source_file, destination_folder):
    import os
    import shutil
    from datetime import datetime

    # Check if the source file exists
    if not os.path.isfile(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    # Get the current date and time for backup filename
    now = datetime.now()
    formatted_datetime = now.strftime("%d_%m_%Y_%H_%M_%S")
    backup_filename = f"Data_{formatted_datetime}.txt"
    backup_filepath = os.path.join(destination_folder, backup_filename)

    # Copy the source file to the destination folder with the new backup filename
    shutil.copy2(source_file, backup_filepath)

    # Log the backup operation details into backup_log.txt
    log_entry = f"Backup operation performed at: {now.strftime('%d-%m-%Y %H:%M:%S')}\n"
    with open("backup_log.txt", "a") as log_file:
        log_file.write(log_entry)

    print(f"Backup completed: {backup_filepath}")

def main():
    import schedule
    import time

    # Accept source and destination paths from the user
    source_file = input("Enter the source file path: ")
    destination_folder = input("Enter the destination folder path: ")

    # Schedule the backup_file function to run every hour
    schedule.every().hour.do(backup_file, source_file=source_file, destination_folder=destination_folder)

    print("Backup scheduler started. Press Ctrl+C to stop.")
    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short duration to avoid busy waiting   

if __name__ == "__main__":
    main()

