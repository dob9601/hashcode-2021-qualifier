import street2, world2, schedule

w=world2.World('a.txt')
schedule=schedule.Schedule.from_file('a_test') # d_ass_1583635

print(w.simulate(schedule))
