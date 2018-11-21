process=['p1', 'p2', 'p3','p4']
arr_t = [0, 1, 3, 4]
burst_t = [4, 5, 3 ,5]
wait_t = [0]*4
start_t = 0
finish_t = 0
turnaround_t = [0]*4
minn=0
i=0
j=0
avg=0.0

for i in range(4):
	for j in range(2-i):
		if arr_t[j]>minn and burst_t[j]>burst_t[j+1]:
			temp=burst_t[j]
			burst_t[j]=burst_t[j+1]
			burst_t[j+1]=temp
			tem=arr_t[j]
			arr_t[j]=arr_t[j+1]
			arr_t[j+1]=tem
			t=process[j]
			process[j]=process[j+1]
			process[j+1]=t
	minn=burst_t[i]+minn

for index in range(4):
	print(process[index])
	
	finish_t = finish_t + burst_t[index]
	wait_t[index] = start_t - arr_t[index]
	print'Waiting Time:', wait_t[index]

        turnaround_t[index] = finish_t-arr_t[index]
	print'Turnaround Time:', turnaround_t[index]
	start_t= start_t+burst_t[index]

print 'Average Turnaround Time'
for k in range(4):
	avg=avg+turnaround_t[k]

avg=avg/4
print(avg)
