import math

# print("hello world")
# print("he said\"let's go.\"")

# a = 6
# b = 9
# c = 20
# print ((-b + (b**2 - 4*a*c)**1/2)/(2*a))
# print ((-b - (b**2 - 4*a*c)**1/2)/(2*a))

# s = "hello world!"
# print(len(s))  #12
# print(s[0])
# print(s[10])
# print(s[len(s)-1])

# user_weight = float(input("您的体重是(kg)： "))
# user_height = float(input("您的身高是(m):  "))
# bmi = user_weight / (user_height ** 2)

# print("您的bmi是：" + str(bmi))

# mood_index = int(input("对象的心情指数是:  ")) #切记input的返回类型
#
# if mood_index >= 60 :
#     print("可以打游戏了！")
# else :
#     print("为了自己的小命，还是别打了。")

# user_weight = float(input("您的体重是(kg)： "))
# user_height = float(input("您的身高是(m):  "))
# bmi = user_weight / (user_height ** 2)
#
# print("您的体重是："+ str(bmi))
#
# if bmi < 18.5:
#     print("偏瘦")
# elif 18.5 < bmi <= 25:
#     print("正常")
# elif 25 < bmi <= 30:
#     print("偏胖")

# shopping_list = []
# shopping_list.append("原道洛基")
# shopping_list.append("拓品dx52")
# shopping_list.append("HD490PRO")
#
# print(shopping_list)
# print(len(shopping_list))
# print(shopping_list[0])
#
# price = [2899,1639,2654]
# max_price = max(price)
# min_price = min(price)
# sorted_price = sorted(price)
# print(max_price)
# print(min_price)
# print(sorted_price)

# dict = {"ci1":"jpui1",
#         "ci2":"jpui2",
#         "ci3":"jpui3"}
# dict["xbtm1"] = "jpuiqmmfhkohc1"
# dict["xbtm2"] = "jpuiqmmfhkohc2"
# dict["xbtm3"] = "jpuiqmmfhkohc3"
# dict["xbtm4"] = "jpuiqmmfhkohc4"
# dict["xbtm5"] = "jpuiqmmfhkohc5"
# dict["xbtm6"] = "jpuiqmmfhkohc6"
#
# query = input("请输入您要查询的值:")
# if query in dict:
#     print("您查询的" + query + "含义如下")
#     print(dict[query])
# else:
#     print("您查询的此条暂时未收录")
#     print("本词典共收录" + str(len(dict)) + "个词条")

# dict = {"staff1":36,
#         "staff2":37,
#         "staff3":38}
# for staff_id, temperature in dict.items():
#     if temperature > 37:
#         print(staff_id)

# total = 0
# for i in range(1,100):
#     total = total + i
# print(total)

# print("一个计算器程序")
# user_input = 0
# user_input = (input("请输入数字(输入q停止）"))
# time = 0
# num = 0
# average = 0
# while user_input != "q":
#     time += 1
#     num += float(user_input)
#     user_input = (input("请输入数字(输入q停止）"))
# if num == 0:
#     average = 0
# else:
#     average = num / time
# print("平均数为" + str(average))

def calculate_sector(central_angle,radius,):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形面积为{sector_area}")

























