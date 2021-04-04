class SymbolTableEntry:
    def __init__(self, name=None, kind=None, type=None, link=None):
        self.name = name
        self.kind = kind
        self.type = type
        self.link = link
    def __repr__(self):
        return f'{self.name} {self.kind} {self.type} {self.link}'


class SymbolTable:
     def __init__(self):
         self.table = []

     def createNewTable(self):
         return []

     def insert(self, symbolTableEntry):
         self.table.append(symbolTableEntry)

     def search(self, name):
         for symbolTableEntry in self.table:
             if(name == symbolTableEntry.name):
                 return symbolTableEntry

     def delete(self, name):
         listOfEntriesToDelete = []
         for symbolTableEntry in self.table:
             if(name == symbolTableEntry.name):
                 listOfEntriesToDelete.append(symbolTableEntry)

         if len(listOfEntriesToDelete) != 0:
             self.table.pop(listOfEntriesToDelete[0])

     def __repr__(self):
         repr = "'name ', 'kind ', 'type ', 'link' \n"
         for symbolTableEntry in self.table:
             repr = repr + str(symbolTableEntry) + '\n'

         return repr

_global = SymbolTable()
bubbleSort = SymbolTable()
printArray = SymbolTable()
main = SymbolTable()

_global.insert(SymbolTableEntry('function', 'bubbleSort', '(integer[],integer):void', bubbleSort))
_global.insert(SymbolTableEntry('function', 'printArray', '(integrer[],integer):void', printArray))
_global.insert(SymbolTableEntry('function', 'main', '():', main))


bubbleSort.insert(SymbolTableEntry('local', 'n', 'integer', None))
bubbleSort.insert(SymbolTableEntry('local', 'i', 'integer', None))
bubbleSort.insert(SymbolTableEntry('local', 'j', 'integer', None))
bubbleSort.insert(SymbolTableEntry('local', 'temp', 'integer', None))

printArray.insert(SymbolTableEntry('local', 'n', 'integer', None))
printArray.insert(SymbolTableEntry('local', 'i', 'integer', None))

main.insert(SymbolTableEntry('local', 'arr', 'integer[7]', None))

print(_global)