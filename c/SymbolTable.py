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

symbolTable = SymbolTable()
symbolTable.insert(SymbolTableEntry('main', 'func', 'func', None))
symbolTable.insert(SymbolTableEntry('adsa', 'ergerg', 'ergrg', None))
symbolTable.insert(SymbolTableEntry('maiergegn', 'erg', 'erggrerg', None))

print(symbolTable)