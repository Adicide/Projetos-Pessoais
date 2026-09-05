import time
from datetime import datetime

opcao = None
hoje = datetime.now()
hora_atual = hoje.hour

while True:
    print("BEM-VINDO AO CONVERSOR DE HORAS.\nSELECIONE UMA DAS OPÇÕES ABAIXO.\n")
    print("1 - CONVERTER [h] EM [h e min]")
    print("2 - CONVERTER [h e min] EM [h]")
    print("3 - SAIR DO CONVERSOR DE HORAS")
    
    opcao = int(input("\nINSIRA SUA OPÇÃO: "))
    if opcao == 1:
        
        tempo_h = float(input('DIGITE O TEMPO EM HORAS (ex: 4.5): '))
        if tempo_h < 0:
            print("ERRO: NÃO EXISTE TEMPO NEGATIVO.")
            time.sleep(3)
            continue
        
        horas = int(tempo_h) # Extrai a parte inteira de tempo_h (em 4.5h, ele pega apenas as 4h completas)
        minutos = int((tempo_h - horas) * 60) # Extrai a parte decimal da hora (em 4.5, 0.5) e converte em minutos

        print(f'[{tempo_h} h] CORRESPONDEM A [{horas} h e {minutos} min.]\n')
        time.sleep(3)
        continue
    
    elif opcao == 2:
        
        tempo_h = int(input('INSIRA AS HORAS (ex: 1h): '))
        if tempo_h < 0:
            print("ERRO: NÃO EXISTEM HORAS NEGATIVAS.")
            time.sleep(3)
            continue
        
        tempo_m = int(input('INSIRA OS MINUTOS (ex: 30min): '))
        if tempo_m < 0:
            print("ERRO: NÃO EXISTEM MINUTOS NEGATIVOS.")
            time.sleep(3)
            continue
            
        horas = int(tempo_h)
        minutos = float((tempo_m) / 60) # Divide o inteiro minutos por 60 e converte o resultado int em float (para permite decimal)
        tempo_final = float(horas + minutos) # Soma as horas completas (inteiras) e as horas decimais, convertendo em float

        print(f'\n[{horas} h e {tempo_m:.0f} min] CORRESPONDEM A [{tempo_final:.2f} h.]\n')
        time.sleep(3)
        continue
    
    elif opcao == 3:
        print("SAINDO DO PROGRAMA...")
        time.sleep(3)
        
        if 5 <= hora_atual < 12:
            print("VOCÊ SAIU DO CONVERSOR DE HORAS. UM BOM DIA E ATÉ A PRÓXIMA!")
        elif 12 <= hora_atual < 18:
            print("VOCÊ SAIU DO CONVERSOR DE HORAS. UMA BOA TARDE E ATÉ A PRÓXIMA!")
        else:
            print("VOCÊ SAIU DO CONVERSOR DE HORAS. UMA BOA NOITE E ATÉ A PRÓXIMA!")
            
        break
    else:
        print("ERRO: VOCÊ SELECIONOU UMA OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
        time.sleep(3)
        continue