import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta
import sqlite3
from sqlite3 import Error

from db_manager import DatabaseManager
from calculadora_horas import calcular_horas, ler_arquivo

db_manager = DatabaseManager()


DATE_FORMAT_DISPLAY = "%d/%m/%Y"
DATE_FORMAT_DB = "%Y-%m-%d"

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

        display = data_var.get() + '/' + ano_var.get()

        try:
            # Converte a string da tela em um objeto datetime (isso valida a data)
            data_disp = datetime.strptime(display, DATE_FORMAT_DISPLAY)
            # Converte o objeto para o formato do banco de dados (YYYY-MM-DD)
            data_db = data_disp.strftime(DATE_FORMAT_DB)
        except ValueError:
            messagebox.showerror("Erro", f"Formato de data inválido. Use o formato {DATE_FORMAT_DISPLAY.replace('%d','dd').replace('%m','mm').replace('%Y','yyyy')}.")
            return

        horarios_existentes = db_manager.get_all_horarios()
        data_banco = [h[1] for h in horarios_existentes]


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
            if data_db in data_banco:  # Verifica se a data já existe
                raise ValueError("O ponto deste dia já foi cadastrado.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return   
    
        sp = sprova.get() #Pega o valor da checkbox

        if db_manager.insert_horario(data_db, entrada, e_almoco, s_almoco, saida, sp):
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
        _, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova = ler_arquivo(db_manager)

        if not datas: # Se a lista de datas estiver vazia, não há o que calcular
            resultado_label.config(text="Banco de Horas: (sem dados)")
            return
        
        saldo = calcular_horas(hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova)

        resultado_label.config(text=f'Banco de Horas: {saldo}')

    # Função para exibir o banco de horas em uma nova janela
    def exibir_banco():
        banco = tk.Toplevel(root)  # Cria uma nova janela (Toplevel)
        banco.title("Banco de Horas")
        banco.geometry("650x600")
        banco.transient(root)
        banco.grab_set()

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

        # Função interna para popular a treeview (para reutilização)
        def _popular_treeview_interno(tree_widget):
            # 1. Limpa a treeview antes de popular
            for i in tree_widget.get_children():
                tree_widget.delete(i)
            
            idhorario, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova = ler_arquivo(db_manager)

            # 3. Exibe o conteúdo na treeview
            for id_val, data_val, entra_val, entra_almoco_val, saida_almoco_val, saida_val, sp_val in zip(idhorario, datas, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova):
                tree_widget.insert("", tk.END, values=(
                    id_val,
                    data_val.strftime("%Y-%m-%d"),
                    entra_val.strftime("%H:%M"),
                    entra_almoco_val.strftime("%H:%M"),
                    saida_almoco_val.strftime("%H:%M"),
                    saida_val.strftime("%H:%M"),
                    # e texto melhorado para clareza. Seu original: "✅" if sp == '1' else "❌"
                    "✅ Sim" if sp_val == 1 else "❌ Não" 
                ))
        
        _popular_treeview_interno(tree)
        scrollbar.config(command=tree.yview)
        
        # Lê os dados do arquivo
        

        def editar(id_selected):
            dados_atuais = db_manager.get_horario_id(id_selected)
            if not dados_atuais:
                messagebox.showerror("Erro", "Não foi possível carregar os dados para edição.", parent=banco)
                return
            
            id_db, data_db_str, he_db_str, eal_db_str, sal_db_str, hs_db_str, sp_db_int = dados_atuais
            sp_db_int = int(sp_db_int) if sp_db_int is not None else 0 # Garante que é int

            editar_janela = tk.Toplevel(banco)  # Cria uma nova janela (Toplevel)
            editar_janela.title(f"Editar ID: {id_db} - Data: {data_db_str}")
            editar_janela.geometry("550x250")
            editar_janela.transient(banco)
            editar_janela.grab_set()

            frame_data = tk.Frame(editar_janela)
            frame_data.pack(pady=15, padx=10)

            # Usar frame_data como contêiner para os elementos com grid
            tk.Label(frame_data, text="Hora de Entrada (HH:MM):", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
            entrada_entry_edit = tk.Entry(frame_data, width=10, font=("Arial", 14), justify="center")
            entrada_entry_edit.grid(row=0, column=1, padx=5, pady=5)
            entrada_entry_edit.insert(0, he_db_str)

            # Entrada Almoço
            tk.Label(frame_data, text="Entrada Almoço (HH:MM):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
            e_almoco_entry_edit = tk.Entry(frame_data, width=10, font=("Arial", 14), justify="center")
            e_almoco_entry_edit.grid(row=1, column=1, padx=5, pady=5)
            e_almoco_entry_edit.insert(0, eal_db_str)

            # Saída Almoço
            tk.Label(frame_data, text="Saída Almoço (HH:MM):", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
            s_almoco_entry_edit = tk.Entry(frame_data, width=10, font=("Arial", 14), justify="center")
            s_almoco_entry_edit.grid(row=2, column=1, padx=5, pady=5)
            s_almoco_entry_edit.insert(0, sal_db_str)

            # Hora de Saída
            tk.Label(frame_data, text="Hora de Saída (HH:MM):", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
            saida_entry_edit = tk.Entry(frame_data, width=10, font=("Arial", 14), justify="center")
            saida_entry_edit.grid(row=3, column=1, padx=5, pady=5)
            saida_entry_edit.insert(0, hs_db_str)
            
            # Checkbutton para Semana de Prova
            sprova_edit_var = tk.IntVar(value=sp_db_int)
            tk.Label(frame_data, text="Semana de Prova:", font=("Arial", 12)).grid(row=4, column=0, padx=5, pady=8, sticky="e")
            check_sprova_edit = tk.Checkbutton(frame_data, variable=sprova_edit_var, onvalue=1, offvalue=0)
            check_sprova_edit.grid(row=4, column=1, padx=5, pady=8, sticky="w")


            def enviar_edicao():
                novos_valores = {}
                novo_he_str = entrada_entry_edit.get().strip()
                novo_eal_str = e_almoco_entry_edit.get().strip()
                novo_sal_str = s_almoco_entry_edit.get().strip()
                novo_hs_str = saida_entry_edit.get().strip()
                novo_sp_int = sprova_edit_var.get()

                try:
                    # HORA_ENTRADA
                    if novo_he_str: # Se não estiver vazio
                        datetime.strptime(novo_he_str, "%H:%M") # Valida formato
                        if novo_he_str != he_db_str: # Se mudou
                            novos_valores["HORA_ENTRADA"] = novo_he_str
                    else: # Não pode ser vazio
                        messagebox.showerror("Erro de Validação", "Hora de Entrada não pode ser vazia.", parent=editar_janela)
                        return
                    
                    # ENTRA_ALMOCO
                    if novo_eal_str: # Se não estiver vazio
                        datetime.strptime(novo_eal_str, "%H:%M")
                        if novo_eal_str != eal_db_str:
                            novos_valores["ENTRA_ALMOCO"] = novo_eal_str
                    elif eal_db_str and eal_db_str != "00:00": # Se estava preenchido e foi apagado, define como "00:00"
                        novos_valores["ENTRA_ALMOCO"] = "00:00"
                    
                    # SAIDA_ALMOCO
                    if novo_sal_str:
                        datetime.strptime(novo_sal_str, "%H:%M")
                        if novo_sal_str != sal_db_str:
                            novos_valores["SAIDA_ALMOCO"] = novo_sal_str
                    elif sal_db_str and sal_db_str != "00:00":
                         novos_valores["SAIDA_ALMOCO"] = "00:00"

                    # HORA_SAIDA
                    if novo_hs_str:
                        datetime.strptime(novo_hs_str, "%H:%M")
                        if novo_hs_str != hs_db_str:
                            novos_valores["HORA_SAIDA"] = novo_hs_str
                    else:
                        messagebox.showerror("Erro de Validação", "Hora de Saída não pode ser vazia.", parent=editar_janela)
                        return
                        
                    # SEMANA_PROVA
                    if novo_sp_int != sp_db_int:
                        novos_valores["SEMANA_PROVA"] = novo_sp_int

                except ValueError:
                    messagebox.showerror("Erro de Formato", "Formato de hora inválido. Use HH:MM.", parent=editar_janela)
                    return

                if not novos_valores:
                    messagebox.showinfo("Sem Alterações", "Nenhuma alteração foi detectada.", parent=editar_janela)
                    return 

                # id_db é o ID original do registro sendo editado
                if db_manager.update_horario(id_db, novos_valores):
                    messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!", parent=banco)
                    editar_janela.destroy()
                    _popular_treeview_interno(tree) # Atualiza a treeview
                    calcular_banco() # Recalcula o banco de horas na tela principal
                else:
                    messagebox.showerror("Erro", "Não foi possível atualizar o registro.", parent=editar_janela)

            # Frame para o botão na parte inferior (mantendo sua estrutura)
            frame_botao_edicao = tk.Frame(editar_janela) # Renomeado para clareza
            frame_botao_edicao.pack(side=tk.BOTTOM, pady=10) # pady aumentado
            tk.Button(frame_botao_edicao, text="Salvar Alterações", font=("Arial", 10, "bold"), width=18, command=enviar_edicao).pack()
            
            editar_janela.wait_window()


        def chamar_edicao():
            selected_items_tree = tree.selection() # Nome da variável alterado
            if not selected_items_tree:
                messagebox.showwarning("Atenção", "Selecione uma linha para editar.", parent=banco)
                return
            
            item_iid = selected_items_tree[0]
            values_from_tree = tree.item(item_iid, "values")
            try:
                # O ID é o primeiro valor na tupla 'values' da Treeview
                id_editar = int(values_from_tree[0]) 
                editar(id_editar) # Chama a função 'editar' principal (agora 'editar_selecionado')
            except (IndexError, ValueError):
                messagebox.showerror("Erro", "Não foi possível obter o ID da linha selecionada.", parent=banco)


        def deleta_selecionado(): 
            selected_items_tree = tree.selection()
            if not selected_items_tree:
                messagebox.showwarning("Atenção", "Selecione uma linha para deletar.", parent=banco)
                return

            item_iid = selected_items_tree[0]
            values_from_tree = tree.item(item_iid, "values")
            try:
                id_to_delete = int(values_from_tree[0])
            except (IndexError, ValueError):
                messagebox.showerror("Erro", "Não foi possível obter o ID da linha selecionada.", parent=banco)
                return

            # Add a confirmation dialog
            confirm = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja deletar o registro ID: {id_to_delete}?", parent=banco)
            if not confirm:
                return

            if db_manager.delete_horario(id_to_delete): # Use id_to_delete
                messagebox.showinfo("Sucesso", "Registro deletado com sucesso!", parent=banco)
                _popular_treeview_interno(tree) # Atualiza a treeview
                calcular_banco() # Recalcula o banco de horas na tela principal
            else:
                messagebox.showerror("Erro", "Não foi possível deletar o registro.", parent=banco) # Changed message


        def filtro_data(dt_ini, dt_fim):
            data_ant = dt_ini
            data_prox = dt_fim

            try:
                data_ant_dt = datetime.strptime(data_ant, DATE_FORMAT_DISPLAY)
                data_prox_dt = datetime.strptime(data_prox, DATE_FORMAT_DISPLAY)

                # Converte para string no formato do DB para a consulta
                data_ant_db = data_ant_dt.strftime(DATE_FORMAT_DB)
                data_prox_db = data_prox_dt.strftime(DATE_FORMAT_DB)

            except ValueError:
                messagebox.showerror("Erro de Formato", f"Use o formato {DATE_FORMAT_DISPLAY.replace('%d','dd').replace('%m','mm').replace('%Y','yyyy')}.", parent=banco)
                return

            if data_ant_dt > data_prox_dt:
                messagebox.showerror("Erro", "Data inicial maior que a final.", parent=banco)
                return

            dados_filtrados = db_manager.filtro_horas(data_ant_db, data_prox_db)

            for i in tree.get_children():
                tree.delete(i)

            for row in dados_filtrados:

                data_db_str = row[1]
                data_display = datetime.strptime(data_db_str, DATE_FORMAT_DB).strftime(DATE_FORMAT_DISPLAY)
      
                # Pega o restante dos valores
                id_val, _, entra_val, entra_almoco_val, saida_almoco_val, saida_val, sp_val = row
                
                tree.insert("", tk.END, values=(
                    id_val, data_display, entra_val, entra_almoco_val, saida_almoco_val, saida_val,
                    "✅ Sim" if sp_val == 1 else "❌ Não"
                ))

        
        # Botão Editar na NAV da janela de exibir_banco
        tk.Button(nav, text="Editar", command=chamar_edicao, borderwidth=0, font=("Arial", 10, "bold"), relief=tk.FLAT).pack(side=tk.LEFT, padx=10, pady=5)
        tk.Button(nav, text="Deletar", command=deleta_selecionado, borderwidth=0, font=("Arial", 10, "bold"), relief=tk.FLAT).pack(side=tk.LEFT, padx=10, pady=5)
        def aplicar_filtro(botao):
            ini_label = tk.Label(nav, text="De:", font=("Arial", 10))
            ini_label.pack(side=tk.LEFT, padx=(20, 5))

            data_ini_entry = tk.Entry(nav, width=10, font=("Arial", 10), justify="center")
            data_ini_entry.pack(side=tk.LEFT)

            ate_label = tk.Label(nav, text="Até:", font=("Arial", 10))
            ate_label.pack(side=tk.LEFT, padx=(10, 5))

            data_fim_entry = tk.Entry(nav, width=10, font=("Arial", 10), justify="center")
            data_fim_entry.pack(side=tk.LEFT)
            def send_data():
                if data_ini_entry.get() and data_fim_entry.get():
                    filtro_data(data_ini_entry.get(), data_fim_entry.get())
                    calcular_banco()
                    data_ini_entry.destroy()
                    data_fim_entry.destroy()
                    ini_label.destroy()
                    ate_label.destroy()
                    search_btn.destroy()
                    botao.config(state="normal")

            search_btn = tk.Button(nav, text="✅", command=send_data, font=(10), relief=tk.FLAT)
            search_btn.pack(side=tk.LEFT, padx=10, pady=5)
            botao.config(state="disable")
        
        clicked = tk.Button(nav, text="Filtrar", font=("Arial", 10, "bold"), relief=tk.GROOVE)
        clicked.config(command=lambda: aplicar_filtro(clicked))
        clicked.pack(side=tk.LEFT, padx=10, pady=5)
        banco.wait_window() 
    
    # Botão para adicionar a entrada
    frame_linha3 = tk.Frame(root)
    frame_linha3.pack(pady=(200,0))

    tk.Button(frame_linha3, text="Calcular Banco de Horas", command=calcular_banco).grid(row=0, column=0, padx=10)
    tk.Button(frame_linha3, text="Exibir Banco de Horas", command=exibir_banco).grid(row=0, column=1, padx=10)

    # Rodando a interface gráfica
    root.mainloop()

# Chamada da função que cria a interface gráfica
Banco_horas()
