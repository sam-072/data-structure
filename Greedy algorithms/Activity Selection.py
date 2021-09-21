def activity_selction(activity,n):
    activity.sort(key= lambda x : x[1])
    c=1
    p=activity[0][1]
    for i in range(1,n):
        if activity[i][0] >= p:
            c+=1
            p=activity[i][1]
    return c

if __name__=='__main__':
    n=int(input())
    activity=[]
    for i in range(n):
        activity.append(list(map(int,input().split())))
    c=activity_selction(activity,n)
    print(c)