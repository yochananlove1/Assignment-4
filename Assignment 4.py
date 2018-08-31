#write a python program that takes 2 lists and returns through if they have atleast one common member
def common_data (list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print (common_data([1,2,3,4,5], [5,6,7,8,9]))
print (common_data([1,2,3,4,5], [6,7,8,9]))
#write a python program to append a list to another list
list1 = ['Tunji', 'Debola', 'Femi', 'Tobi', 'Kemi']
list2 = ['12', '45', '10']
final_list = list1 + list2
print (final_list)
#write a python program to convert a list of multiple intergers into a single integer
L = [5,15,25,35,45,55,65,75,85,95]
print ('Original List: ', L)
x = int(''.join(map(str, L)))
print ('Single Integer: ', x)
