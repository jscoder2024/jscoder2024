import matplotlib.pyplot as plt

# Dados das empresas e suas participações de mercado
labels = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D']
sizes = [30, 25, 20, 25]  # Participações de mercado
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Cores para cada setor
explode = (0.1, 0, 0, 0)  # Destaque a primeira fatia

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Adicionar título
plt.title('Distribuição de Participação de Mercado', fontsize=16, fontweight='bold')

# Manter a proporção do gráfico
plt.axis('equal')  

# Exibir o gráfico
plt.show()

