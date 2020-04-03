import operator


class BinHeap:
    def __init__(self):
        self.heap_list = [(0, 0)]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_сhild(i)
            if self.heap_list[i][0] > self.heap_list[mc][0]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_сhild(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2][0] < self.heap_list[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [(0, 0)] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def size(self):
        return self.current_size


def sort_stack():
    f = open("C:\Lol\Value.txt")
    stack = 0
    fl = False
    while stack < 5000:
        a = []
        stack += 1
        i = 0
        while i < 10 ** 5:
            a.append(int(f.readline()))
            i += 1
        writefile = open("Mystack" + str(stack) + ".txt", "w")
        a.sort()
        for item in a:
            writefile.write("%s\n" % item)
        writefile.close()


def heapify(a, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i


def update(stack):
    f = open("Mystack" + str(stack) + ".txt", "r")
    return int(f.readline())


def merge_stack():
    a = []
    b = BinHeap()

    ans = open("result.txt", "w")

    for i in range(10000):
        f = open("Mystack" + str(i + 1) + ".txt", "r")
        a.append(int(f.readline()))
    b.buildHeap(a)
    for i in range(100000):

        q = b.del_min()

        ans.write("%s\n" % q)
        index = a.index(q)

        rr = update(index + 1)
        b.insert(rr)


def merge():
    out_fp = open("result.txt", "w")
    fp = []
    b = BinHeap()

    for i in range(5000):
        fp.append(open("Mystack" + str(i + 1) + ".txt", "r"))
        b.insert((int(fp[i].readline()), i + 1))
        if i % 100 == 0:
            print(i)
    while b.size() > 0:
        elem = b.del_min()

        k = int(elem[1])
        k -= 1

        line = int(fp[k].readline())

        if line:
            b.insert((line, k + 1))
        out_fp.write(str(elem[0]) + "\n")

merge()

