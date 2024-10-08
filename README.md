<h1>Criando uma Rapida API com FastApi.</h1>
<p>O objetivo desse projeto e mostrar como e simples criar uma API com FastApi.</p>

<p>Primeiro vamos criar nosso ambiente virtual. </p>

```
python3 -m venv venv
```

<h2>Ativando o Ambiente Virtual</h2>
<p>Uma vez criada a venv ira aparecer uma pasta chamada venv em sua pasta do projeto, depois disso iremos ativar nosso ambiente virtual.</p>

```
windows -> venv\Scripts\activate.bat
linux -> source venv/bin/activate
mac -> venv/bin/activate
```

<h2>Instalando o FastAPI</h2>
<p>Uma vez ativada a venv, iremos instalar o FastApi utilizando pip o gerenciador de pacotes do python.</p>

```
pip install fastapi
```
<h2>Criando API.</h2>
<p>Uma vez instalado o FastApi criaremos um arquivo chamado app.py e dentro dele importaremos o FastApi.</p>

```
from fastapi import FastAPI
```

<p>Uma vez importado a classe instaciaremos a classe para usar seus metodos. </p>

```
app = FastAPI()
```
<h2>Criando um Hello World</h2>
<p>Depois de instanciar chegou a hora de testar o FastApi, utilizaremos o decorator @ em conjunto com nossa instancia app e o metodo get onde apontaremos para home do nosso site, onde retornaremos um hello world mostrado no codigo abaixo.</p>

```
@app.get('/')
def init():
    return {"data":"Hello World"}
```

<h2>Instalando o Uvicorn</h2>
<p>Depois de ter criado nosso codigo hello world agora testaremos nossa aplicacao, mas antes certificaremos que o uvicorn esta instalado para iniciar a nossa aplicacao para instalar o uvicorn utilize o codigo mostrado abaixo.</p>

```
pip install uvicorn
```
<h2>Testando o FastApi</h2>
<p>Depois de ter instalado o uvicorn iniciaremos nosso FastApi com seguinte comando.</p>

```
uvicorn app:app --reload
```
<p>app:app -> esta pegando o arquivo e a variavel app dentro do arquivo.

--reload->Recarrega a pagina a cada mudanca no arquivo.
</p>

<p>Uma vez iniciada voce vera um link para sua aplicacao local na porta 8000 entao voce vera algo mais ou menos assim.</p>

![imagem do terminal](https://i.imgur.com/2atgfXQ.png)

<p>Ao copiar o link e colar em seu navegador voce provalvelmente ira ver uma imagem como essa.</p>

![imagem da nossa pagina loca](https://i.imgur.com/WHLP2nX.png)

<p>Esse json que vc ve em sua pagina local nada mais e do que aquele retorno que definimos acima.</p>

<h2>Criando uma lista.</h2>
<p>Feito Teste e tudo funcionado normalmente. Agora Criaremos uma lista para armazenar nossos usuarios criados.</p>

```
user_list = []
```

<h2>Criando Modelos.</h2>
<p>Agora Criaremos um outro arquivo para armazenar nossos modelos de classe para usar como modelo de requisicao, nesse caso criaremos um para passar um modelo na requisicao.</p>

```
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    drive_license:bool
```

<p>Obeserve que utlizamos o BaseModel para facilitar na criacao de nossa class em vez de usar o padrao de classe do python, simplesmente importamos o Basemodel e criamos nossas propriedades.</p>

<h2>Criando Caminho para Adicionar Usuario.</h2>

<p>Uma vez Criado o modelo para o usuario vamos criar o caminho utilizando o metodo POST para adicionar o usuario e passaremos como requisicao em user a classe User, feito isso vamos adicionar esse usuario a nossa lista user_list e por fim retornaremos um dicionario ou objeto com "status" e a "data" com nossa user_list.</p>

```
@app.post('/add/user/')
def add_user(user:User):
    
    user_list.append(user)

    return {
        "Status":"ok",
        "data":user_list
        }
```
<h2>Testando nossa aplicacao</h2>
<p>Feito todos os passos acima vamos testar nossa aplicacao iniciaremos nossa aplicacao fastapi utilizando uvicorn como descrito acima e na url do seu navegador coloque a seguinte url abaixo para testar nossa aplicacao.</p>

```
http://127.0.0.1:8000/docs
```
<p>Voce vera os urls que voce criou no seu app.py</p>

![imagem fastapi docs](https://i.imgur.com/9N3ukA4.png)

<p>Clicando no caminho do Add User abrira a opcao de vc passar as informacoes clicando em <b>try it out</b> e observe que o modelo que e passado e o mesmo que definimos, uma vez preenchido os parametros clique em execute e voce obtera a seguinte resposta se tudo estiver correto.</p>

![imagem fastapi resposta](https://i.imgur.com/XO7jRJl.png)

<p>Uma resposta com status 200 e com o retorno que vc definiu.</p>


<h2>Buscando um Usuario</h2>
<p>Feito os passos acima agora vamos implementar usando o metodo get que nos vai retornar atraves de uma busca pelo nome e nos retornara o seus dados, segue o codigo abaixo</p>

```
@app.get('/user/{nome}')
def get_user(nome:str):

    for usuario in user_list:
        if(usuario.name == nome):
            return {"data":usuario}

    return {"data":user_list}  
```
<p>O codigo vai percorrer a lista user_list e comparar com o nome da minha requisicao no caminho "nome" e quando encontrar retornara o dados do usuario. Entre no doc do fastapi e http://127.0.0.1:8000/docs e adicione usuario utilizando o metodo acima e depois entre no caminho /user/{nome}.</p>

![imagem doc fastapi](https://i.imgur.com/B161t8q.png)

<p>Ao clicar no link aparecera um espaco em branco para digitar o nome que deseja procurar digite um nome que voce adicionou utilizando o exemplo acima e clique em executar.</p>

<p>Como voce passou o caminho o {nome} tambem funcionara se voce na sua barra de pesquisa digitar http://127.0.0.1:8000/user/{nome} claro no lugar do {nome} voce ira digitar o nome que voce procura tipo http://127.0.0.1:8000/user/Carlos</p>

![imagem doc fastapi](https://i.imgur.com/HLjAQwZ.png)

<p>E voce obtera o retorno com status 200 e com os dados do nome que vc procurou.</p>

![imagem doc fastapi](https://i.imgur.com/Ig68rlV.png)

<h2>Conclusao</h2>
<p>Pronto voce acabou de fazer uma api utilizando o FastApi Adicionando usuarios e retornando usuarios pelo nome procurado, com FastApi ficou bem simples ne?.</p>
