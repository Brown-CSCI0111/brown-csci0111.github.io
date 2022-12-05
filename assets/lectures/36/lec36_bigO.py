# CS111 code file for bigO lecture

def distinct1(my_list: list):
    output = []
    for item in my_list:
        if not(item in output): output.append(item)
    return output

def distinct2(my_list: list):
    "return list of unique items in the list"
    if len(my_list) == 0: return []
    else:
        first = my_list[0]
        rest = my_list[1:]
        if first in rest:
            return distinct2(rest)
        else:
            return [first] + distinct2(rest)

def distinct3(my_list: list):
    item_dict = {}
    for item in my_list:
        item_dict[item] = True
    return list(item_dict.keys())

test_list = [1, 2, 1, 2, 2, 2, 4, 5, 2, 1]

print(distinct1(test_list))
print(distinct2(test_list))
print(distinct3(test_list))