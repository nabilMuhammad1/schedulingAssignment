print('First come Fisrt serve')
arr_t = [0, 2, 4]
burst_t = [4, 3, 5]
wait_t = [0]*3
start_t = 0
finish_t = 0
turnaround_t= [0]*3
avg=0.0

for index in range(3):
	print 'Process', index
	finish_t = finish_t + burst_t[index]
	wait_t[index] = start_t - arr_t[index]
	print'Waiting Time:', wait_t[index]

        turnaround_time[index] = finish_t-arr_t[index]
	print'Turnaround Time:', turnaround_time[index]
	start_t= start_t+burst_t[index]
print 'Average Turnaround Time'
for k in range(3):
	avg=avg+turnaround_time[k]
avg=avg/3
print(avg)
