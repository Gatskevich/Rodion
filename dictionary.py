_punctuation = ",."
def dictionary_main():
    j = 0
    my_dict = dict()
    with open("C:\Lol\inf.txt") as f:
        for line in f:
            _punctuation_trans = line.maketrans(_punctuation, " " * len(_punctuation))
            line.translate(_punctuation_trans)
            for word in line.split():
                if word in my_dict:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
    list_dict = list(my_dict.items())
    list_dict.sort(key=lambda i: i[1])
    list_dict.reverse()
    for i in list_dict[:10]:
        print(i[0])
    pass
    pass


