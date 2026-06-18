<h1>Python Simple API: FastAPI & Pydantic Tutorial</h1>
<p>A hands-on, practical repository demonstrating how to rapidly build, model, and deploy a RESTful API using FastAPI and Pydantic data validation.</p>

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** FastAPI
* **Data Validation:** Pydantic (BaseModel validation tracking)
* **ASGI Server:** Uvicorn

## 🌟 Key Architectural Concepts Covered

* **Pydantic Data Modeling:** Utilizes `BaseModel` schemas to automatically validate payload data types (strings, integers, booleans) on incoming requests before execution.
* **REST Operations:** Implements core HTTP methods including `GET` for data fetching/filtering and `POST` for array data persistence.
* **Interactive Swagger UI:** Leverages FastAPI's built-in OpenAPI integration to expose an interactive environment (`/docs`) for real-time endpoint testing.

## 🚀 Tutorial & Code Breakdown

<p>1. Create the virtual Environment</p>

```
python3 -m venv venv
```

<h2>2. Activate the Environment</h2>

```
windows -> venv\Scripts\activate.bat
linux -> source venv/bin/activate
mac -> venv/bin/activate
```

<h2>3. Install the FastAPI</h2>
<p>Once the venv is activated, we will install FastApi using pip, the Python package manager.</p>

```
pip install fastapi
```
<h2>Create a API.</h2>
<p>Once FastApi is installed, we will create a file called app.py and import FastApi into it.</p>

```
from fastapi import FastAPI
```

<p>Once the class is imported, we will instantiate it to use its methods.</p>

```
app = FastAPI()
```
<h2>Creating a Hello World</h2>
<p>After instantiating, it's time to test FastApi. We'll use the @ decorator in conjunction with our app instance and the get method, which will point to the home page of our website, where we'll return a "hello world" message as shown in the code below.</p>

```
@app.get('/')
def init():
    return {"data":"Hello World"}
```

<h2>Installing Uvicorn</h2>
<p>After creating our hello world code, we will now test our application, but first we will make sure that Uvicorn is installed to start our application. To install Uvicorn, use the code shown below.</p>

```
pip install uvicorn
```
<h2>Testing FastApi</h2>
<p>After installing uvicorn, we will start our FastAPI with the following command.</p>

```
uvicorn app:app --reload
```
<p>app:app -> is retrieving the file and a variable application within the file.

--reload->Reloads the page every time the file changes.
</p>

<p>Once started, you will see a link to your local application on port 8000, so you will see something more or less like this.</p>

![imagem do terminal](https://i.imgur.com/2atgfXQ.png)

<p>By copying the link and pasting it into your browser, you will likely see an image like this..</p>

![imagem da nossa pagina loca](https://i.imgur.com/WHLP2nX.png)

<p>The JSON you see on your local page is simply the return value we defined above.</p>

<h2>Creating a list.</h2>
<p>Tested and everything working normally. Now we will create a list to store our created users.</p>

```
user_list = []
```

<h2>Creating Models.</h2>
<p>Now we will create another file to store our class models to use as a request template; in this case, we will create one to pass a model in the request.</p>

```
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    drive_license:bool
```

<p>Note that we use BaseModel to facilitate the creation of our class instead of using the Python class pattern; we simply import BaseModel and create our properties.</p>

<h2>Creating a Path to Add a User.</h2>

<p>Once the user model is created, we will create the path using the POST method to add the user and pass the User class as a request in the user class. After that, we will add this user to our user_list and finally return a dictionary or object with "status" and "date" from our user_list.</p>

```
@app.post('/add/user/')
def add_user(user:User):
    
    user_list.append(user)

    return {
        "Status":"ok",
        "data":user_list
        }
```
<h2>Testing our application</h2>
<p>Having completed all the steps above, let's test our application. We will start our fastapi application using uvicorn as described above, and in your browser's URL bar, enter the following URL below to test our application.</p>

```
http://127.0.0.1:8000/docs
```
<p>You will see the URLs you created in your app.py file.</p>

![imagem fastapi docs](https://i.imgur.com/9N3ukA4.png)

<p>Clicking on the Add User path will open the option for you to pass the information by clicking on <b>try it out</b> and note that the model that was passed is the same as the one we defined. Once the parameters are filled in, click on execute and you will get the following response if everything is correct.</p>

![imagem fastapi resposta](https://i.imgur.com/XO7jRJl.png)

<p>A response with status 200 and the return you defined.</p>

<h2>Searching for a User</h2>
<p>Having completed the steps above, let's now implement it using the get method, which will return the user's data through a search by name. The code follows below.</p>

```
@app.get('/user/{nome}')
def get_user(nome:str):

    for usuario in user_list:
        if(usuario.name == nome):
            return {"data":usuario}

    return {"data":user_list}  
```
<p>The code will iterate through the user_list and compare it to the name in my request at the path "name", and when it finds it, it will return the user's data. Go to the fastapi documentation at http://127.0.0.1:8000/docs and add a user using the method above, and then go to the path /user/{name}.</p>

![imagem doc fastapi](https://i.imgur.com/B161t8q.png)

<p>Clicking the link will create a blank space where you can type the name you want to search for. Type a name you added using the example above and click execute.</p>

<p>Since you provided the path, {name} will also work if you type http://127.0.0.1:8000/user/{name} in your search bar. Of course, in place of {name} you will type the name you are looking for, like http://127.0.0.1:8000/user/Carlos</p>

![imagem doc fastapi](https://i.imgur.com/HLjAQwZ.png)

<p>And you will get a return with status 200 and the data for the name you searched for.</p>

![imagem doc fastapi](https://i.imgur.com/Ig68rlV.png)

<h2>Conclusion</h2>

<p>There you go, you just created an API using FastApi. Adding users and returning users by searched name, it was pretty simple with FastApi, right?</p>
