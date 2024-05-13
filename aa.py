from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def buscar_cliente(nome_arquivo, termo_busca):
    try:
        # Carregar o arquivo Excel
        df = pd.read_excel(nome_arquivo)

        # Converter o termo de busca para minúsculas
        termo_busca = termo_busca.lower()

        # Filtrar os clientes cujo nome contenha o termo de busca
        encontrados = df[df['Nome'].str.lower().str.contains(termo_busca)]

        if len(encontrados) > 0:
            print("Informações dos Clientes:")
            for index, cliente in encontrados.iterrows():
                print(cliente)
        else:
            print("Cliente não encontrado.")

    except Exception as e:
        print("Ocorreu um erro:", e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_path = request.files['file_path']
        cliente = request.form['cliente']
        # Aqui você precisa chamar a função buscar_cliente com os parâmetros apropriados
        # Por enquanto, vamos apenas imprimir os dados para verificar se o roteamento está funcionando corretamente
        print("Arquivo:", file_path)
        print("Cliente:", cliente)
        # Simulando a passagem de dados para a página de resultado
        cliente_info = {"Nome": "Exemplo", "Idade": 30, "Email": "exemplo@email.com"}
        return render_template('resultado.html', cliente_info=cliente_info)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
