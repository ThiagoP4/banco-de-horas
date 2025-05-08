import tkinter as tk
from tkinter import *
from datetime import datetime, timedelta
from tkinter import messagebox

# Função para ler as entradas e saídas do arquivo, considerando a data
def ler_arquivo():    
    hora_entrada = []
    entra_almoco = []
    saida_almoco = []
    hora_saida = []
    datas = []

    with open("thiago.txt", "r", encoding="utf-8") as f:

        for linha in f:
            if not linha.strip():
                continue # Ignora as linhas vazias
            
            try:
                data_str, h1, h2, h3, h4 = linha.strip().split()

                data = datetime.strptime(data_str, "%d/%m/%Y")

                # Adicionando data e horários à lista
                hora_entrada.append(datetime.strptime(h1,"%H:%M").replace(year=data.year, month=data.month, day=data.day))
                entra_almoco.append(datetime.strptime(h2,"%H:%M").replace(year=data.year, month=data.month, day=data.day))
                saida_almoco.append(datetime.strptime(h3,"%H:%M").replace(year=data.year, month=data.month, day=data.day))
                hora_saida.append(datetime.strptime(h4,"%H:%M").replace(year=data.year, month=data.month, day=data.day))
                datas.append(data)
            except ValueError as e:
                print(f"Erro ao processar linha: {linha.strip()} -> {e}")
        return datas, hora_entrada, entra_almoco, saida_almoco, hora_saida


# Função para calcular o banco de horas
def calcular_horas(horas_entrada, entra_almoco, saida_almoco, horas_saida, resultado_label):
    carga_horaria = timedelta(hours=6)
    banco = timedelta(0)

    for entrada, e_almoco, s_almoco, saida in zip(horas_entrada, entra_almoco, saida_almoco, horas_saida):
        diferenca = (saida - entrada) - (s_almoco - e_almoco) # Calcula o tempo trabalhado
                        #9 horas        #1 hora
        if diferenca < carga_horaria:
            falta = carga_horaria - diferenca
            banco -= falta
            print(f'falta: {falta}')
        else:
            sobrando = diferenca - carga_horaria
            banco += sobrando
            print(f'sobrando: {sobrando}')

    # Converter o banco de horas para horas e minutos corretamente
    total_segundos = abs(banco.total_seconds())  # Pega o valor absoluto para evitar dias negativos
    horas_banco = int(total_segundos // 3600)  # Extrai as horas
    minutos_banco = int((total_segundos % 3600) // 60)  # Extrai os minutos

    sinal = '-' if banco < timedelta(0) else '+'

    # Formatando a exibição corretamente
    resultado = f'{sinal} {horas_banco:02}:{minutos_banco:02}'

    # Atualiza o texto no label com o resultado formatado
    resultado_label.config(text=f'Banco de Horas: {resultado}')


# Função para a interface gráfica
def Banco_horas():
    root = tk.Tk()
    root.title("Banco de Horas")
    root.geometry("800x700")

    compensa = tk.IntVar(value=0)

    data_atual = datetime.now().strftime("%d/%m")
    data_var = tk.StringVar(value=data_atual)
    
    ano_atual = datetime.now().strftime("%Y")
    ano_var = tk.StringVar(value=ano_atual)

    # Label para mostrar o banco de horas
    resultado_label = tk.Label(root, text="Banco de Horas: 00:00", font=("Arial", 16))
    resultado_label.pack(pady=20)

    frame_data = tk.Frame(root)
    frame_data.pack(pady=5)

    # Usar frame_data como contêiner para os elementos com grid
    data_label = tk.Label(frame_data, text="Data (dd/mm):", font=("Arial", 12))
    data_label.grid(row=0, column=0, padx=5, pady=2)
    data_entry = tk.Entry(frame_data, width=10, font=("Arial", 16), textvariable=data_var, justify="center")
    data_entry.grid(row=1, column=0, padx=5, pady=(0,40))

    ano_label = tk.Label(frame_data, text='Ano (yyyy):', font=("Arial", 12))
    ano_label.grid(row=0, column=1, padx=5, pady=2)
    ano_entry = tk.Entry(frame_data, width=10, font=("Arial", 16), textvariable=ano_var, justify="center")
    ano_entry.grid(row=1, column=1, padx=5, pady=(0,40))

    entrada_label = tk.Label(frame_data, text="Hora de Entrada (HH:MM):", font=("Arial", 12), )
    entrada_label.grid(row=2, column=0, padx=15, pady=5)
    entrada_entry = tk.Entry(frame_data, width=10, font=("Arial", 16), justify="center")
    entrada_entry.grid(row=3, column=0, pady=5, padx=15)

    e_almoco_label = tk.Label(frame_data, text="Entrada de Almoço (HH:MM):", font=("Arial", 12))
    e_almoco_label.grid(row=2, column=1, padx=15, pady=5)
    e_almoco_entry = tk.Entry(frame_data, width=12, font=("Arial", 16), justify="center")
    e_almoco_entry.grid(row=3, column=1, padx=15)

    saida_label = tk.Label(frame_data, text="Hora de Saída (HH:MM):", font=("Arial", 12))
    saida_label.grid(row=4, column=0, padx=15, pady=5)
    saida_entry = tk.Entry(frame_data, width=12, font=("Arial", 16), justify="center")
    saida_entry.grid(row=5, column=0, padx=15, pady=(0, 80))

    s_almoco_label = tk.Label(frame_data, text="Saída de Almoço (HH:MM):", font=("Arial", 12))
    s_almoco_label.grid(row=4, column=1, padx=15, pady=5)
    s_almoco_entry = tk.Entry(frame_data, width=12, font=("Arial", 16), justify="center")
    s_almoco_entry.grid(row=5, column=1, padx=15, pady=(0, 80))

    def compensar_horas():
        if compensa.get() == 1:
            # Marcar: coloca "00:00" e desativa os campos
            entrada_entry.delete(0, tk.END)
            entrada_entry.insert(0, "00:00")
            entrada_entry.config(state='disabled')

            e_almoco_entry.delete(0, tk.END)
            e_almoco_entry.insert(0, "00:00")
            e_almoco_entry.config(state='disabled')

            s_almoco_entry.delete(0, tk.END)
            s_almoco_entry.insert(0, "00:00")
            s_almoco_entry.config(state='disabled')

            saida_entry.delete(0, tk.END)
            saida_entry.insert(0, "00:00")
            saida_entry.config(state='disabled')
        else:
            # Desmarcar: limpa e reativa os campos
            entrada_entry.config(state='normal')
            entrada_entry.delete(0, tk.END)

            e_almoco_entry.config(state='normal')
            e_almoco_entry.delete(0, tk.END)

            s_almoco_entry.config(state='normal')
            s_almoco_entry.delete(0, tk.END)

            saida_entry.config(state='normal')
            saida_entry.delete(0, tk.END)

    linha_frame2 = tk.Frame(root)
    linha_frame2.pack(pady=10)

    # Função para adicionar uma nova linha no arquivo (só chamada quando o botão for clicado)
    def adicionar_horas():

        data = data_entry.get() + '/' + ano_entry.get()
        db_data, *_ = ler_arquivo()

        data_banco = [d.strftime("%d/%m/%Y") for d in db_data]
        
        # Verifica se a data está no formato correto
        try:
            datetime.strptime(data, "%d/%m/%Y")  # Verifica se a data está no formato dd/mm/aaaa
        except ValueError:
            print("Formato de data inválido. Use dd/mm.")  # Erro simples para depuração
            return
        

        if compensa.get() == 1:
            entrada = "00:00"
            e_almoco = "00:00"
            s_almoco = "00:00"
            saida = "00:00"
        else:
            entrada = entrada_entry.get()
            e_almoco = e_almoco_entry.get()
            s_almoco = s_almoco_entry.get()
            saida = saida_entry.get()

        try:
            if data in data_banco:  # Verifica se a data já existe
                raise ValueError("O ponto deste dia já foi cadastrado.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        # Escreve no arquivo
        with open("thiago.txt", "a", encoding="utf-8") as f:
            f.write(f"{data} {entrada} {e_almoco} {s_almoco} {saida}\n")

        # Limpar os campos após a adição
        data_entry.delete(0, tk.END)
        entrada_entry.delete(0, tk.END)
        e_almoco_entry.delete(0, tk.END)
        s_almoco_entry.delete(0, tk.END)  
        saida_entry.delete(0, tk.END)

    tk.Button(linha_frame2, text="Enviar", command=adicionar_horas).grid(row=0, column=0, padx=(350, 10))
    Checkbutton(linha_frame2, text='Horas a Compensar?', variable=compensa, onvalue=1, offvalue=0, command=compensar_horas).grid(row=0, column=1, sticky='w', padx=(200,0))

    # Função para calcular o banco de horas (quando for clicado)
    def calcular_banco():
        datas, hora_entrada, entra_almoco, saida_almoco, hora_saida = ler_arquivo()
        calcular_horas(hora_entrada, entra_almoco, saida_almoco, hora_saida, resultado_label)

    # Função para exibir o banco de horas em uma nova janela
    def exibir_banco():
        banco = tk.Toplevel(root)  # Cria uma nova janela (Toplevel)
        banco.title("Banco de Horas")
        banco.geometry("500x500")
        
        meses = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
        "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
        "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
        }


        # Criando um Frame para conter a área de texto e a barra de rolagem
        frame = tk.Frame(banco)
        frame.pack(fill=tk.BOTH, expand=True)

        # Criando uma barra de rolagem vertical
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Criando um widget Text para exibir o conteúdo
        text_widget = tk.Text(frame, wrap="none", yscrollcommand=scrollbar.set, font=("Arial", 12))
        text_widget.pack(fill=tk.BOTH, expand=True)

        # Configurando a barra de rolagem para rolar o conteúdo do widget Text
        scrollbar.config(command=text_widget.yview)

        # Lê os dados do arquivo
        datas, hora_entrada, entra_almoco, saida_almoco, hora_saida = ler_arquivo()

        mes_atual = None

        # Exibindo o conteúdo do banco de horas
        resultado = ""
        for d, e, ea, sa, s in zip(datas, hora_entrada, entra_almoco, saida_almoco, hora_saida):
            mes = d.strftime('%m')
            ano = d.strftime('%Y')
            nome_mes = meses[mes]
            mes = f"{nome_mes} de {ano}"

            if mes_atual != (mes, ano):
                mes_atual = (mes, ano)
                resultado += f"\n{nome_mes} de {ano}\n"
            resultado += f"{d.strftime('%d/%m')} - Entrada: {e.strftime('%H:%M')} - Saída: {s.strftime('%H:%M')} - Almoco: {ea.strftime('%H:%M')} - {sa.strftime('%H:%M')}\n"

        # Inserindo o resultado no widget Text
        text_widget.insert(tk.END, resultado)
        text_widget.config(state=tk.DISABLED)  # Impede edição do conteúdo


    # Botão para adicionar a entrada
    frame_linha3 = tk.Frame(root)
    frame_linha3.pack(pady=(200,0))

    tk.Button(frame_linha3, text="Calcular Banco de Horas", command=calcular_banco).grid(row=0, column=0, padx=10)
    tk.Button(frame_linha3, text="Exibir Banco de Horas", command=exibir_banco).grid(row=0, column=1, padx=10)

    # Rodando a interface gráfica
    root.mainloop()

# Chamada da função que cria a interface gráfica
Banco_horas()
