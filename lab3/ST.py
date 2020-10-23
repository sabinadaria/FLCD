class SortedList:
    def __init__(self):
        self._list = []
        self._count =0

    def add(self,value):
        id = self.getId(value)
        if id != -1:
            return id
        self._list.append((value, self._count))
        self._count +=1
        self._list = sorted(self._list,key=lambda x:x[0])
        return self._count -1

    def getId(self,value):
        for i in self._list:
            if i[0] == value:
                return i[1]
        return -1

    def __str__(self):
        return str(self._list)
