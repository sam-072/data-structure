# Code by : Sam._.072

# Time Complexity : 2^N

def subsetSum(index, a, sum, ans):
    if index >= len(a):
        ans.append(sum)
        return
    subsetSum(index+1, a, sum+a[index], ans)
    subsetSum(index+1, a, sum, ans)

if __name__ == '__main__':
    a = list(map(int, input().split()))
    ans = []
    subsetSum(0, a, 0, ans)
    print(ans)