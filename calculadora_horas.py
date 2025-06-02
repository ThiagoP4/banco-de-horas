from datetime import datetime, timedelta

# Função para calcular o banco de horas
def calcular_horas(horas_entrada, entra_almoco, saida_almoco, horas_saida, semana_prova):
    carga_horaria_normal = timedelta(hours=8)
    banco = timedelta(0)

    if not horas_entrada: # Se a lista de entradas estiver vazia, não há o que calcular
        return "+00:00"
    
    for entrada, e_almoco, s_almoco, saida, sp in zip(horas_entrada, entra_almoco, saida_almoco, horas_saida, semana_prova):
        
        # Verifica se os campos de almoço estão vazios ou são "00:00"
        if e_almoco.time() == datetime.strptime("00:00", "%H:%M").time() and s_almoco.time() == datetime.strptime("00:00", "%H:%M").time():
            diferenca = saida - entrada  # Ignora almoço
        else:
            diferenca = (saida - entrada) - (s_almoco - e_almoco)  # Cálculo normal

        carga_horaria = carga_horaria_normal / 2 if int(sp) == 1 else carga_horaria_normal

        if diferenca < carga_horaria:
            falta = carga_horaria - diferenca
            banco -= falta
            #print(f'falta: {falta}')
        else:
            sobrando = diferenca - carga_horaria
            banco += sobrando
            #print(f'sobrando: {sobrando}')

    # Converter o banco de horas para horas e minutos corretamente
    total_segundos = abs(banco.total_seconds())  # Pega o valor absoluto para evitar dias negativos
    horas_banco = int(total_segundos // 3600)  # Extrai as horas
    minutos_banco = int((total_segundos % 3600) // 60)  # Extrai os minutos

    sinal = '-' if banco < timedelta(0) else '+'

    # Formatando a exibição corretamente
    resultado = f'{sinal} {horas_banco:02}:{minutos_banco:02}'

    # Atualiza o texto no label com o resultado formatado
    return resultado


def ler_arquivo(db_manager_instance):    
    registros = db_manager_instance.get_all_horarios()

    idhorario = []
    hora_entrada = []
    entra_almoco = []
    saida_almoco = []
    hora_saida = []
    datas = []
    semana_prova = []


    if registros is None: # Verifica se get_all_horarios pode retornar None
        registros = []

    for registro in registros:
        
        try:
            # Adicionando data e horários à lista
            idhorario.append(registro[0])
            data = datetime.strptime(registro[1], "%d/%m/%Y")
            datas.append(data)
            hora_entrada.append(datetime.strptime(registro[2],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
            entra_almoco.append(datetime.strptime(registro[3],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
            saida_almoco.append(datetime.strptime(registro[4],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
            hora_saida.append(datetime.strptime(registro[5],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
            
            semana_prova.append(registro[6]) #armazena 0 ou 1

        except Exception as e:
            print(f"Erro ao processar o registro {registro}: {e}")

    return idhorario, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova
