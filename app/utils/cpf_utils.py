import json
import random

def generate_cpf_digits(resultado:int):
    mult_per_10 = 0
    div_per_11 = 0

    mult_per_10 = resultado * 10
    div_per_11 = mult_per_10 % 11


    result_condition = 0 if div_per_11 > 9 else div_per_11

    return result_condition


def soma_digitos(digitos:str, contador):
    count = contador
    resultado = 0
    for numero in digitos:
        resultado += count * int(numero)
        count -= 1
    return resultado

def valida_cpf(digito_um, digito_dois, cpf_formatado):
    try:
        e_valor_repetido = cpf_formatado[0] * len(cpf_formatado)

        if cpf_formatado == e_valor_repetido:
            return {"message":"O CPF Informado é Inválido!", "status": "false"}

        concatena_digitos = f"{digito_um}{digito_dois}"
        dois_ultimos_digitos = cpf_formatado[-2:]
        is_valid = {"message":"O CPF Informado é Válido!", "status": "true"} if concatena_digitos == dois_ultimos_digitos else {"message":"O CPF Informado é Inválido!", "status": "false"}

        return is_valid
    except:
        return {"message":"Valor Digitado Incorreto, Tente Novamente!", "status": "error"}

def generate_random_cpf():
        generated_number = ''
        for _ in range(9):
            generated_number += str(random.randint(0,9))
        soma_9_digitos = soma_digitos(generated_number, 10)
        digito_1 = generate_cpf_digits(soma_9_digitos)
        ten_digits = f"{generated_number}{digito_1}"
        soma_10_digitos = soma_digitos(ten_digits, 11)
        digito_2 = generate_cpf_digits(soma_10_digitos)

        cpf_generated = f"{generated_number}{digito_1}{digito_2}"

        return '{}.{}.{}-{}'.format(cpf_generated[:3], cpf_generated[3:6], cpf_generated[6:9], cpf_generated[9:])
