def add_time(start, duration, day=""):
  start_hour = start.split(':')[0]
  start_minutes = (start.split(':')[1]).split(' ')[0].lstrip('0')
  start_ampm = (start.split(':')[1]).split(' ')[1]

  print(start_hour, start_minutes, start_ampm)



  return new_time

