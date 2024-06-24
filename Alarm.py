import time
import winsound

# Function to set an alarm
def set_alarm():
    try:
        # Input alarm time from the user
        alarm_time = input("Enter the alarm time (HH:MM): ")

        # Parse the user input
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

        while True:
            # Get the current time
            current_time = time.localtime()
            current_hour, current_minute = current_time.tm_hour, current_time.tm_min

            # Check if it's time for the alarm
            if current_hour == alarm_hour and current_minute == alarm_minute:
                print("Time's up")
                # Play a sound (Windows-specific)
                winsound.Beep(1000, 3000)  # Beep at 1000 Hz for 1 second
                break

            # Wait for one minute before checking again
            time.sleep(60)

    except ValueError:
        print("Invalid time format. Please use HH:MM.")

# Set the alarm
set_alarm()
