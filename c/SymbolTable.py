class SymbolTableEntry:
    def __init__(self, name=None, kind=None, type=None, link=None):
        self.name = name
        self.kind = kind
        self.type = type
        self.link = link

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

