import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo com cabeçalho
df = pd.read_csv('adc_data0.csv')

# Visualize os nomes das colunas (se quiser conferir)
print("Colunas disponíveis:", df.columns.tolist())

# Cria um gráfico com os dados dos giroscópios
plt.figure(figsize=(10, 5))
plt.plot(df['amostra'], df['eixoX'], label='Giro X')
plt.plot(df['amostra'], df['eixoY'], label='Giro Y')
plt.plot(df['amostra'], df['eixoZ'], label='Giro Z')
plt.title('Eixos do Giroscópio')
plt.xlabel('Amostra')
plt.ylabel('Valor do Eixo')
plt.legend()
plt.grid(True)

# Segundo gráfico: Aceleração
plt.figure(figsize=(10, 5))
plt.plot(df['amostra'], df['aceleracaoX'], label='Accel X')
plt.plot(df['amostra'], df['aceleracaoY'], label='Accel Y')
plt.plot(df['amostra'], df['aceleracaoZ'], label='Accel Z')
plt.title('Aceleração')
plt.xlabel('Amostra')
plt.ylabel('g')
plt.legend()
plt.grid(True)

plt.show()
