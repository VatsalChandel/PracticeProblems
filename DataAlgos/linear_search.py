def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    else:
        return "Target not found"