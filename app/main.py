from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ValidaCPF
from fastapi.params import Body
import re
from .utils.cpf_utils import generate_cpf_digits, soma_digitos, valida_cpf, generate_random_cpf
import uvicorn

app = FastAPI()

origins = ["*"]
# allow all domains, but if want to specify which site you want to have acess, pass in te array, ex ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def welcome_api():
    return "Welcome to CPF API by Gabs"

@app.post("/validar-cpf")
def validar_cpf(payload:ValidaCPF = Body):

            cpf_formatado = re.sub(r'[^0-9]', '', payload.cpf)
            nove_digitos = cpf_formatado[:9]
            dez_digitos = cpf_formatado[:10]

            resultado_soma_primeiro_digito = soma_digitos(nove_digitos, 10)
            primeiro_digito = generate_cpf_digits(resultado_soma_primeiro_digito)
            resultado_soma_segundo_digito =  soma_digitos(dez_digitos, 11)
            segundo_digito = generate_cpf_digits(resultado_soma_segundo_digito)
            e_valido = valida_cpf(primeiro_digito, segundo_digito, cpf_formatado)

            return e_valido

@app.get("/gerar-cpf")
def gerar_cpf():
    return generate_random_cpf()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
