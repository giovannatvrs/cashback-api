from fastapi import APIRouter, Depends, Request
from backend import schemas, models, database
from sqlalchemy.orm import Session

router = APIRouter(prefix="/cashback", tags=["cashback"])

def get_client_ip(request: Request):
    ip = request.headers.get("x-forwarded-for")

    if ip:
        ip = ip.split(",")[0]
    else:
        ip = request.client.host

    if ip == "::1":
        ip = "127.0.0.1"

    return ip

@router.post("/", response_model=schemas.ConsultaResponse)
async def calcular_cashback(consulta: schemas.ConsultaRequest, request: Request, db: Session = Depends(database.get_db)):
    valor_final = consulta.valor_compra - (consulta.valor_compra * consulta.percentual_desconto/100)

    cashback_base = valor_final * 5/100
    if consulta.tipo_cliente == "VIP":
        cashback = cashback_base + cashback_base * 10/100
    else:
        cashback = cashback_base
    
    if valor_final > 500:
        cashback *= 2

    

    db_consulta = models.Consulta(
        ip_usuario = get_client_ip(request),
        tipo_cliente = consulta.tipo_cliente,
        valor_compra =  consulta.valor_compra,
        valor_final = valor_final,
        cashback = cashback,
        percentual_desconto = consulta.percentual_desconto,

    )

    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)

    return {
        "cashback": cashback
    };

@router.get("/consultas", response_model=list[schemas.HistoricoResponse])
async def exibir_historico_consultas(request: Request, db: Session = Depends(database.get_db)):
    ip = get_client_ip(request)
    consultas = db.query(models.Consulta).filter(models.Consulta.ip_usuario == ip).order_by(models.Consulta.data_consulta.desc()).all()
    return consultas;
