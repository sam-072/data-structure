# Code by : Sam._.072

# Time Complexity : O(N^2)
# Space Complexity : O(1)

def UniqueTriplet(arr):
    n = len(arr)
    arr.sort()
    c, ans = 0, []
    for i in range(n-2):
        if i == 0 or ( i > 0 and arr[i] != arr[i-1]):
            a = -1*arr[i]
            l, h = i+1, n-1
            while l < h:
                if arr[l] + arr[h] == a:
                    c += 1
                    ans.append([arr[i], arr[l], arr[h]])
                    t = arr[l]
                    while l < h and arr[l] == t:
                        l += 1
                    t = arr[h]
                    while l < h and arr[h] == t:
                        h -= 1
                elif arr[l] + arr[h] < a:
                    l += 1
                else:
                    h -= 1
    return c, ans

# Time Complexity : O(N^2 * log(M) )
# Space Complexity : O(M) for set + O(N) for hashmap

def UniqueTriplet1(arr):
    n = len(arr)
    c, ans = 0, []
    d = dict()
    d1 = dict()
    for i in arr:
        d[i] = d.get(i,0)+1
    for i in range(n-2):
        d[arr[i]] -= 1
        for j in range(i+1,n-1):
            d[arr[j]] -= 1
            if d.get(-1*(arr[i]+arr[j]),0)>0:
                l = [arr[i], arr[j], -1*(arr[i]+arr[j])]
                l.sort()
                l = tuple(l)
                if d1.get(l,False)==False:
                    c += 1
                    d1[l] = True
                    ans.append(list(l))           
            d[arr[j]] += 1
        d[arr[i]] += 1
    return c, ans






if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(UniqueTriplet(a))
    print(UniqueTriplet1(a))
                