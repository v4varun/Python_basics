my_dict = {'apple': 5, 'orange': 8, 'banana': 2, 'grape': 3}

dict_sort=dict(sorted(my_dict.items(), key = lambda x:x[1], reverse=True ))
#dict_sort = sorted(my_dict)
#dict_sort = my_dict.values()

print(dict_sort)