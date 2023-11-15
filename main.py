import mysql.connector

# Conecte-se ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="herica",
    password="1234",
    database="testWestB"
)

# Crie um cursor para executar consultas SQL
cursor = conexao.cursor()

# Execute a consulta SQL
cursor.execute("""
    SELECT
        c.nome AS cliente_nome,
        c.sobrenome AS cliente_sobrenome,
        ca.cor AS cor_casa,
        b.nome AS bairro,
        car.modelo AS modelo_carro
    FROM cliente c
    JOIN casa ca ON c.id_cliente = ca.fk_cliente
    JOIN bairro b ON ca.fk_bairro = b.id_bairro
    LEFT JOIN carro car ON c.id_cliente = car.fk_cliente
""")

# Recupere os resultados
resultados = cursor.fetchall()

# Exiba os resultados de forma mais detalhada
for resultado in resultados:
    for coluna, valor in zip(cursor.column_names, resultado):
        print(f"{coluna}: {valor}")
    print("----")

# Feche a conexão e o cursor quando terminar
cursor.close()
conexao.close()