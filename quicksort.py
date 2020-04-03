def quick_sort(series):
    lengs = len(series)
    if lengs <=1:
        return series
    else:
        pivot = series.pop()
    greater = []
    lower = []
    for item in series:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quick_sort(lower) + [pivot] + quick_sort(greater)
def quick_sort_main():
    my_text = ""
    with open("C:\Lol\inum.txt") as f:
        for line in f:
            text = line
            my_text += " " + text
    my_list = text.split()
    my_list = [int(i) for i in my_list]
    print(my_list)
    n = len(my_list)
    print(quick_sort(my_list))


