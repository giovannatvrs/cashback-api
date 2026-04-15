from backend.database import Base
from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime, timezone

def agora_utc():
    return datetime.now(timezone.utc)

class Consulta(Base):
    __tablename__= "consultas"

    id = Column(Integer, primary_key=True)
    ip_usuario = Column(String(45), nullable=False)
    tipo_cliente = Column(String, nullable=False)
    valor_compra = Column(Numeric(10,2), nullable=False)
    percentual_desconto = Column(Integer, default=0, nullable=False)
    valor_final = Column(Numeric(10,2), nullable=False)
    cashback = Column(Numeric(10,2), nullable=False)
    data_consulta = Column(DateTime(timezone=True), default=agora_utc)


