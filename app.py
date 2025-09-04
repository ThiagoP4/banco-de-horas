# app.py
# Banco de Horas - Aplicação Principal
# Este arquivo contém a lógica principal da aplicação, incluindo a criação da interface do usuário e o gerenciamento de eventos.
import pyvisual as pv
from gui.ui.ui import create_ui
from db_manager import DatabaseManager 
from calculadora_horas import calcular_horas, ler_arquivo 
from datetime import datetime

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
