import datetime
import time
import smtplib  # For sending email notifications
from plyer import notification  # For desktop notifications (install with: pip install plyer)
import winsound


# Function to set a reminder
def set_reminder(reminder_text, reminder_time):
    try:
        # Parse the reminder time with the correct format 'YYYY-MM-DD HH:MM:SS'
        reminder_time = datetime.datetime.strptime(reminder_time, '%Y-%m-%d %H:%M')

        # Calculate the time difference in seconds
        time_diff = (reminder_time - datetime.datetime.now()).total_seconds()

        if time_diff <= 0:
            print("The reminder time should be in the future.")
            return

        # Sleep until the reminder time
        time.sleep(time_diff)

        # Send a desktop notification
        notification.notify(
            title='Reminder',
            message=reminder_text,
            app_name='Reminder App',
            timeout=10  # Notification display time in seconds
        )

        # Optionally, send an email notification (requires a configured email server)
        send_email_notification(reminder_text)

    except ValueError:
        print("Invalid date/time format. Please use 'YYYY-MM-DD HH:MM:SS' format.")

# Function to send an email notification (SMTP configuration required)
def send_email_notification(message):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 535
        smtp_username = 'promotingthebest2008@gmail.com'
        smtp_password = 'nowadays3435'

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        subject = 'Reminder'
        body = message
        from_email = 'promotingthebest2008@gmail.com'
        to_email = 'promotingthebest2008@gmail.com'

        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(from_email, to_email, msg)
        server.quit()
        print("Email notification sent successfully.")

    except Exception as e:
        print(f"Error sending email notification: {e}")

# Input reminder details from the user
reminder_text = input("Enter the reminder text: ")
reminder_ime = input("Enter the reminder date and time (HH:MM): ")
reminder_time = (f"{datetime.datetime.now():%Y-%m-%d}"+" "+reminder_ime)

# Set the reminder
set_reminder(reminder_text, reminder_time)
