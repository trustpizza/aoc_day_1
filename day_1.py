
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
    seperate_lists_for_each_elf = find_elven_lists_sums(list.split('\n'))
    return max(seperate_lists_for_each_elf)

print(find_elven_calories("""1000
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
