
from abc import ABC, abstractmethod

# Abstract class
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Email notification
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")


# SMS notification
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


# App notification
class AppNotification(Notification):
    def send(self, message):
        print(f"Sending App Notification: {message}")


# Create a list of notification objects
notifications = [
    EmailNotification(),
    SMSNotification(),
    AppNotification()
]

# Send the message using a for loop
for notification in notifications:
    notification.send("Enrollment is now open!")