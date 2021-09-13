l=[]
n=int(input("Enter number of process : "))
print("Enter process No Arrival Time CPU Burst and Priority")
at=dict()
bt=dict()
for i in range(n):
    l.append(list(map(int,input().split())))
    at[l[i][0]]=l[i][1]
    bt[l[i][0]]=l[i][2]

l=sorted(l,key=lambda x: (x[1],x[2],x[3]))
GanttChart=dict()
completionTime=n*[0]
p=0
for i in l:
    p+=i[2]
    completionTime[i[0]-1]=p
    GanttChart[i[0]]=p
print("\nGantt Chart : ")
print(GanttChart)
print()
print("TurnAround Time for each process : ")
tat=[]
p=0
for i in range(1,n+1):
    print("TAT for process ",i," is : ",completionTime[i-1]-at[i])
    tat.append(completionTime[i-1]-at[i])

print("\nAverage TAT is : ",sum(tat)/n)
print()
wt=[]
p=0
print("Waiting time for each process : ")
for i in range(1,n+1):
    print("Waiting Time for process ",i," is : ",tat[i-1]-bt[i])
    p+=tat[i-1]-bt[i]
print("\nAverage waiting time is : ",p/n)
