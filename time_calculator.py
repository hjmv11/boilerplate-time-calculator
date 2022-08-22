def add_time(start, duration, day=""):
  #array of all days
  days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  #create variables of start argument 
  start_day = (day.lower()).capitalize()
  start_day_index = 0
  #if start_day is not empty
  if start_day != "":
    start_day_index = days_of_week.index(start_day)
  start_hour = int(start.split(':')[0])
  start_minutes = int((start.split(':')[1]).split(' ')[0].lstrip('0'))
  start_ampm = (start.split(':')[1]).split(' ')[1]
  #set hour to 24hour time
  if start_ampm == 'PM':
    start_hour += 12

  #create blank variables for the new time and day 
  new_hour = 0
  new_minutes = 0
  new_ampm = ""
  days_passed = 0
  new_day_index = 0
  new_day = ""

  #create variables for duration argument 
  duration_days = 0
  duration_hours = int(duration.split(':')[0])
  #if duration hours is greater than or equal to 24, calculate the durations days and set hours to the remainder 
  if duration_hours >= 24:
    duration_days = duration_hours//24
    duration_hours = duration_hours%24
  duration_minutes = duration.split(':')[1].lstrip('0')
  #if duration minutes equal to 00 set to int 0 
  if duration_minutes == '':
    duration_minutes = 0

  #calculate new time and date variables 
  new_hour = start_hour + duration_hours
  new_minutes = start_minutes + int(duration_minutes)
  #if new minutes is greater than 60, calculate the hours and set minutes to the remainder
  if new_minutes >= 60:
    new_hour += new_minutes//60
    new_minutes = new_minutes%60
  #if new hour is greater than 24, calculate the additional days and set new hour to the remainder 
  if new_hour >=24:
    days_passed = duration_days + new_hour//24
    new_hour = new_hour%24
  else:
    days_passed = duration_days
  #set new day index by adding days passed
  new_day_index = start_day_index + days_passed
  #if new day index is greater than 6, set the remainder to new day index , set new day based on newer new day index
  if new_day_index > 6:
    new_day_index = new_day_index%7
  new_day = days_of_week[new_day_index]
  #if new hour is 0-11, set to AM, else set to PM 
  if 0 <= new_hour < 12:
    new_ampm = 'AM'
    if new_hour == 0:
      new_hour = 12
  else:
    #if new hour is 13-23, subtract by 12  
    if new_hour > 12:
      new_hour -= 12
    new_ampm = 'PM'
  

  #if day argument is empty, do not return new day 
  if day=="":
    #if days passed is greater than 1, return the number of days passed
    if days_passed > 1:
      return (f"{new_hour}:{str(new_minutes).rjust(2,'0')} {new_ampm} ({days_passed} days later)")
    else:
      #if days passed equals 1 then return next day
      if days_passed == 1:
        return (f"{new_hour}:{str(new_minutes).rjust(2,'0')} {new_ampm} (next day)")
      else: 
        return (f"{new_hour}:{str(new_minutes).rjust(2,'0')} {new_ampm}")
  else:
    if days_passed > 1:
      return (f"{new_hour}:{str(new_minutes).rjust(2,'0')} {new_ampm}, {new_day} ({days_passed} days later)")
    else:
      if days_passed == 1:
        return (f"{new_hour}:{str(new_minutes).rjust(2,'0')} {new_ampm}, {new_day} (next day)")
      else:
        return (f"{new_hour}:{str(new_minutes).rjust(2,'0')} {new_ampm}, {new_day}")
          
