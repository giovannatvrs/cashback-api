from pydantic import BaseModel, ConfigDict
from datetime import datetime
import decimal

class ConsultaRequest(BaseModel):
    tipo_cliente: str
    valor_compra: decimal.Decimal
    percentual_desconto: int 
    
    model_config = ConfigDict(from_attributes=True)

class ConsultaResponse(BaseModel):
    valor_final: decimal.Decimal
    cashback: decimal.Decimal
    
    model_config = ConfigDict(from_attributes=True)

class HistoricoResponse(BaseModel):
    tipo_cliente: str
    valor_compra: decimal.Decimal
    valor_final: decimal.Decimal
    cashback: decimal.Decimal
    data_registro: datetime
    
    model_config = ConfigDict(from_attributes=True)