def binary_search(arr,l,r,x):
    if r >= l:
        mid = l + (r-l)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr,l,mid-1,x)
        
        else:
            return binary_search(arr,mid+1,r,x)
        
    else:
        return -1

xlist = input('Enter the sortd list : ')

xlist = xlist.split()
xlist = [int(x) for x in xlist]

key = int(input('The number to search for : '))

result = binary_search(xlist,0,len(xlist)-1,key)

if result != -1:
    print('{} was found at index {}.'.format(key, result))
else:
    print('  was not found .'%(key))

