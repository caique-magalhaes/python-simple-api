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
<h2>Criando API</h2>
<p>Uma vez instalado o FastApi criaremos um arquivo chamado app.py e dentro dele importaremos o FastApi </p>

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
<p>Depois de ter instalado o uvicorn iniciaremos nosso FastApi com seguinte comando </p>

```
uvicorn app:app --reload
```
<p>app:app -> esta pegando o arquivo e a variavel app dentro do arquivo.

--reload->Recarrega a pagina a cada mudanca no arquivo.
</p>

<p>Uma vez iniciada voce vera um link para sua aplicacao local na porta 8000 entao voce vera algo mais ou menos assim</p>

![imagem do terminal](https://i.imgur.com/2atgfXQ.png)

<p>Ao copiar o link e colar em seu navegador voce provalvelmente ira ver uma imagem como essa</p>

![imagem da nossa pagina loca](https://i.imgur.com/WHLP2nX.png)

<p>Esse json que vc ve em sua pagina local nada mais e do que aquele retorno que definimos acima.</p>