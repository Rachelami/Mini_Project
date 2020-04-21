import datetime
import os


class Logger:
    def add_to_log(msg):
            try:
                f = open('C:\\Users\\rache\\PycharmProjects\\ITC Python\\mini_project\\logger.txt', "a+")
                x = datetime.datetime.now()
                f.write(x.strftime("%m-%d-%Y, %H:%M:%S") + msg)
            except OSError:
                try:
                    os.makedirs('C:\\Users\\rache\\PycharmProjects\\ITC Python\\mini_project\\logger.txt')
                except Exception as e:
                    print("something went wrong: " + str(e))

Logger.add_to_log(" log something \n")