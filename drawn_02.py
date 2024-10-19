#! bin/python3
"""
Este script analisa a frequência de letras em uma string fornecida.

Ele transforma a string em minúsculas, remove caracteres não alfabéticos e
conta a frequência de cada letra, gerando um gráfico de barras para visualização.

Dependências:
- collections
- matplotlib
- numpy
- string
"""

import collections
import matplotlib.pyplot as plt
import numpy as np
import string

data = "To be, or not to be, that is the question."
data = data.lower()
data = ''.join(filter(lambda x: x in string.ascii_lowercase, data))

counter = collections.Counter(data)

letters, counts = zip(*counter.items())

indices = np.arange(len(letters))

plt.bar(indices, counts, color='skyblue')
plt.xticks(indices, letters)
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.title('Frequency of Letters in the Given String')
plt.show()

