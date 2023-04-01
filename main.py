# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
n = int(input())
m = int(input())
def circular_array(n, m):

    array = list(range(1, n+1))

    current_index = 0
    path = []
    while array[current_index] not in path:
       path.append(array[current_index])
       current_index = (current_index + m - 1) % n

    return path
print(circular_array(n, m))

