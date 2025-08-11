import pyvisual as pv
from PySide6.QtCore import QTimer

def create_page_1_ui(window, ui):
    ui_page = {}
    ui_page["nav_horarios"] = pv.PvRectangle(container=window, x=-3, y=-4, width=740,
        height=48, idle_color=(60, 60, 58, 1), border_color=None, border_thickness=0,
        corner_radius=0, border_style="solid", opacity=1, is_visible=True)
    
    ui_page["scroll_area"] = pv.PvScroll(
        container=window, x=18, y=70, width=661, height=406
    )
    ui_page["scroll_area"].background_color = (75, 73, 75, 1)
    ui_page["scroll_area"].corner_radius = 18
    ui_page["scroll_area"].opacity = 0.75

    #ui_page["scroll_area"].add_widget(container)

    ui_page["Text_1"] = pv.PvText(container=window, x=50, y=13, width=45,
        height=15, idle_color=(194, 155, 215, 0), text='Editar', is_visible=True,
        text_alignment='left', font='assets/fonts/Lexend/Lexend.ttf', font_size=15,
        font_color=(255, 255, 255, 1))

    ui_page["Icon_2"] = pv.PvIcon(container=window, x=7, y=10, width=21,
        height=21, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/6b3cdb5a6f.svg',
        is_visible=True, opacity=1)

    ui_page["Text_3"] = pv.PvText(container=window, x=119, y=13, width=56,
        height=14, idle_color=(194, 155, 215, 0), text='Deletar', is_visible=True,
        text_alignment='left', font='assets/fonts/Lexend/Lexend.ttf', font_size=15,
        font_color=(255, 255, 255, 1))

    ui_page["Text_4"] = pv.PvText(container=window, x=192, y=12, width=45,
        height=15, idle_color=(194, 155, 215, 0), text='Filtrar', is_visible=True,
        text_alignment='left', font='assets/fonts/Lexend/Lexend.ttf', font_size=15,
        font_color=(255, 255, 255, 1))

    ui_page["horarios_area"] = pv.PvRectangle(container=window, x=18, y=70, width=661,
        height=406, idle_color=(75, 73, 75, 1), corner_radius=18, opacity=0.75, is_visible=True)

    ui_page["Button_6"] = pv.PvButton(container=window, x=296, y=442, width=105,
        height=21, text='Pronto', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), idle_color=(50, 50, 50, 1),
        border_color=(100, 100, 100, 1), border_thickness=0,
        corner_radius=25, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1),
        is_visible=True, opacity=1, on_click=lambda el: ui["pages"].set_current_page(0))

    # Cabeçalhos das colunas
    ui_page["Text_9"] = pv.PvText(container=window, x=96, y=83, width=17,
        height=17, idle_color=(144, 80, 178, 0), text='ID', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1))

    ui_page["Text_10"] = pv.PvText(container=window, x=171, y=83, width=42,
        height=17, idle_color=(144, 80, 178, 0), text='Data', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1))

    ui_page["Text_11"] = pv.PvText(container=window, x=253, y=83, width=56,
        height=16, idle_color=(144, 80, 178, 0), text='Entrada', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1))

    ui_page["Text_12"] = pv.PvText(container=window, x=342, y=83, width=75,
        height=17, idle_color=(144, 80, 178, 0), text='Ida Almoço', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1))

    ui_page["Text_13"] = pv.PvText(container=window, x=442, y=83, width=77,
        height=17, idle_color=(144, 80, 178, 0), text='Almoço Fim', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1))

    ui_page["Text_14"] = pv.PvText(container=window, x=567, y=82, width=40,
        height=18, idle_color=(144, 80, 178, 0), text='Saída', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1))

    # Linhas verticais separadoras
    ui_page["Rectangle_20"] = pv.PvRectangle(container=window, x=146, y=76, width=2,
        height=30, idle_color=(75, 73, 75, 1), corner_radius=10, opacity=1, is_visible=True)
    ui_page["Rectangle_21"] = pv.PvRectangle(container=window, x=232, y=76, width=2,
        height=30, idle_color=(75, 73, 75, 1), corner_radius=10, opacity=1, is_visible=True)
    ui_page["Rectangle_22"] = pv.PvRectangle(container=window, x=327, y=76, width=2,
        height=30, idle_color=(75, 73, 75, 1), corner_radius=10, opacity=1, is_visible=True)
    ui_page["Rectangle_23"] = pv.PvRectangle(container=window, x=428, y=76, width=2,
        height=30, idle_color=(75, 73, 75, 1), corner_radius=10, opacity=1, is_visible=True)
    ui_page["Rectangle_24"] = pv.PvRectangle(container=window, x=531, y=76, width=3,
        height=30, idle_color=(75, 73, 75, 1), corner_radius=10, opacity=1, is_visible=True)

    return ui_page

def render_lista(ui_page_1, container, horarios_lista):
    # Coleta as chaves dos widgets antigos
    keys_to_remove = [key for key in ui_page_1 if key.startswith("row_") or key.startswith("row_container_")]
    widgets_to_delete = [ui_page_1[key] for key in keys_to_remove]


     # Oculta e agenda a deleção dos widgets
    def delete_and_remove(key, widget):
        widget.delete()
        if key in ui_page_1:
            del ui_page_1[key]


    for key, widget in zip(keys_to_remove, widgets_to_delete):
        widget.setVisible(False)
        QTimer.singleShot(200, lambda k=key, w=widget: delete_and_remove(k, w))

    MAX_ITEMS = 9  # Limite de itens a serem exibidos

    # Cria os novos widgets para cada item na lista
    for i, horario in enumerate(horarios_lista[:MAX_ITEMS]):
        y_base = 116 + i * 40

        # Container para a linha
        row_container = pv.PvRectangle(
            container=ui_page_1["scroll_area"], x=40, y=y_base, width=618,
            height=31, idle_color=(75, 73, 75, 1), corner_radius=8, is_visible=True
        )
        ui_page_1[f"row_container_{i}"] = row_container

        campos = {
            'id': (62, str(horario['id'])),
            'data': (149, horario["data"]),
            'entrada': (236, horario["entrada"]),
            'entra_almoco': (329, horario["entra_almoco"]),
            'saida_almoco': (430, horario["saida_almoco"]),
            'saida': (539, horario["saida"])
        }

        for j, (key, (x, texto)) in enumerate(campos.items()):
            input_widget = pv.PvTextInput(
                container=row_container, x=x-40, y=2, width=85, height=27,
            default_text="", background_color=(0,0,0,0),
                font_color=(255, 255, 255, 1), text_alignment='center',
                border_hover_color=None, border_thickness=0, is_visible=True
            )
            setattr(input_widget, 'text', str(texto))
            ui_page_1[f"row_{i}_col_{j}"] = input_widget

        

    # Torna todos os campos da lista somente leitura
    # Define os campos como somente leitura
    for i in range(min(len(horarios_lista), MAX_ITEMS)):
        for j in range(6):
            widget = ui_page_1.get(f"row_{i}_col_{j}")
            if widget:
                widget.setEnabled(False)

