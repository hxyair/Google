toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] =24 # Chapter 3 now starts on page 24
del toc["Chapter 1"]
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?
for extention in toc:
	print(extention)
for name,page in toc.items():
	print("Page is {} of {}".format(page,name))
print(toc.keys())
print(toc.values())




wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
    for i in value:
        print("{} {}".format(i, key))
        
'''
dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
dict.keys() - Returns a sequence containing the keys in the dictionary
dict.values() - Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
dict.clear() - Removes all the items of the dictionary
len(dictionary) - Returns the number of items in the dictionary
for key in dictionary - Iterates over each key in the dictionary
for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
if key in dictionary - Checks whether the key is in the dictionary
dictionary[key] - Accesses the item with key key of the dictionary
dictionary[key] = value - Sets the value associated with key
del dictionary[key] - Removes the item with key key from the dictionary
'''
# score_dict 这是小象学院成绩单字典
score_dict = {"张三": 90, "李四": 85, "王五": 92, "李雷": 100, "韩梅梅": 100}
print('李雷的成绩是：{}'.format(score_dict['李雷']))
print('张三的成绩是：{}'.format(score_dict['张三']))
##########################
# 对键循环遍历
# 使用score_dict.keys()，for循环遍历字典中的所有键
for key in score_dict.keys():
    print("键是：{}" .format(key))
##########################
# 对值循环遍历
# 使用score_dict.values()，for循环遍历字典中的所有值
for value in score_dict.values():
    print("值是：{}" .format(value))
##########################
# 对键值对循环遍历
# 使用score_dict.items()，for循环遍历字典中的所有键值对
# key 和 value 分别记录每个键值对中的键和值
for key, value in score_dict.items():
    print("键是：{}, 值是：{}" .format(key, value))


pizza1 = {'crust':'thick','toppings':['potato','mushroom','extra cheese']}
#请补充代码，在配料表加入'onion'并打印配料表
pizza1['toppings'].append('onion')
print(pizza1['toppings'])
pizza2 = {'crust':'thin','toppings':['potato','onion']}
pizza3 = {'crust':'thick'}
#请补充代码，合并pizza1和pizza2的配料，作为pizza3的配料
topping = pizza1['toppings']+pizza2['toppings']
pizza3['toppings']=topping
print(pizza3)
print('pizza3的配料是：{}'.format(pizza3['toppings']))


class_list = ["一班", "二班", "三班", "四班", "五班"]
class_student = {}  # 创建一个空字典
# 填充字典
#下面用变量c来对class_lsit进行遍历，设置每个键值对的值为空列表
for c in class_list: # c分别为"一班", "二班", "三班", "四班", "五班"
    class_student[c] = [] # 为字典添加键值对，字典中原来没有c这个键，就创建新键值对，值设置为空列表[]。键值对的值可以为任何类型，包括列表。
print("最初的班级字典是：{}" .format(class_student))
while True:
    your_name = input("请输入你的姓名：（输入q退出）")
    if your_name =='q':
        break
    your_class = input("请输入你的班级：")
    # 现在可以将输入的your_name添加在列表中，使用append()
    class_student[your_class].append(your_name)
    #打印现在的班级列表
    print("现在的班级列表是：{}".format(class_student))
#打印三班学生名单
print('三班学生有：{}'.format(class_student['三班']))
#一班的第二名学生
print('一班的第二个同学是：'+class_student['一班'][1])