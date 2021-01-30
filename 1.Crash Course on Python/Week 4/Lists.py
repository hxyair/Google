def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("Nothing")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


def skip_elements(elements):
	# Initialize variables
	new_list = []
	newest_list=[]
	i = 0

	# Iterate through the list
	for element in elements:
		# Does this element belong in the resulting list?
		if elements[i] in elements:
			# Add this element to the resulting list
			new_list += [element]
		# Increment i
		i+=1
		newest_list=new_list[::2]

	return newest_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


def file_size(file_info):
	name, file_type, size= file_info
	return("{:.2f}".format(size/ 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


def skip_elements(elements):
	# code goes here
    list = []
    for index,element in enumerate(elements):
        if index % 2 == 0:
            list.insert(index, element)
#            list.append(element) 
    return list 
#    element = [e for i, e in enumerate(elements) if i % 2 == 0]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']



def full_email(people):
	result=[]
	for email, name in people:
		result.append("{} <{}>".format(name, email))
	return	result

print(full_email([("hanxinyu@gmail.com","Hans"),("candice@gmail.com","Candice")]))



animals=["cat","dophine","lion","tiger"]
animals.sort()
animals.reverse() 
length=[len(animal) for animal in animals]
print(length)

"""
list[i] = x Replaces the element at index i with x
list.append(x) Inserts x at the end of the list
list.insert(i, x) Inserts x at index i
list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x) Removes the first occurrence of x in the list
list.sort() Sorts the items in the list
list.reverse() Reverses the order of items of the list
list.clear() Removes all the items of the list
list.copy() Creates a copy of the list
list.extend(other_list) Appends all the elements of other_list at the end of list
"""


spring = [3,4,5]
summer = [i+3 for i in spring]
autumn = [9,10]
autumn.append(11)
winter = [12,1,2,3]
winter.remove(3)
month = int(input('请输入月份：'))
if month in spring:
    print('{}月是春天'.format(month))
elif month in summer:
    print('{}月是夏天'.format(month))
elif month in autumn:
    print('{}月是秋天'.format(month))
elif month in winter:
    print('{}月是冬天'.format(month))
else:
    print('请输入正确的月份')