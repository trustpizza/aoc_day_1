def split_lists_by_enter(list):
    lists_as_dict = {}
    lists = list.splitlines()
    for item in lists:
        list_arr = []
        if len(item) > 1:
            list_arr.append(item)

        print(list_arr)
        

def find_elven_calories(list):
    # First, we need to clean the list
    # For the list, first split at eat lines
    split_lists_by_enter(list)

find_elven_calories("""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""")
