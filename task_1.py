time_to_sum = '1h 45m,360s,25m,30m 120s,2h 60s'
time_to_sum = time_to_sum.split(',')
total_minutes = 0

for i in time_to_sum:
    separator = i.split(' ')
    for j in separator:
        if 'h' in j:
            j = j.replace('h', '')
            total_minutes += int(j) * 60
        elif 'm' in j:
            j = j.replace('m', '')
            total_minutes += int(j)
        elif 's' in j:
            j = j.replace('s', '')
            total_minutes += int(j) // 60

print(total_minutes)

