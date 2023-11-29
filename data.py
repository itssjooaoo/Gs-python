from datetime import datetime
datetime.now()
data=datetime.fromisoformat("2023-11-24")
print(data)



consulta=[["joao", "2023-4-15", "febre"], ["herbert", "2023-1-13", "dor"]]

def adiciona_ocorrencia():
    usuario = input("digite nome do usuario: ")
    data = input("digite a data da ocorrencia: ")
    ocorrencia = input("digite a ocorrencia: ")
    consulta.append([usuario, data, ocorrencia])


usuario=input("digite nome do usuario")
for registro in consulta:
     if registro[0]== usuario:
             print(registro)




             usuario = input("Área destinada a consultas passadas, de o nome do usuario ")
data = (input("Gostaria de consultar a data? S ou n"))
if data == "S":
            data_consulta=datetime.fromisoformat(input("Deseja consultar qual data de consulta:(2022-02-15, 2022-06-23) Digite a data no formato \"yyyy-mm-dd\""))
if data_consulta== "2022-02-15":
        print("Nessa consulta você estava com dor de garganta, \n ninfonodos inchados com alteração de BPM, foi-lhe recomendado uma tomografia")

if data_consulta == "2022-06-23":
        print("")
