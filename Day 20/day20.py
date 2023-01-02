class Link(object):
    def __init__(self, data):
        self.data = data
        self.next = self
    def __str__(self):
        return f"{self.data}"
class CircularList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def insert(self, data):
        if self.head == None:
            self.head = Link(data)
            self.size = 1
            return
        temp = self.head
        for _ in range(self.size - 1):
            temp = temp.next
        nexttemp = temp.next
        temp.next = Link(data)
        temp.next.next = nexttemp
        self.size += 1
        return
    def find(self, data):
        idx = 0
        temp = self.head
        for _ in range(self.size):
            if temp.data == data:
                return (idx, temp.data)
            temp = temp.next
            idx += 1
        return None
    def delete(self, data):
        if data == 0:
            idx == 0
        else:
            findData = self.find(data)
            if findData != None:
                idx = self.find(data)[0]
            else:
                idx = None
        if idx != None:
            prevtemp = self.head
            for _ in range(self.size - 1 if idx - 1 == -1 else idx - 1):
                prevtemp = prevtemp.next
            nexttemp = prevtemp.next.next
            prevtemp.next = nexttemp
            if idx == 0:
                self.head = nexttemp
            self.size -= 1
            return
        else:
            return
    def delete_after(self, start, n):
        if start == 0:
            start = self.size - 1
        start_idx = self.find(start)[0]
        temp = self.head
        for _ in range(n + start_idx):
            temp = temp.next
        copy = temp
        copy2 = temp.next
        self.delete(temp.data)
        return copy.data, copy2.data
    def insert_after(self, start, n, data):
        if start == self.size:
            start = 0
        temp = self.head
        for _ in range(n + start):
            temp = temp.next
        new = Link(data)
        new.next = temp.next
        temp.next = new
        self.size += 1
    def __str__(self):
        arr = []
        temp = self.head
        for _ in range(self.size):
            arr.append(temp.data)
            temp = temp.next
        return f"Circularly Linked List: {arr}"
    
def part1(fileName):
    circList = CircularList()
    f = list(map(int, open(fileName).readlines()))
    # for idx in range(len(f)):
    #     f[idx] %= len(f) - 1
    
    
    # go with this apporach
    # for data in f:
    #     circList.insert(data)
    # print(circList)
    # circList.insert_after(0,3, 2)
    # print(circList)

def part2(fileName):
    f = open(fileName).read().strip()


if __name__ == "__main__":
    import os

    print(
        part1(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part1(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/test.txt"),
        # part2(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"),
        sep="\n",
    )
