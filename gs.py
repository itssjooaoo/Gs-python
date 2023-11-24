
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

    
        
        data = (input("Gostaria de consultar a data? S ou n"))
        if data == "S":
           consulta=[["joao", "2023-4-15", "febre"], ["herbert", "2023-1-13", "dor"]]
        

        print(f"Nesta data {data_consulta} você teve alteração sanguinea grave")


        quantidade = int(input("Digite a quantidade: "))
        consultar_consulta(usuario, data, ocorrencia)
    elif opcao == 2:
        listar_estoque()
    elif opcao == 3:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser adicionada ou subtraida: "))