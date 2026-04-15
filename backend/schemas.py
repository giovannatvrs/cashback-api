from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime
import decimal


class ConsultaRequest(BaseModel):
    tipo_cliente: str
    valor_compra: decimal.Decimal
    percentual_desconto: int 

    @field_validator('valor_compra')
    def validar_valor(cls, v):
        if v <= 0:
            raise ValueError("Valor deve ser maior que zero")
        return v

    @field_validator('percentual_desconto')
    def validar_desconto(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Desconto inválido")
        return v
    
    model_config = ConfigDict(from_attributes=True)

class ConsultaResponse(BaseModel):
    cashback: decimal.Decimal
    
    model_config = ConfigDict(from_attributes=True)

class HistoricoResponse(BaseModel):
    tipo_cliente: str
    valor_compra: decimal.Decimal
    valor_final: decimal.Decimal
    cashback: decimal.Decimal
    data_consulta: datetime

    model_config = ConfigDict(from_attributes=True)