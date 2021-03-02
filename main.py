import street2, world2, schedule

w=world2.World('e.txt')
schedule=schedule.Schedule.from_file('e_684786_inc')

print(w.simulate(schedule))
