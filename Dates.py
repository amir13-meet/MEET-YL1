                                                                ### Dates

#####################################################

months_def = {}
var = ""

#####################################################

def months():
    global months_def
    months_def["01"] = "January"
    months_def["02"] = "February"
    months_def["03"] = "March"
    months_def["04"] = "April"
    months_def["05"] = "May"
    months_def["06"] = "June"
    months_def["07"] = "July"
    months_def["08"] = "August"
    months_def["09"] = "September"
    months_def["10"] = "October"
    months_def["11"] = "November"
    months_def["12"] = "December"

#####################################################

def SwapValue(month):
    global months_def
    global var
    for k, v in months_def.iteritems():
        if (month == k):
            var = v
    return var

#####################################################

def PrintDate_mm_dd(month, day, year):
    print month + " " + day + " " + year

#####################################################

def PrintDate_dd_mm(day, month, year):
    print day + " " + month + " " + year

#####################################################    

def mm_dd_yy():
    string = AskDatemm()
    months()
    month = string[0:2] # string[0:2] // month in mm_dd_yy
    day = string[3:5] # string[3:5] // day in mm_dd_yy
    year = string[6:len(string)] # string[6:len(string)] //year
    month = SwapValue(month)
    PrintDate_mm_dd(month, day, year)

#####################################################

def dd_mm_yy():
    string = AskDatedd()
    months()
    day = string[0:2] # string[0:2] // day in dd_mm_yy
    month = string[3:5] # string[3:5] // month in dd_mm_yy
    year = string[6:len(string)] # string[6:len(string)] //year
    month = SwapValue(month)
    PrintDate_dd_mm(day, month, year)

#####################################################

def AskDatemm():
    x = raw_input("Enter the date: ")
    return x

#####################################################

def AskDatedd():
    x = raw_input("Enter the date: ")
    return x

#####################################################

def AskDateKind():
    answer = raw_input("mm_dd_yy  or  dd_mm_yy?: ")
    while (answer != "mm_dd_yy") and (answer != "dd_mm_yy"):
        print "Enter your answer exactly as printed for you"
    if (answer == "mm_dd_yy"):
        mm_dd_yy()
    else:
        dd_mm_yy()

#####################################################
#####################################################

if __name__ == "__main__":            
    AskDateKind()
    
