## Como configurar e utilizar ambientes virtuais com `venv` em Python

### **Por que utilizar ambientes virtuais?**
Ambientes virtuais permitem isolar as dependências de um projeto para garantir que todos trabalhem com as mesmas versões de bibliotecas e módulos, evitando problemas de compatibilidade. Isso é útil quando, por exemplo, um projeto utiliza Python 3.9 e Flask, enquanto outro usa Python 3.11 e Django.

### **Criando um ambiente virtual com `venv`**
1. No terminal, dentro do diretório do projeto, crie um ambiente virtual com o comando:
   ```bash
   python -m venv venv
   ```
   Isso cria uma pasta `venv` no diretório do projeto.

2. Ative o ambiente virtual:
   - **Windows:**
     ```bash
     ./venv/Scripts/activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

   Após ativado, o prefixo `(venv)` aparecerá no terminal, indicando que o ambiente está ativo.

### **Instalando dependências**
- Instale bibliotecas necessárias usando `pip`. Por exemplo, para instalar a biblioteca `requests`:
   ```bash
   pip install requests
   ```
- Liste as dependências instaladas com:
   ```bash
   pip freeze
   ```

### **Salvando dependências no `requirements.txt`**
Para facilitar a instalação das mesmas dependências em outro ambiente, exporte-as para um arquivo `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

### **Desativando o ambiente virtual**
Quando terminar de usar o ambiente virtual, desative-o com:
   ```bash
   deactivate
   ```

Agora você sabe como configurar, ativar, gerenciar dependências e desativar ambientes virtuais em Python.

### Diferenças entre `venv` e `virtualenv`

Como mencionamos, tanto `venv` quanto `virtualenv` são utilizados para criar ambientes virtuais no Python, mas eles têm algumas diferenças significativas, especialmente em termos de compatibilidade, escopo de funcionalidades, e situações de uso recomendadas.

#### Compatibilidade
- **`venv`:** Integrado ao Python 3.3 e versões posteriores, tornando-o mais conveniente para desenvolvedores que utilizam essas versões mais recentes do Python. É o padrão recomendado a partir do Python 3.5, pois já está embutido e não requer instalação extra.
- **`virtualenv`:** Ferramenta externa que precisa ser instalada manualmente, mas é compatível com versões mais antigas do Python (até o Python 2), o que a torna uma opção viável para projetos legados ou que precisam de compatibilidade com versões pré-Python 3.3.

#### Escopo de Funcionalidades
- **`venv`:** Suporta funcionalidades básicas de isolamento de ambientes, atendendo bem à maioria dos casos de uso em Python 3.
- **`virtualenv`:** Apresenta funcionalidades mais avançadas, como o suporte a múltiplas versões do Python e integração com diferentes interpretadores, além de poder ser usado em ambientes mais complexos que envolvem múltiplas linguagens.

#### Isolamento de Ambientes Virtuais
- **`venv`:** Fornece isolamento adequado para a maioria dos projetos Python, mas com menos opções de personalização.
- **`virtualenv`:** Oferece uma separação de dependências mais robusta e é mais flexível em situações onde o isolamento de múltiplas versões de bibliotecas e interpretadores é crucial.

### Ativação e Desativação do Ambiente Virtual

Tanto `venv` quanto `virtualenv` utilizam comandos semelhantes para ativar e desativar ambientes virtuais. No Windows, o comando para ativar o ambiente é `<env>\Scripts\activate`, enquanto no Linux/macOS é `source <env>/bin/activate`.

**Exemplo de uso no Windows:**
```bash
<env>\Scripts\activate
```

**Exemplo de uso no Linux/macOS:**
```bash
source <env>/bin/activate
```

### Quando Usar `venv` ou `virtualenv`?

- **Use `venv`:** Se você está trabalhando com Python 3.3 ou superior e não precisa de funcionalidades extras, `venv` é a melhor opção por ser integrado e fácil de usar.
- **Use `virtualenv`:** Se você está utilizando Python 2 ou precisa de mais flexibilidade, como suporte a múltiplas versões de Python e melhores opções de personalização, `virtualenv` será mais apropriado.

---

### Protocolo HTTP e APIs

Agora que temos uma compreensão dos ambientes virtuais, vamos abordar a importância do protocolo HTTP e como ele é utilizado no desenvolvimento de APIs para compartilhar dados entre um servidor e um cliente.

#### O que é uma API?

Uma **API** (Interface de Programação de Aplicações) permite que diferentes sistemas se comuniquem entre si, utilizando um protocolo comum — neste caso, o **HTTP**. Com a API, você pode expor dados ou funcionalidades de uma aplicação para que outros desenvolvedores possam integrá-las em seus próprios sistemas.

#### Comunicação Cliente-Servidor

A comunicação entre cliente e servidor segue uma estrutura de **requisição** e **resposta**:
1. **Cliente**: Faz uma solicitação (requisição) para acessar um recurso ou informação em um servidor.
2. **Servidor**: Processa essa requisição e devolve uma **resposta** contendo os dados solicitados.

### Exemplo de Uso com JSON e a Biblioteca `requests`

Para acessar dados de uma API que retorna um arquivo JSON, utilizamos a biblioteca `requests` do Python. Suponha que estamos acessando dados de restaurantes. Podemos usar a URL de uma API que contém informações de um cardápio em formato JSON e processar esses dados em nossa aplicação.

```python
import requests

# URL com os dados de restaurantes
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# Fazendo a requisição GET para acessar os dados
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)  # Exibindo os dados JSON no console
else:
    print(f'O erro foi {response.status_code}')
```

Neste exemplo:
- Usamos o método `requests.get(url)` para obter os dados.
- Verificamos se o **status code** da requisição é 200 (sucesso).
- Caso a requisição tenha sido bem-sucedida, processamos os dados JSON e os exibimos.

Aqui está um resumo que você pode utilizar para documentar como criar uma API usando **FastAPI** no seu projeto:

---

## Criando uma API com FastAPI

Neste projeto, utilizamos o **FastAPI** para criar uma API que acessa dados de restaurantes e exibe seus cardápios. A seguir está um guia passo a passo para configurar o ambiente e criar endpoints.

### 1. Instalação do FastAPI e Uvicorn
Primeiro, precisamos instalar as bibliotecas necessárias:

```bash
pip install fastapi
pip install uvicorn
```

Para garantir que todas as dependências estão documentadas, execute:

```bash
pip freeze > requirements.txt
```

### 2. Criando o Arquivo `main.py`
Criamos um arquivo chamado `main.py` e iniciamos importando o FastAPI e o Uvicorn:

```python
from fastapi import FastAPI
import requests

app = FastAPI()
```

### 3. Definindo a Primeira Rota
Adicionamos um endpoint simples que responde com "Hello World":

```python
@app.get('/api/hello')
def hello_world():
    return {'Hello': 'World'}
```

### 4. Rota para Consultar Restaurantes
Criamos uma rota para consultar os cardápios dos restaurantes:

```python
from fastapi import Query

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = [
            {
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            }
            for item in dados_json if item['Company'] == restaurante
        ]
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}
```

### 5. Executando o Servidor
Para rodar o servidor localmente, utilizamos o comando:

```bash
uvicorn main:app --reload
```

Isso permite acessar a API localmente em `http://127.0.0.1:8000`.

### 6. Consultando Endpoints
- Para testar o endpoint de saudação: `http://127.0.0.1:8000/api/hello`
- Para obter todos os cardápios: `http://127.0.0.1:8000/api/restaurantes`
- Para filtrar por restaurante específico, como McDonald's: `http://127.0.0.1:8000/api/restaurantes/?restaurante=McDonald's`

