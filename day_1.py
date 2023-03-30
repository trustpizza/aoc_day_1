
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
    # First, we need to clean the list
    # For the list, first split at eat lines
    #print(list.split("\n"))
    seperate_lists_for_each_elf = find_elven_lists_sums(list)
    # print(seperate_lists_for_each_elf)
    return seperate_lists_for_each_elf

def clean_and_find_cals(dirty_list):
    return elf_with_most_calories(clean_list(dirty_list))

def clean_list(dirty_list):
    return dirty_list.split('\n')

def elf_with_most_calories(list):
    print(list)
    return max(find_elven_calories(list))

def top_3_elves(list, times):
    out = []
    list_of_cals = find_elven_calories(list.split('\n'))

    for i in range(times):
        highest = max(list_of_cals)
        out.append(highest)
        list_of_cals.remove(highest)

    return sum(out)

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
""", 3))


"""
print(clean_and_find_cals("""
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