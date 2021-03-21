import csv
import matplotlib.pyplot as plt
import networkx as nx

graph = nx.DiGraph(directed=True)

#### READING DATASET
with open('809864.edges') as file:
    reader  = csv.reader(file,delimiter=' ')
    count = 0
    for row in reader:
        if(count!=0):
            graph.add_edge(row[0],row[1])
        count+=1

nx.draw(graph,with_labels=True)
plt.draw()
plt.show()


#### CALCULATING CENTRALITIES
degreeCentralities = nx.degree_centrality(graph)
sum=0
for row in degreeCentralities:
    sum+=degreeCentralities[row]
    
print('Average Degree Centrality: ' + str(sum/count))

clossnessCentralities = nx.closeness_centrality(graph,None,None,True)
sum=0
for row in clossnessCentralities:
    sum+=clossnessCentralities[row]
    
print('Average Clossness Centrality: ' + str(sum/count))

betweennessCentralities = nx.betweenness_centrality(graph,None,True,None,False,None)
sum=0
for row in betweennessCentralities:
    sum+=betweennessCentralities[row]
    
print('Average Betweenness Centrality: ' + str(sum/count))

eigenCentralities = nx.eigenvector_centrality(graph,100,1e-06,None,None)
sum=0
for row in eigenCentralities:
    sum+=eigenCentralities[row]
    
print('Average Eigen Centrality: ' + str(sum/count))

katzCentralities = nx.katz_centrality_numpy(graph)
sum=0
for row in katzCentralities:
    sum+= katzCentralities[row]
    
print('Average Katz Centrality: ' + str(sum/count))

Cluster = nx.clustering(graph,None,None)
sum=0
for row in Cluster:
    sum+=Cluster[row]
    
print('Average Clustering: ' + str(sum/count))

Transitivity = nx.transitivity(graph)
print('Average Transitiviy: ' + str(Transitivity))

Reciprocity = nx.overall_reciprocity(graph)
print('Reciprocity of the Directed graph: ' + str(Reciprocity))


#### PLOT for N_G and N RATIO
n = graph.number_of_nodes()
x = []
y = []
k = 0
while(k <= 5):
    x.append(k)
    p = k / n
    g_random = nx.gnp_random_graph(n, p)
    random_n = g_random.number_of_nodes()
    random_n_g = 0
    for component in nx.connected_components(g_random):
        random_n_g = max(random_n_g, len(component))
    y.append(random_n_g / random_n)

    k += 0.1
    
ymax = max(y)
ymin = min(y)
plt.plot(x, y,lw=3)
plt.xlabel("Average Degree")
plt.ylabel("N_G/N ratio")
plt.show()
