# 12. zadanie: labyrint
# autor: Adam Lopaška
# datum: 29.5.2022

class Labyrinth:
    class Vertex:
        def __init__(self, row, column):  # riadok, stĺpec
            self.adjacent = []            # zoznam susedov, susedia sú typu Vertex
            self.row, self.column = row, column
            self.reward = False           # odmena

        def __repr__(self):
            return f'<{self.row},{self.column}>'

    def __init__(self, file_name):
        self.graph = {}                   # slovník vrcholov grafu – obsahuje objekty typu Vertex
        self.odmeny = set()               # mnozina vrcholov s odmenami
        self.steny = set()                # mnozina dvojic vrcholov so stenami(bez priechodu)
        with open(file_name, 'r') as file:
            riadky , stlpce = file.readline().split() #prvy riadok pocet riadkov a stlpcov
            for riadok in file:
                riadok = riadok.split()
                if len(riadok) == 2:
                    self.odmeny.add((int(riadok[0]),int(riadok[1])))  #pridaj odmenu
                elif len(riadok) > 2:
                    for i in range(2, len(riadok), 2):
                        riadok = list(map(lambda x: int(x),riadok))
                        self.steny.add(((riadok[i-2],riadok[i-1]),(riadok[i],riadok[i+1])))
        riadky, stlpce = int(riadky), int(stlpce)
        for i in range(riadky):
            for j in range(stlpce):
                self.graph[(i,j)] = self.Vertex(i,j) 
        for i in range(riadky):
            for j in range(stlpce):
                susedia = []
                
                if (i,j) in self.odmeny:
                    self.graph[(i,j)].reward = True
                if i > 0:
                    susedia.append((i-1,j))
                if i < riadky-1:
                    susedia.append((i+1,j))
                if j > 0:
                    susedia.append((i,j-1))
                if j < stlpce-1:
                    susedia.append((i,j+1))
                for sus in susedia:
                    if not ((i,j),(sus[0],sus[1])) in self.steny and not ((sus[0],sus[1]),(i,j)) in self.steny:
                        self.graph[(i,j)].adjacent.append(self.graph[(sus[0],sus[1])])

        
    def zisti_odmeny(self):
        self.odmeny = set()
        for v in self.graph:
            if self.graph[v].reward == True:
                self.odmeny.add((self.graph[v].row,self.graph[v].column))
        return self.odmeny

    def get_vertex(self, row, column):
        return self.graph[(row,column)]

    def change_rewards(self, *seq):
        for i in seq:
            if self.graph[i].reward == True:
                self.graph[i].reward = False
            else:
                self.graph[i].reward = True
        self.zisti_odmeny()

    def start(self, row, column):
        self.pocet = len(self.zisti_odmeny())
        self.riesenie = []
        self.cesta = [(row,column)]
        self.najcesta = None
        self.visited = set()
        if (row,column) in self.odmeny:
            self.backtracking([(row,column)],1)
        else:
            self.backtracking([(row,column)],0)
        if self.najcesta is None:
            return []
        return self.najcesta 
    
    def backtracking(self,cesta,hodnota):
        if hodnota == self.pocet:
            if self.najcesta is None:
                self.najcesta = cesta
            elif len(self.najcesta) > len(cesta):
                self.najcesta = cesta
        else:
            for v in self.graph[(cesta[-1][0],cesta[-1][1])].adjacent:
                if (v.row,v.column) not in cesta:
                    if (v.row,v.column) in self.odmeny:
                        self.backtracking(cesta + [(v.row,v.column)], hodnota +1)
                    else:
                        self.backtracking(cesta + [(v.row,v.column)], hodnota)

if __name__ == '__main__':
    lab = Labyrinth('subor3.txt')
    lab.start(5, 5)
    lab.change_rewards((6, 5), (7, 5), (8, 5), (9, 5), (10, 5))
    lab.start(5, 5)
    lab.change_rewards((4, 5))
    print(lab.start(5, 5))