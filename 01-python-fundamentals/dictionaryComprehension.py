#syntax
# new_dict ={new_key:new_value for item in list}
#another
# new_dict ={new_key:new_value for (key,value) in dict.items() if test_condition}
import random
# names =["Shreas","Goku","Vegeta","Luffy","Natsu"]
# power_lvl ={n:random.randint(1,100) for n in names}
# print(power_lvl)
#
# power_passed_lvl ={key:val for (key,val) in power_lvl.items() if power_lvl[key]>60}
# print(power_passed_lvl)

#Dictionary Comprehension 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sen_list=sentence.split()
# result = {key:len(key) for key in sen_list }
# print(result)

# Dictionary Comprehension 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {k:weather_c[k]*9/5+32 for (k,v) in weather_c.items()}

print(weather_f)