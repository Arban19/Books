a = leave_time = 6 + 52/60
b = easy_pace = (8 + 15/60)/60
c = tempo = (7 + 12/60)/60

running_time_hr = 2 * easy_pace + 3 * tempo
breakfast_hrs = (leave_time + running_time_hr)
breakfast_min = (breakfast_hrs - int(breakfast_hrs))*60
breakfast_sec = (breakfast_min - int(breakfast_min))*60
print ('breakfast_hrs', int(breakfast_hrs))
print ('breakfast_min', int (breakfast_min))
print ('breakfast_sec', int (breakfast_sec))
