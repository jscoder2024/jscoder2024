import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gerando dados de idade aleatórios entre 0 e 100
np.random.seed(42)  # Para reprodutibilidade
idades = np.random.randint(0, 101, size=100)

# Configurando o estilo do Seaborn
sns.set(style="whitegrid")

# Criando o histograma
plt.figure(figsize=(10, 6))
sns.histplot(idades, bins=15, kde=True, color='skyblue', edgecolor='black')

# Adicionando títulos e rótulos
plt.title('Histograma de Idades', fontsize=24, fontweight='bold')
plt.xlabel('Idades', fontsize=16)
plt.ylabel('Frequência', fontsize=16)

# Personalizando a grade
plt.grid(axis='y', alpha=0.75)

# Exibindo o histograma
plt.show()

