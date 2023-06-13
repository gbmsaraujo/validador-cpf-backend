from pydantic import BaseModel

class ValidaCPF(BaseModel):
    cpf: str

