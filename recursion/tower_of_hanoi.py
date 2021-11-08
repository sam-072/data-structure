#  Sam._.072   :)
# here we will discuss the famous problem tower of hanoi. Basically the problem is we have 3 pole with different disk and we have to move
# all the disk from pole 1 to pole 3 with the help of pole 2. The rule is at a time we can only move a single disk and larger disk should 
#  not the placed over the smaller dsik

# we can slove this problem using recursion , first we move the top n-1 disk to 2nd pole i.e B and then we move the last disk from 1st pole
# i.e A to 3rd ploe i.e C and and again transer all the disks on the 2nd pole to 1st pole using 3rd pole. here at this stage we successfully
# transfer your last disk to 3rd pole and we recusrive repeat the above process. thus we successfully transfer all disks from 1st pole to
# 3rd pole 
# here n: is the total no of disks
# a is the first pole 
# b is the helper pole
# c is the final pole or 3rd pole

def tower_of_hanoi(n,a,b,c):
    count=1
    if n==0:
        return 0
    if n>0:
        count+=tower_of_hanoi(n-1, a, c, b)
        print(a,c)
        count+=tower_of_hanoi(n-1, b, a, c)
    return count

if __name__=='__main__':
    print(tower_of_hanoi(5, 1, 2, 3))