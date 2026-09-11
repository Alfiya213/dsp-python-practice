Program 1: Linear Search
def linear_search(arr, key):
for i in range(len(arr)):
if arr[i] == key:
return i
return -1
arr = [10, 25, 30, 45, 60]
key = 30
result = linear_search(arr, key)
if result != -1:
print(&quot;Element found at index:&quot;, result)
else:
print(&quot;Element not found&quot;)

�� Program 2: Binary Search
def binary_search(arr, key):
low = 0
high = len(arr) - 1
while low &lt;= high:
mid = (low + high) // 2
if arr[mid] == key:
return mid
elif arr[mid] &lt; key:
low = mid + 1
else:
high = mid - 1
return -1
arr = [10, 20, 30, 40, 50]
key = 40
print(&quot;Index:&quot;, binary_search(arr, key))
