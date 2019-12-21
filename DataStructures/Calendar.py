import calendar
try:                  #using try block for different inputs
    yy = int(input("please enter the year")) #Asking the user to provide year
    mm = int(input("please enter the month in number format")) #Asking the user to provide month

    # display the calendar
    print(calendar.month(yy, mm))
except ValueError:     #using "except" to avoid errors
    print("provide valid data")