import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# creo una instancia
app = FastAPI()

# Coloco un decorador y defino una función para consumir
@app.get('/')

def get_list():
    return[1,2,3]

#@app.get('/contact')
@app.get("/contact/", response_class=HTMLResponse)
def get_list():
    #return{'name':'Platzi'}
    return """
    <h1>Mi primera prueba con el servidor web con python</h1>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()