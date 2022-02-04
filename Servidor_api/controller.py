from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re
import uvicorn
import hashlib

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=["*"],
)


class controllerCadastro:

    @classmethod
    def verificaDados(cls, nome, email, password):
        '''
        :param nome:
        :param email:
        :param senha:
        :return: 1 Cadastro realizado com sucesso
        :return: 2 quantidade minima de letras no nome
        :return: 3 Email invalido
        :return: 4 Senha precisa ser forte
        '''
        if len(nome) < 5 or len(nome) > 100:
            return 2
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return 3
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])(?:([0-9a-zA-Z$*&@#])(?!\1)){8,}$", password):
            return 4
        return 1


@app.get("/")
def main():
    return {'massenger' :'Home'}

@app.post("/cadastro")
def cadastro(user: str, email: str , senha: str):
    return {'massenger' :'cadastro'}



if __name__ == "__main__":
    uvicorn.run("controller:app", port=8000, reload=True, access_log=False)