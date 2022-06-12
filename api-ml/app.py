from flask import Flask

from mlkit.app.controller.getCleanTextsController import (GetCleanTextsController)
app = Flask(__name__)
from bootstrap.bootstrap import Init 



@app.route('/')
def hello_world(): 
    return 'Hello World!'

@app.route('/hola')
async def prueba():
    res =  await GetCleanTextsController.handle()
    return 'BIEN'

if __name__ == '__main__':
    app.run(debug=True)

