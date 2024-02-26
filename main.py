seconds = input('Enter the number of seconds (integer): ')
seconds = int(seconds)
hours = seconds/3600
seconds%= 3600
minutes = seconds/60
seconds%=60
print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
