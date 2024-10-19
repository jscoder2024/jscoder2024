import matplotlib.pyplot as plt
import networkx as nx

# Definindo os nós e arestas
nodes = ["A", "B", "C", "D", "E"]
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

# Criando o gráfico
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Posicionando os nós
pos = nx.spring_layout(G)  # Algoritmo de força direcionada

# Criando a figura
plt.figure(figsize=(8, 6))

# Desenhando os nós
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black')

# Desenhando as arestas
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')

# Adicionando rótulos aos nós
nx.draw_networkx_labels(G, pos, font_size=14, font_color='black')

# Adicionando um título
plt.title("Gráfico de Rede Artístico", fontsize=16)

# Ocultando os eixos para melhor visualização
plt.axis('off')

# Exibindo o gráfico
plt.show()

