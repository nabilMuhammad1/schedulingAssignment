quantum=input('Enter quantum time:')
type(quantum)
processes=[0]*10
index=0
i=0
j=0
k=0
time=0

processes[0]=dictt={}
processes[1]=dictt={}
processes[2]=dictt={}

processes[0]['P_id']='p1'
processes[1]['P_id']='p2'
processes[2]['P_id']='p3'

processes[0]['arr_t']=0
processes[1]['arr_t']=5
processes[2]['arr_t']=2

processes[0]['burst_t']=9
processes[1]['burst_t']=3
processes[2]['burst_t']=5

for i in range(3):
	for j in range(2-i):
		if processes[j]['arr_t']>processes[j+1]['arr_t']:
			temp={}
			temp=processes[j]
			processes[j]=processes[j+1]
			processes[j+1]=temp

check='true'

for i in range(3):
	processes[i]['remaining_burst']=processes[i]['burst_t']

for j in range(3):
	check='true'
	if processes[j]['remaining_burst']>0:
		check='false'
		if processes[j]['remaining_burst']>quantum:
			time= time+ quantum
			processes[j]['remaining_burst'] = processes[j]['remaining_burst']-quantum
	else:
		time= time+ processes[j]['remaining_burst']
		processes[j]['wait_time']= time-processes[j]['arr_t']-processes[j]['burst_t']
		processes[j]['remaining_burst']=0

	if check=='true':
		break
for k in range(3):
	processes[k]['turnaround_time']=time-processes[k]['arr_t']
avgturntime=0
k=0
for k in range(3):
	print processes[k]
	avgturntime=avgturntime+processes[k]['turnaround_time']
avgturntime=avgturntime/3
print 'Average Turnaround Time'
print(avgturntime)
