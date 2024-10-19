import matplotlib.pyplot as plt
import numpy as np

# Gerar dados aleatórios
np.random.seed(42)  # Para reprodutibilidade
x = np.random.rand(100) * 100  # Coordenadas x
y = np.random.rand(100) * 100  # Coordenadas y
sizes = np.random.rand(100) * 200  # Tamanhos dos pontos
colors = np.random.rand(100)  # Cores dos pontos

# Criar o gráfico de dispersão
plt.figure(figsize=(12, 8))
scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis', edgecolors='w')

# Adicionar título e rótulos
plt.title('Visualização Artística de Dados - Gráfico de Dispersão', fontsize=16, fontweight='bold')
plt.xlabel('Eixo X', fontsize=14)
plt.ylabel('Eixo Y', fontsize=14)

# Adicionar uma barra de cores
plt.colorbar(scatter, label='Cores')

# Exibir o gráfico
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

