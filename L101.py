#the authors are Gwyneth and Victoria



def my_get_method(d, key):
    if key in d:
        return d[key]
    else:
        return None

dict_1 ={'Name':'Alice', 'State':'Minnesota', 'Age': 45}
dict_2 = {"flour":1, "jam":3, "butter":4}
print(my_get_method(dict_1,'Name'))
print(my_get_method(dict_1,'State'))
print(my_get_method(dict_2,"butter"))
