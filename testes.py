from app import create_app, db
from app.models import Agendamento
from datetime import date, time

app = create_app()
app.app_context().push()

db.session.query(Agendamento).delete()
db.session.commit()

agendamento = Agendamento(
    id_usuario=1,               
    data_reserva=date(2026, 2, 5),
    hora_inicial=time(13, 0),
    hora_final=time(14, 0),
    validacao='EM_ANALISE',    
    id_estacao=1,               
    observacao='Teste simples'
)

db.session.add(agendamento)
db.session.commit()

print("Agendamento criado com sucesso!")
print(f"Número total de agendamentos: {Agendamento.query.count()}")