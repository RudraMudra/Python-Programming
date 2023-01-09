lst = []

num = int(input("Enter the size of list : "))

for n in range(num):
    numbers = (int(input("Enter the array of %d element :- "%n)))
    lst.append(numbers)

x = int(input("Enter number to search in list : "))

def rec_linear_search(arr, l, r, x):
    if r<l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return rec_linear_search(arr,l+1,r-1,x)

res = rec_linear_search(lst,0,len(lst)-1,x)

if res != -1:
    print('{} was found at index {}.'.format(x,res))
else:
    print('{} was not found.'.format(x))