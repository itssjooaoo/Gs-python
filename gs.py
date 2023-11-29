
from datetime import datetime

consulta=[["joao", "2023-4-15", "febre"], ["herbert", "2023-1-13", "dor"]]
def adiciona_ocorrencia():
    usuario = input("digite nome do usuario: ")
    data = input("digite a data da ocorrencia: ")
    ocorrencia = input("digite a ocorrencia: ")
    consulta.append([usuario, data, ocorrencia])

def lista_ocorrencias():
    for registro in consulta:
        print(registro)
def consultar_consulta(usuario, data,):
    consulta.append((usuario, data,))

def agendar_consulta(nome_area, lista_consultas):
    consulta = {'Nome da Área': nome_area, 'Status': 'Agendado'}
    lista_consultas.append(consulta)

def ver_consultas(lista_consultas):
    print("\nConsultas Agendadas:")
    for consulta in lista_consultas:
        print(f"Área: {consulta['Nome da Área']} - Status: {consulta['Status']}")

lista_consultas = []



while True:
    print("\n1. Consulta")
    print("2. Saúde")
    print("3. Exames")
    print("4. Agendamento")
    print("5. Lembretes")

    opcao = int(input("Fale a opção que deseja acessar: "))

    if opcao == 1:
        adiciona_ocorrencia()
    if opcao == 2:
        lista_ocorrencias()
    if opcao == 3:
        # Na área de exames mostramos exames pendentes onde você deve ver os exames pedidos e agendar na opção 4
        print(" Você tem a fazer os seguintes exames: Hemograma, Glicemia em jejum e exame de urina. Vá até a opção Agendamento para agendalos.")
    if opcao == 4:
        nome_area = input("Digite o nome da área para agendar a consulta: ")
        agendar_consulta(nome_area, lista_consultas)
    if opcao == 5:
        ver_consultas(lista_consultas)
    if opcao == 6:
        break
    else:
        ("opção invalida.")

        