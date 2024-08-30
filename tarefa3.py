from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Acessar o banco de dados e a coleção
db = client["distribuidora"]
collection = db["faturamento"]

# Consultar os dias com faturamento maior que zero
faturamentos = list(collection.find({"valor": {"$gt": 0}}))

# Extrair apenas os valores de faturamento
valores = [dia['valor'] for dia in faturamentos]

# Calcular o menor e o maior faturamento
menor_faturamento = min(valores)
maior_faturamento = max(valores)

# Calcular a média mensal
media_mensal = sum(valores) / len(valores)

# Contar os dias com faturamento acima da média mensal
dias_acima_media = len([valor for valor in valores if valor > media_mensal])

# Exibir os resultados formatados em reais
print(f"Menor valor de faturamento: R$ {menor_faturamento:,.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:,.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
