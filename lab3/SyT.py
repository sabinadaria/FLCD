from ST import SortedList


class SymbolTable:
    def __init__(self):
        self._sortedList = SortedList()

    def add(self,value):
        return self._sortedList.add(value)

    def get(self,value):
        return self._sortedList.getId(value)

    def __str__(self):
        return str(self._sortedList)


