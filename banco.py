import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import sqlite3
from sqlite3 import Error

from db_manager import DatabaseManager


db_manager = DatabaseManager()

# Função para ler as entradas e saídas do arquivo, considerando a data
def ler_arquivo():    
    registros = db_manager.get_all_horarios()

    idhorario = []
    hora_entrada = []
    entra_almoco = []
    saida_almoco = []
    hora_saida = []
    datas = []
    semana_prova = []
    


    for registro in registros:

        # Adicionando data e horários à lista
        idhorario.append(registro[0])
        data = datetime.strptime(registro[1], "%d/%m/%Y")
        datas.append(data)
        hora_entrada.append(datetime.strptime(registro[2],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
        entra_almoco.append(datetime.strptime(registro[3],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
        saida_almoco.append(datetime.strptime(registro[4],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
        hora_saida.append(datetime.strptime(registro[5],"%H:%M").replace(year=data.year, month=data.month, day=data.day))
        
        semana_prova.append(registro[6]) #armazena 0 ou 1

    return idhorario, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova


# Função para calcular o banco de horas
def calcular_horas(horas_entrada, entra_almoco, saida_almoco, horas_saida, resultado_label, semana_prova):
    carga_horaria_normal = timedelta(hours=8)
    banco = timedelta(0)
    
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
    sprova = tk.IntVar(value=0)

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
        horarios_existentes = db_manager.get_all_horarios()
        data_banco = [h[1] for h in horarios_existentes]

        # Verifica se a data está no formato correto
        try:
            datetime.strptime(data, "%d/%m/%Y")  # Verifica se a data está no formato dd/mm/aaaa
        except ValueError as e:
            messagebox.showerror("Erro", "Formato de data inválido. Use dd/mm.")
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
    
        sp = sprova.get() #Pega o valor da checkbox

        if db_manager.insert_horario(data, entrada, e_almoco, s_almoco, saida, sp):
            messagebox.showinfo("Sucesso", "Horário adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Não foi possível adicionar o horário.")

        # Limpar os campos após a adição
        data_entry.delete(0, tk.END)
        entrada_entry.delete(0, tk.END)
        e_almoco_entry.delete(0, tk.END)
        s_almoco_entry.delete(0, tk.END)  
        saida_entry.delete(0, tk.END)
        data_var.set(datetime.now().strftime("%d/%m")) # Reseta para a data atual
        compensa.set(0) # Desmarca o checkbox
        sprova.set(0) # Desmarca o checkbox

    tk.Button(linha_frame2, text="Enviar", command=adicionar_horas).grid(row=0, column=0, padx=(350, 10))
    Checkbutton(linha_frame2, text='Horas a Compensar?', variable=compensa, onvalue=1, offvalue=0, command=compensar_horas).grid(row=0, column=1, sticky='w', padx=(200,0))
    Checkbutton(linha_frame2, text='Semana de Prova?', variable=sprova, onvalue=1, offvalue=0).grid(row=1, column=1, sticky='w', padx=(200,0))


    # Função para calcular o banco de horas (quando for clicado)
    def calcular_banco():
        _, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova = ler_arquivo()
        calcular_horas(hora_entrada, entra_almoco, saida_almoco, hora_saida, resultado_label, semana_prova)

    # Função para exibir o banco de horas em uma nova janela
    def exibir_banco():
        banco = tk.Toplevel(root)  # Cria uma nova janela (Toplevel)
        banco.title("Banco de Horas")
        banco.geometry("650x600")

        # Criando uma NAV 
        nav = tk.Frame(banco)
        nav.pack(fill=tk.X)

        # Criando um Frame para conter a área de texto e a barra de rolagem
        frame = tk.Frame(banco)
        frame.pack(fill=tk.BOTH, expand=True)

        # Criando uma barra de rolagem vertical
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        tree = ttk.Treeview(
            frame, 
            columns=("id", "data", "entrada", "entrada_almoco", "saida_almoco", "saida", "semana_de_prova"), 
            show="headings",
            yscrollcommand=scrollbar.set
        )
        tree.pack(fill=tk.BOTH, expand=True)

        # Definindo cabeçalhos da tabela
        tree.heading("id", text="ID")
        tree.heading("data", text="Data")
        tree.heading("entrada", text="Entrada")
        tree.heading("entrada_almoco", text="Almoço Início")
        tree.heading("saida_almoco", text="Almoço Fim")
        tree.heading("saida", text="Saída")
        tree.heading("semana_de_prova", text="Semana de Prova")

        tree.column("id", width=50, anchor="center")
        tree.column("data", width=50, anchor="center")
        tree.column("entrada", width=50, anchor="center")
        tree.column("entrada_almoco", width=50, anchor="center")   
        tree.column("saida_almoco", width=50, anchor="center")
        tree.column("saida", width=50, anchor="center")
        tree.column("semana_de_prova", width=50, anchor="center")

        # Lê os dados do arquivo
        idhorario, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova = ler_arquivo()

        # Exibindo o conteúdo do banco de horas
        for id, d, e, ea, sa, s, sp in zip(idhorario, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova):
            tree.insert("", tk.END, values=(
            id,
            d.strftime("%d/%m/%Y"),
            e.strftime("%H:%M"),
            ea.strftime("%H:%M"),
            sa.strftime("%H:%M"),
            s.strftime("%H:%M"),
            "✅" if sp == '1' else "❌"
        ))
            

        def on_tree_select(event):
            selected_items = tree.selection() # Obtem os itens selecionados
            if selected_items:
                item = selected_items[0] # Pega o primeiro valor
                values = tree.item(item, "values") # Obtem os valores da linha
                id_selected = values[0]
                print(f"ID selecionado: {id_selected}")
        tree.bind("<<TreeviewSelect>>", on_tree_select) # Vincula o evento de seleção ao Treeview
        scrollbar.config(command=tree.yview) # Vincula a barra de rolagem ao Treeview


        def editar(id_selected):
            editar_janela = tk.Toplevel(banco)  # Cria uma nova janela (Toplevel)
            editar_janela.title("Editar Banco de Horas")
            editar_janela.geometry("550x250")

            frame_data = tk.Frame(editar_janela)
            frame_data.pack(pady=5)

            # Usar frame_data como contêiner para os elementos com grid
            entrada_label = tk.Label(frame_data, text="Hora de Entrada (HH:MM):", font=("Arial", 12), )
            entrada_label.grid(row=0, column=0, padx=15, pady=5)
            entrada_entry = tk.Entry(frame_data, width=10, font=("Arial", 16), justify="center")
            entrada_entry.grid(row=1, column=0, pady=5, padx=15)

            e_almoco_label = tk.Label(frame_data, text="Entrada de Almoço (HH:MM):", font=("Arial", 12))
            e_almoco_label.grid(row=0, column=1, padx=15, pady=5)
            e_almoco_entry = tk.Entry(frame_data, width=12, font=("Arial", 16), justify="center")
            e_almoco_entry.grid(row=1, column=1, padx=15)

            saida_label = tk.Label(frame_data, text="Hora de Saída (HH:MM):", font=("Arial", 12))
            saida_label.grid(row=2, column=0, padx=15, pady=5)
            saida_entry = tk.Entry(frame_data, width=12, font=("Arial", 16), justify="center")
            saida_entry.grid(row=3, column=0, padx=15, pady=(0, 80))

            s_almoco_label = tk.Label(frame_data, text="Saída de Almoço (HH:MM):", font=("Arial", 12))
            s_almoco_label.grid(row=2, column=1, padx=15, pady=5)
            s_almoco_entry = tk.Entry(frame_data, width=12, font=("Arial", 16), justify="center")
            s_almoco_entry.grid(row=3, column=1, padx=15, pady=(0, 80))


            def enviar_edicao():
                novos_valores = {
                "entrada": entrada_entry.get() or None,
                "entrada_almoco": e_almoco_entry.get() or None,
                "saida": saida_entry.get() or None,
                "saida_almoco": s_almoco_entry.get() or None,
                "semana_prova": None  # ajuste se for editar isso também
                }
                editar_banco(id_selected, novos_valores)
                editar_janela.destroy()

            # Frame para o botão na parte inferior
            frame_botao = tk.Frame(editar_janela)
            frame_botao.pack(side=tk.BOTTOM, pady=2)

            tk.Button(frame_botao, text="Enviar", font=("Arial", 10), width=15, command=enviar_edicao).pack()

        def editar_banco(id_selected, novos_valores):
            campos_atualizados = {
            "HORA_ENTRADA": novos_valores.get("entrada"),
            "ENTRA_ALMOCO": novos_valores.get("entrada_almoco"),
            "SAIDA_ALMOCO": novos_valores.get("saida_almoco"),
            "HORA_SAIDA": novos_valores.get("saida"),
            "SEMANA_PROVA": novos_valores.get("semana_prova")
    }
            
        
            campos_validos = {campo: valor for campo, valor in campos_atualizados.items() if valor is not None}

            if not campos_validos:
                return  # Nada para atualizar
            
            set_clause = ", ".join([f"{campo} = ?" for campo in campos_validos.keys()])
            valores = list(campos_validos.values())

            conn = sqlite3.connect("banco_database.db")
            cursor = conn.cursor()

            print(set_clause)

            cursor.execute(f"""
                UPDATE HORARIOS 
                SET {set_clause}
                WHERE IDHORARIO = ?
                """, (*valores, id_selected))

            conn.commit()
            conn.close()   
            
    
        def chamar_edicao():
            selected_items = tree.selection()
            if selected_items:
                item = selected_items[0]
                values = tree.item(item, "values")
                id_selected = values[0]
                editar(id_selected)
            else:
                messagebox.showwarning("Atenção", "Selecione uma linha para editar.")

        tk.Button(nav, text="Editar", command=chamar_edicao, borderwidth=0).pack(side=tk.LEFT, padx=10)
    
    # Botão para adicionar a entrada
    frame_linha3 = tk.Frame(root)
    frame_linha3.pack(pady=(200,0))

    tk.Button(frame_linha3, text="Calcular Banco de Horas", command=calcular_banco).grid(row=0, column=0, padx=10)
    tk.Button(frame_linha3, text="Exibir Banco de Horas", command=exibir_banco).grid(row=0, column=1, padx=10)

    # Rodando a interface gráfica
    root.mainloop()

# Chamada da função que cria a interface gráfica
Banco_horas()
