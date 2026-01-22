import time
import schedule

# função que será agendada
def dizer_ola():
    print(20*'-')
    print('Olá, isso é um agendamento!')
    print(20*'-')

# função de agendamento
def agendamento():
    schedule.every(2).seconds.do(dizer_ola)
    while True:
        schedule.run_pending()
        time.sleep(1)
# execução do agendamento
agendamento()
