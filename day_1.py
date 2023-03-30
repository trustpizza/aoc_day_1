
def convert_list_values_to_numbers(list):
    for idx, item in enumerate(list):
        list[idx] = int(item)
    return sum(list)

def find_elven_lists_sums(list):
    out = []
    arr = []
    for idx,item in enumerate(list):
        if len(list[idx]) > 1:
            arr.append(item)
        else:
            #arr = convert_list_values_to_numbers(arr)
            out.append(convert_list_values_to_numbers(arr))
            arr = []
    return out

def find_elven_calories(list):
    seperate_lists_for_each_elf = find_elven_lists_sums(list.split('\n'))
    return seperate_lists_for_each_elf

def elf_with_most_calories(list):
    return max(find_elven_calories(list))

def top_3_elves(list):
    list = find_elven_calories(list)
    highest = elf_with_most_calories(list)
    return list

print(top_3_elves("""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""))
    

"""
print(elf_with_most_calories("""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""))
"""