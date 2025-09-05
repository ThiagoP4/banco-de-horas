# app.py
# Banco de Horas - Aplicação Principal
# Este arquivo contém a lógica principal da aplicação, incluindo a criação da interface do usuário e o gerenciamento de eventos.
import pyvisual as pv
from gui.ui.ui import create_ui
from db_manager import DatabaseManager 
from calculadora_horas import calcular_horas, ler_arquivo 
from datetime import datetime
from PySide6.QtWidgets import QDialog, QFormLayout, QLineEdit, QDialogButtonBox, QCheckBox, QVBoxLayout

# ==================================================
# ================ 1. LOGIC CODE ====================
# ===================================================

db_manager = DatabaseManager()

# Variáveis de estado para a UI PyVisual
current_data_dm = datetime.now().strftime("%d/%m")
current_ano_yyyy = datetime.now().strftime("%Y")


compensar_horas_checked = False
semana_prova_checked = False


def update_saldo_display(ui_elements):
    global current_saldo_text
    _, _, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova = ler_arquivo(db_manager)

    saldo = calcular_horas(hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova)
    current_saldo_text = f"{saldo}"
    text_widget = ui_elements["page_0"]["saldo"]

    if "saldo" in ui_elements["page_0"]:
        setattr(text_widget, 'text', current_saldo_text)
        text_widget.update()
        text_widget.setDisabled(True)
    else:
        print("[Aviso] saldo não encontrado na page_0")


def register_horario(ui_elements):
    daymonth = ui_elements["page_0"]["DayMonth"].text
    dana_ano = ui_elements["page_0"]["year"].text
    entrada = ui_elements["page_0"]["entrada"].text
    entra_almoco = ui_elements["page_0"]["entra_almoco"].text
    saida_almoco = ui_elements["page_0"]["saida_almoco"].text
    saida = ui_elements["page_0"]["saida"].text

    global semana_prova_checked
    semana_prova = 1 if semana_prova_checked else 0

    data = f"{daymonth + '/' + dana_ano}"

    try:
        data_disp = datetime.strptime(data, "%d/%m/%Y")
        data_db = data_disp.strftime("%Y-%m-%d")
    except ValueError:
        print("Erro: Formato de data inválido. Use dd/mm/yyyy.") 
        return
    
    try:
        datetime.strptime(entrada, "%H:%M")
        datetime.strptime(entra_almoco, "%H:%M")
        datetime.strptime(saida_almoco, "%H:%M")
        datetime.strptime(saida, "%H:%M")
    except ValueError:
        print("Erro: Formato de hora inválido. Use HH:MM.") # Use pv.PvMessageBox aqui
        return

    horarios_existentes = db_manager.get_all_horarios()
    data_banco = [h[1] for h in horarios_existentes]

    if data_db in data_banco:
        pv.MessageBox.error("Erro: Dia já cadastrado.") 
        return

    if db_manager.insert_horario(data_db, entrada, entra_almoco, saida_almoco, saida, semana_prova):
        print("Sucesso", "Horário adicionado com sucesso!")
        setattr(ui_elements["page_0"]["DayMonth"], 'text', datetime.now().strftime("%d/%m"))
        setattr(ui_elements["page_0"]["year"], 'text', datetime.now().strftime("%Y"))
        setattr(ui_elements["page_0"]["entrada"], 'text', '')
        setattr(ui_elements["page_0"]["entra_almoco"], 'text', '')
        setattr(ui_elements["page_0"]["saida_almoco"], 'text', '')
        setattr(ui_elements["page_0"]["saida"], 'text', '')
        semana_prova_checked = False
        update_saldo_display(ui_elements)
    else:
        pv.PvMessageBox(ui_elements["window"], "Erro", "Não foi possível adicionar o horário.").show()


def ler_horarios():
    horarios = db_manager.get_all_horarios()
    if not horarios:
        print("Nenhum horário encontrado.")
        return []

    horarios_lista = []
    for horario in horarios:
        id, data, entrada, entra_almoco, saida_almoco, saida, semana_prova = horario
        data_formatada = datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
        horarios_lista.append({
            "id": id,
            "data": data_formatada,
            "entrada": entrada,
            "entra_almoco": entra_almoco,
            "saida_almoco": saida_almoco,
            "saida": saida,
            "semana_prova": bool(semana_prova)
        })

    return horarios_lista

def show_edit_dialog(horario_data):
    dialog = QDialog()
    dialog.setWindowTitle(f"Editar Horário - {horario_data['data']}")
    dialog.setStyleSheet("background-color: #2b2b2b; color: #ffffff;")

    layout = QFormLayout(dialog)
    layout.setRowWrapPolicy(QFormLayout.WrapAllRows)

    entrada_edit = QLineEdit(horario_data["entrada"])
    entra_almoco_edit = QLineEdit(horario_data["entra_almoco"])
    saida_almoco_edit = QLineEdit(horario_data["saida_almoco"])
    saida_edit = QLineEdit(horario_data["saida"])
    semana_prova_check = QCheckBox()
    semana_prova_check.setChecked(horario_data["semana_prova"])

    layout.addRow("Entrada", entrada_edit)
    layout.addRow("Entra almoco", entra_almoco_edit)
    layout.addRow("Saida almoco", saida_almoco_edit)
    layout.addRow("Saida", saida_edit)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)
    
    main_layout = QVBoxLayout()
    main_layout.addLayout(layout)
    main_layout.addWidget(button_box)
    dialog.setLayout(main_layout)

    # Exibe o diálogo e retorna os novos dados se o usuário clicar em "OK"
    if dialog.exec() == QDialog.Accepted:
        return {
            "entrada": entrada_edit.text(),
            "entra_almoco": entra_almoco_edit.text(),
            "saida_almoco": saida_almoco_edit.text(),
            "saida": saida_edit.text(),
            "semana_prova": 1 if semana_prova_check.isChecked() else 0,
        }
    return None # Retorna None se o usuário cancelar

def editar(id_horario, novos_dados):
    horario_original = db_manager.get_horario_id(id_horario)
    if not horario_original:
        pv.MessageBox.error("Erro", f"Horário com ID {id_horario} não encontrado.").show()
        return
    
    entrada, entra_almoco, saida_almoco, saida, semana_prova = horario_original
    novos_valores = {}

    try:
        # Validação e verificação de mudanças para cada campo
        novo_he = novos_dados.get("entrada")
        if not novo_he:
            pv.MessageBox.warning("Aviso", "O campo 'Entrada' não pode ser vazio.").show()
            return
        datetime.strptime(novo_he, "%H:%M")
        if novo_he != entrada:
            novos_valores["HORA_ENTRADA"] = novo_he

        novo_eal = novos_dados.get("entra_almoco") or "00:00"
        datetime.strptime(novo_eal, "%H:%M")
        if novo_eal != entra_almoco:
            novos_valores["ENTRA_ALMOCO"] = novo_eal

        novo_sal = novos_dados.get("saida_almoco") or "00:00"
        datetime.strptime(novo_sal, "%H:%M")
        if novo_sal != saida_almoco:
            novos_valores["SAIDA_ALMOCO"] = novo_sal

        novo_hs = novos_dados.get("saida")
        if not novo_hs:
            pv.MessageBox.warning("Aviso", "O campo 'Saída' não pode ser vazio.").show()
            return
        datetime.strptime(novo_hs, "%H:%M")
        if novo_hs != saida:
            novos_valores["HORA_SAIDA"] = novo_hs

        novo_sp = novos_dados.get("semana_prova")
        if novo_sp != semana_prova:
            novos_valores["SEMANA_PROVA"] = novo_sp

    except ValueError:
        pv.MessageBox.error("Erro de Formato", "Formato de hora inválido. Use HH:MM.").show()
        return

    if not novos_valores:
        print("Nenhuma alteração detectada.")
        return 

    # id_db é o ID original do registro sendo editado
    if db_manager.update_horario(id_horario, novos_valores):
        pv.MessageBox.info("Sucesso", "Horário atualizado com sucesso!").show()
    else:
        pv.MessageBox.error("Erro", "Não foi possível atualizar o horário no banco de dados.").show()




# ===================================================
# ============== 2. EVENT BINDINGS ==================
# ===================================================

def attach_events(ui):
    global compensar_horas_checked, semana_prova_checked

    if "save" in ui["page_0"]:
        ui["page_0"]["save"].on_click = lambda el: register_horario(ui)

    def on_compensar_change(is_checked):
        global compensar_horas_checked
        compensar_horas_checked = is_checked

        text_inputs = [
            ui["page_0"]["entrada"],
            ui["page_0"]["entra_almoco"],
            ui["page_0"]["saida_almoco"],
            ui["page_0"]["saida"]
        ]
        for input_el in text_inputs:
            input_el.setDisabled(is_checked)
            setattr(input_el, 'text', '00:00' if compensar_horas_checked else '')

    if "compensar_horas" in ui["page_0"]:
        ui["page_0"]["compensar_horas"].on_change = on_compensar_change

    def on_semana_prova_change(is_checked):
        global semana_prova_checked
        semana_prova_checked = is_checked

    if "semana_prova" in ui["page_0"]:
        ui["page_0"]["semana_prova"].on_change = on_semana_prova_change

    def listar_horarios():
        horarios = ler_horarios()
        if not horarios:
            pv.MessageBox.info("Informação", "Nenhum horário cadastrado.").show()
            return
        ui["pages"].set_current_page(1)
        ui["render_lista_func"](
            ui["page_1"],           # Dicionário para armazenar widgets dinâmicos
            ui["page_1_widget"],    # O widget container da página 1
            horarios                # Os dados a serem exibidos
        )

    if "editar" in ui["page_0"]:
        ui["page_0"]["editar"].on_click = lambda el: listar_horarios()

    
    def chamar_edicao():
        table = ui["page_1"]["table"]
        # Usa currentRow() para obter o índice da linha selecionada
        selected_row = table.currentRow() 

        if selected_row < 0: # Se nenhuma linha estiver selecionada, o valor é -1
            pv.MessageBox.warning("Aviso", "Por favor, selecione um horário na tabela para editar.").show()
            return

        # Pega o ID do item na primeira coluna (coluna 0) da linha selecionada
        id_horario = int(table.item(selected_row, 0).text())
        
        # Busca a lista completa para obter todos os dados do item selecionado
        horarios_lista_completa = ler_horarios()
        horario_original_dict = next((h for h in horarios_lista_completa if h["id"] == id_horario), None)

        if not horario_original_dict:
            pv.MessageBox.error("Erro", "Não foi possível encontrar os dados originais do horário.").show()
            return

        # Abre o diálogo de edição com os dados do horário
        novos_dados = show_edit_dialog(horario_original_dict)

        # Se o usuário confirmou a edição (não cancelou)
        if novos_dados:
            editar(id_horario, novos_dados) # Chama a função de edição com os novos dados
            listar_horarios() # Atualiza a tabela para exibir as mudanças
            update_saldo_display(ui) # Atualiza o saldo geral

    # Corrigido: o widget de texto 'Editar' chama a função de edição
    if "editar_nav" in ui["page_1"]:
        # Assumindo que o PvText suporta 'on_click' ou um evento similar
        ui["page_1"]["editar_nav"].on_click = lambda el: chamar_edicao()

        
# ===================================================
# ============== 3. MAIN FUNCTION ==================
# ===================================================


def main():
    app = pv.PvApp()
    ui = create_ui()
    attach_events(ui)

    if "DayMonth" in ui["page_0"]:
        setattr(ui["page_0"]["DayMonth"], 'text', datetime.now().strftime("%d/%m"))
    if "year" in ui["page_0"]:
        setattr(ui["page_0"]["year"], 'text', datetime.now().strftime("%Y"))
    
    update_saldo_display(ui)
    ui["window"].show()
    
    app.run()


if __name__ == '__main__':
    main()
