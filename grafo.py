class Adj:
    def __init__(self,v,peso):
        self.vertice=v
        self.peso=peso
        self.prox=None

class Vertice:
    def __init__(self):
        self.cabeca = None
        self.nvizinhos=0
        self.dado=None

class initD:
    def __init__(self,v):
        self.d=[]
        self.p=[]
        for i in range(100):
            self.p.append(-1)
            self.d.append(50000)
        self.d[v]=0
class Grafo:

    def __init__(self,nvert):
        self.nvert=nvert
        self.arestas=0
        self.verticies=[]

def criarvertice(grafo):
    for i in range(100):
        grafo.verticies.append(Vertice())

def criararesta(vi,vf,grafo,peso):
    novo=Adj(vf,peso)
    grafo.verticies[vi].nvizinhos+=1
    novo.prox=grafo.verticies[vi].cabeca
    grafo.verticies[vi].cabeca=novo
    grafo.arestas+=1
def printargf(grafo):

    for i in range (5):
        print("vertice=",i)
        j=i
        fk=grafo.verticies
        for i in range(fk[j].nvizinhos):
            print(fk[j].cabeca.vertice)
            fk[j].cabeca=fk[j].cabeca.prox
def relaxa(grafo,listas,u,v):
    ad=grafo.verticies[u].cabeca
    while (ad and ad.vertice!=v):
        ad=ad.prox
    if(ad):
        if(listas.d[v] > listas.d[u]+ ad.peso):
            listas.d[v] = listas.d[u]+ad.peso
            listas.p[v] = u

def dijsktra(grafo,vertice):
    aberto=[]
    listas=initD(vertice)
    for i in range(grafo.nvert):
        aberto.append(1)
    while(isopen(grafo,aberto)):
        u=smallerdist(grafo,aberto,listas)
        aberto[u]=0
        ad=grafo.verticies[u].cabeca
        while(ad):
            relaxa(grafo,listas,u,ad.vertice)
            ad=ad.prox
    for i in range(grafo.nvert):
        print(listas.d[i])
def isopen(grafo,aberto):
    for i in range(grafo.nvert):
        if(aberto[i]==1):
            return 1
    return 0

def smallerdist(grafo,aberto,listas):
    for i in range(grafo.nvert):
        if(aberto[i]):
            break
        if(i==grafo.nvert):
            return -1
        menor =1
        j=menor +1
        for j in range(grafo.nvert):
            if(aberto[j] and listas.d[menor]>listas.d[i]):
                menor=i
        print(menor)
        return menor


grafo=Grafo(6)
criarvertice(grafo)
criararesta(0,1,grafo,10)
criararesta(0,2,grafo,5)
criararesta(2,1,grafo,3)
criararesta(1,3,grafo,1)
criararesta(2,3,grafo,8)
criararesta(2,4,grafo,2)
criararesta(4,5,grafo,6)
criararesta(3,5,grafo,4)
criararesta(3,4,grafo,4)
dijsktra(grafo,0)
