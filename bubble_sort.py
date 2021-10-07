"""
def bubble_sort(elements):
    for i in range(len(elements)-1):
        for j in range(len(elements)-1):
            if elements[j]>elements[j+1]:

                tmp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=tmp



elements=list(map(int,input().split()))
bubble_sort(elements)
print(elements)

"""

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

arr=[2,3,5,1,9]
print(search(arr,5))