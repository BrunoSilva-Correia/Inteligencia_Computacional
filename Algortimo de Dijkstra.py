#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sys 
  
class Graph():
    
  
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex \tDistance from Source")
        for node in range(self.V): 
            print (node, "\t", dist[node])

    # Incluir o vertice com menor distancia na arvore
    # de distância mínima
    def minDistance(self, dist, sptSet): 
  
        # Distancia minima para o proximo nó 
        min = sys.maxsize
  
        
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Função que implementa o algoritmo de dijkstra para
    # encontrar o menor caminho a se percorrer num grafo
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 

            # Escolher o vertice com menor distancia
            # que ainda não faça parte dos vertices
            # já processados
            u = self.minDistance(dist, sptSet) 

            # Colocar o vertice de menor distância
            # na arvore
            sptSet[u] = True
  

            # Atualizar a distância do vertice somente se
            # o novo vertice tiver menor tamanho que o
            # anterior, se a nova distância for maior que
            # a anterior, o novo vertice não sera colocado
            # na arvore
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                
                    dist[v] = dist[u] + self.graph[u][v]
  
        self.printSolution(dist)



# In[14]:


# Para fazer o teste do algoritmo, utilizei uma matriz
# 9x9 para calcular as menores distancias.
g = Graph(9) 
g.graph = [
        [0, 6, 8, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ];

g.dijkstra(0);


# In[ ]:




