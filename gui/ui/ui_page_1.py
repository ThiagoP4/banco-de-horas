import pyvisual as pv
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QHeaderView
from PySide6.QtCore import Qt

def create_page_1_ui(window, ui):
    ui_page = {}

    # -- Widgets do topo (sem alterações) --
    ui_page["nav_horarios"] = pv.PvRectangle(
        container=window, x=-3, y=-4, width=740, height=48,
        idle_color=(60, 60, 58, 1), border_color=None, border_thickness=0,
        corner_radius=0, border_style="solid", opacity=1, is_visible=True
    )
    ui_page["Text_1"] = pv.PvText(
        container=window, x=50, y=13, width=45, height=15, idle_color=(194, 155, 215, 0),
        text='Editar', is_visible=True, text_alignment='left',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=15, font_color=(255, 255, 255, 1)
    )
    ui_page["Icon_2"] = pv.PvIcon(
        container=window, x=7, y=10, width=21, height=21, idle_color=(255, 255, 255, 1),
        preserve_original_colors=False, icon_path='assets/icons/6b3cdb5a6f.svg',
        is_visible=True, opacity=1
    )
    ui_page["Text_3"] = pv.PvText(
        container=window, x=119, y=13, width=56, height=14, idle_color=(194, 155, 215, 0),
        text='Deletar', is_visible=True, text_alignment='left',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=15, font_color=(255, 255, 255, 1)
    )
    ui_page["Text_4"] = pv.PvText(
        container=window, x=192, y=12, width=45, height=15, idle_color=(194, 155, 215, 0),
        text='Filtrar', is_visible=True, text_alignment='left',
        font='assets/fonts/Lexend/Lexend.ttf', font_size=15, font_color=(255, 255, 255, 1)
    )

    # REMOVIDO: O retângulo de fundo e a área de scroll do PyVisual foram removidos
    # para evitar conflitos de renderização. O estilo será aplicado diretamente na tabela.
    # ui_page["scroll_area"] = ...
    # ui_page["horarios_area"] = ...

    ui_page["Button_6"] = pv.PvButton(
        container=window, x=296, y=442, width=105, height=21,
        text='Pronto', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), idle_color=(50, 50, 50, 1),
        border_color=(100, 100, 100, 1), border_thickness=0,
        corner_radius=25, border_style="solid",
        box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1),
        is_visible=True, opacity=1, on_click=lambda el: ui["pages"].set_current_page(0)
    )

    # -- Cabeçalhos visuais e divisórias (sem alterações) --
    ui_page["Text_9"] = pv.PvText(
        container=window, x=96, y=83, width=17, height=17,
        idle_color=(144, 80, 178, 0), text='ID', is_visible=True,
        text_alignment='left', font='assets/fonts/Poppins/Poppins.ttf', font_size=13,
        font_color=(255, 255, 255, 1)
    )
    # ... (outros PvText para os cabeçalhos) ...
    ui_page["Text_10"] = pv.PvText(container=window, x=171, y=83, width=42, height=17, text='Data', font='assets/fonts/Poppins/Poppins.ttf', font_size=13, font_color=(255, 255, 255, 1))
    ui_page["Text_11"] = pv.PvText(container=window, x=253, y=83, width=56, height=16, text='Entrada', font='assets/fonts/Poppins/Poppins.ttf', font_size=13, font_color=(255, 255, 255, 1))
    ui_page["Text_12"] = pv.PvText(container=window, x=342, y=83, width=75, height=17, text='Ida Almoço', font='assets/fonts/Poppins/Poppins.ttf', font_size=13, font_color=(255, 255, 255, 1))
    ui_page["Text_13"] = pv.PvText(container=window, x=442, y=83, width=77, height=17, text='Almoço Fim', font='assets/fonts/Poppins/Poppins.ttf', font_size=13, font_color=(255, 255, 255, 1))
    ui_page["Text_14"] = pv.PvText(container=window, x=567, y=82, width=40, height=18, text='Saída', font='assets/fonts/Poppins/Poppins.ttf', font_size=13, font_color=(255, 255, 255, 1))
    # ... (retângulos divisórios) ...
    ui_page["Rectangle_20"] = pv.PvRectangle(container=window, x=146, y=76, width=2, height=30, idle_color=(75, 73, 75, 1), corner_radius=10)
    ui_page["Rectangle_21"] = pv.PvRectangle(container=window, x=232, y=76, width=2, height=30, idle_color=(75, 73, 75, 1), corner_radius=10)
    ui_page["Rectangle_22"] = pv.PvRectangle(container=window, x=327, y=76, width=2, height=30, idle_color=(75, 73, 75, 1), corner_radius=10)
    ui_page["Rectangle_23"] = pv.PvRectangle(container=window, x=428, y=76, width=2, height=30, idle_color=(75, 73, 75, 1), corner_radius=10)
    ui_page["Rectangle_24"] = pv.PvRectangle(container=window, x=531, y=76, width=3, height=30, idle_color=(75, 73, 75, 1), corner_radius=10)
    
    # MODIFICADO: Container da tabela posicionado para ocupar toda a área desejada.
    # A altura foi ajustada para não sobrepor o botão "Pronto".
    horarios_container_qt = QWidget(window)
    horarios_container_qt.setGeometry(18, 70, 661, 360) # Posição e tamanho da área visual original
    horarios_container_qt.setStyleSheet("background: transparent;") # O container em si é transparente
    layout = QVBoxLayout(horarios_container_qt)
    # Margens ajustadas para o conteúdo da tabela começar abaixo dos cabeçalhos de texto
    layout.setContentsMargins(0, 40, 0, 0) # 40px de margem no topo

    table = QTableWidget(0, 6, horarios_container_qt)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setVisible(False)
    table.setShowGrid(False)
    table.setEditTriggers(QTableWidget.NoEditTriggers)
    table.setSelectionMode(QTableWidget.ExtendedSelection) 
    table.setSelectionBehavior(QTableWidget.SelectRows)  
    table.setFocusPolicy(Qt.NoFocus)

    # ADICIONADO: Estilo completo aplicado diretamente na tabela.
    # Isso inclui o fundo semi-transparente, bordas arredondadas e estilo para a barra de rolagem.
    table.setStyleSheet("""
        QTableWidget {
            background-color: rgba(75, 73, 75, 0.75); /* Cor e opacidade do PvRectangle */
            color: #ffffff;
            border-radius: 18px; /* Raio da borda do PvRectangle */
            font-size: 13px;
            border: none; /* Remove qualquer borda padrão */
        }
        QTableWidget::item {
            border-bottom: 1px solid #555;
            padding-left: 10px; /* Adiciona um espaçamento interno */
        }
        QTableWidget::item:selected {
             background-color: rgba(144, 80, 178, 0.5); /* Cor de seleção suave */
        }
        
        /* Estilização da Barra de Rolagem */
        QScrollBar:vertical {
            border: none;
            background: #404040;
            width: 10px;
            margin: 18px 0 18px 0; /* Margem para não tocar o topo/fundo arredondado */
            border-radius: 5px;
        }
        QScrollBar::handle:vertical {
            background: #888;
            min-height: 20px;
            border-radius: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
    """)

    # ADICIONADO: Configuração do tamanho das colunas para se ajustarem ao conteúdo e ao espaço.
    header = table.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.ResizeToContents) # ID
    header.setSectionResizeMode(1, QHeaderView.ResizeToContents) # Data
    header.setSectionResizeMode(2, QHeaderView.Stretch)          # Entrada
    header.setSectionResizeMode(3, QHeaderView.Stretch)          # Ida Almoço
    header.setSectionResizeMode(4, QHeaderView.Stretch)          # Almoço Fim
    header.setSectionResizeMode(5, QHeaderView.Stretch)          # Saída
    
    layout.addWidget(table)
    horarios_container_qt.show()

    ui_page["horarios_container_qt"] = horarios_container_qt
    ui_page["table"] = table

    return ui_page


def render_lista(ui_page_1, container, horarios_lista):
    """
    Popula a QTableWidget com os dados de uma lista de horários.

    Args:
        ui_page_1 (dict): O dicionário da UI contendo a referência da tabela.
        container (QWidget): O container da janela principal (não utilizado nesta função, mas mantido por consistência).
        horarios_lista (list): Uma lista de dicionários, onde cada dicionário representa uma linha.
    """
    # Pega a referência da tabela a partir do dicionário da UI
    table = ui_page_1["table"]
    
    # Limpa a tabela completamente antes de adicionar novos dados
    table.setRowCount(0)

    # Itera sobre a lista de horários e adiciona cada um como uma nova linha na tabela
    for row_number, horario in enumerate(horarios_lista):
        table.insertRow(row_number)
        
        # Cria os QTableWidgetItem para cada coluna, convertendo os dados para string
        id_item = QTableWidgetItem(str(horario.get("id", "")))
        data_item = QTableWidgetItem(horario.get("data", ""))
        entrada_item = QTableWidgetItem(horario.get("entrada", ""))
        ida_almoco_item = QTableWidgetItem(horario.get("entra_almoco", ""))
        volta_almoco_item = QTableWidgetItem(horario.get("saida_almoco", ""))
        saida_item = QTableWidgetItem(horario.get("saida", ""))

        # Centraliza o texto em todas as células para um melhor alinhamento visual
        for item in [id_item, data_item, entrada_item, ida_almoco_item, volta_almoco_item, saida_item]:
            item.setTextAlignment(Qt.AlignCenter)
        
        # Insere os itens na tabela na linha e coluna corretas
        table.setItem(row_number, 0, id_item)
        table.setItem(row_number, 1, data_item)
        table.setItem(row_number, 2, entrada_item)
        table.setItem(row_number, 3, ida_almoco_item)
        table.setItem(row_number, 4, volta_almoco_item)
        table.setItem(row_number, 5, saida_item)