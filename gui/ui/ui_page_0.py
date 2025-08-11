import pyvisual as pv
from PySide6.QtCore import QTimer 

def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["Rectangle_0"] = pv.PvRectangle(container=window, x=-2, y=-13, width=736,
        height=48, idle_color=(60, 60, 58, 1), border_color=None, border_thickness=0,
        corner_radius=0, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Icon_1"] = pv.PvIcon(container=window, x=7, y=8, width=21,
        height=21, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/6b3cdb5a6f.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["Rectangle_2"] = pv.PvRectangle(container=window, x=140, y=101, width=427,
        height=297, idle_color=(75, 73, 75, 1), border_color=None, border_thickness=0,
        corner_radius=18, border_style="solid", opacity=0.75, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_3"] = pv.PvText(container=window, x=262, y=10, width=174,
        height=17, idle_color=(194, 155, 215, 0), text='Banco de Horas', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=22,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["DayMonth"] = pv.PvTextInput(container=window, x=562, y=10, width=67,
        height=16, background_color=(255, 255, 255, 1), is_visible=True, placeholder='dd/mm',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=3, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["entrada"] = pv.PvTextInput(container=window, x=225, y=209, width=105,
        height=34, background_color=(255, 255, 255, 1), is_visible=True, placeholder='00:00',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Lexend/Lexend.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=4, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["year"] = pv.PvTextInput(container=window, x=634, y=10, width=53,
        height=16, background_color=(255, 255, 255, 1), is_visible=True, placeholder='yyyy',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=3, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["saida"] = pv.PvTextInput(container=window, x=382, y=209, width=105,
        height=34, background_color=(255, 255, 255, 1), is_visible=True, placeholder='00:00',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=4, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["entra_almoco"] = pv.PvTextInput(container=window, x=223, y=285, width=105,
        height=34, background_color=(255, 255, 255, 1), is_visible=True, placeholder='00:00',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=4, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["saida_almoco"] = pv.PvTextInput(container=window, x=382, y=286, width=105,
        height=34, background_color=(255, 255, 255, 1), is_visible=True, placeholder='00:00',
        text_alignment='center', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=4, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["save"] = pv.PvFileDialog(container=window, x=344, y=348, width=20,
        height=20, text='', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(240, 241, 240, 0), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=15, border_style="solid", box_shadow=None, box_shadow_hover=None,
        icon_path='assets/icons/127f1610bb.svg', icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=0.7, paddings=(0, 0, 0, 0), enable_drag_drop=False,
        dialog_mode="save", files_filter="All Files (*.*)", is_visible=True, is_disabled=False,
        opacity=1, on_hover=None, on_click=None, on_release=None,
        tag=None)

    ui_page["title_hora_entrada"] = pv.PvText(container=window, x=237, y=175, width=80,
        height=27, idle_color=(194, 155, 215, 0), text='Hora Entrada', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["title_hora_saida"] = pv.PvText(container=window, x=401, y=175, width=67,
        height=27, idle_color=(194, 155, 215, 0), text='Hora Saída', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["title_entra_almoco"] = pv.PvText(container=window, x=227, y=254, width=100,
        height=24, idle_color=(194, 155, 215, 0), text='Entrada Almoço', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["title_sai_almoco"] = pv.PvText(container=window, x=393, y=255, width=82,
        height=23, idle_color=(194, 155, 215, 0), text='Saída Almoço', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=12,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["editar"] = pv.PvIcon(container=window, x=162, y=118, width=18,
        height=18, idle_color=(255, 251, 251, 1), preserve_original_colors=False, icon_path='assets/icons/641a91f4d5.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=lambda el: (
            setattr(el, 'idle_color', (200, 200, 200, 1)),
        ),
        on_click=lambda el: (
           setattr(el, 'idle_color', (200, 200, 200, 1)),
           QTimer.singleShot(200, lambda: ui["pages"].set_current_page(1))
           ), 
        box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)', 
        on_release=lambda el: setattr(el, 'idle_color', (255, 251, 251, 1)), 
        is_visible=True,
        opacity=1, tag=None)


    ui_page["saldo"] = pv.PvTextInput(container=window, x=316, y=136, width=85,
        height=32, background_color=(255, 255, 255, 0), is_visible=True, placeholder='00:00',
        text_alignment='right', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Lexend/Lexend.ttf',
        font_size=16, font_color=(245, 242, 242, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        is_disabled=True,
        text_type='Text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='')
    
    if hasattr(ui_page["saldo"], '_q_widget') and hasattr(ui_page["saldo"]._q_widget, 'setReadOnly'):
        ui_page["saldo"]._q_widget.setReadOnly(True)

    ui_page["title_compensar"] = pv.PvText(container=window, x=468, y=346, width=89,
        height=12, idle_color=(194, 155, 215, 0), text='Horas a Compensar', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=9,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["title_semana_prova"] = pv.PvText(container=window, x=468, y=368, width=89,
        height=12, idle_color=(194, 155, 215, 0), text='Semana de Prova', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=9,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Circle_1"] = pv.PvCircle(container=window, x=28, y=454, width=26,
        height=26, idle_color=(50, 50, 50, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", on_hover=None, on_click=None, on_release=None,
        opacity=1, is_visible=True, tag=None)

    ui_page["Circle_2"] = pv.PvCircle(container=window, x=64, y=455, width=23,
        height=23, idle_color=(60, 60, 58, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", on_hover=None, on_click=None, on_release=None,
        opacity=1, is_visible=True, tag=None)

    ui_page["Circle_3"] = pv.PvCircle(container=window, x=98, y=456, width=22,
        height=22, idle_color=(75, 73, 75, 1), border_color=(0, 0, 0, 1), border_thickness=0,
        border_style="solid", on_hover=None, on_click=None, on_release=None,
        opacity=1, is_visible=True, tag=None)

    ui_page["compensar_horas"] = pv.PvCheckbox(container=window, x=446, y=338, width=26,
        height=30, text='', is_checked=False, checked_color=(0, 0, 255, 1),
        unchecked_color=(255, 255, 255, 1), checkmark_color=(255, 255, 255, 1), checkmark_size=10, checkbox_size=12,
        corner_radius=4, checkmark_type='✓', border_color=(0, 0, 0, 1), border_thickness=0,
        spacing=10, font='assets/fonts/Poppins/Poppins.ttf', font_size=12, font_color=(0, 0, 0, 1),
        bold=False, italic=False, underline=False, strikeout=False,
        paddings=(5, 0, 0, 0), is_visible=True, opacity=1, tag=None,
        on_change=None)

    ui_page["semana_prova"] = pv.PvCheckbox(container=window, x=446, y=359, width=26,
        height=30, text='', is_checked=False, checked_color=(0, 0, 255, 1),
        unchecked_color=(255, 255, 255, 1), checkmark_color=(255, 255, 255, 1), checkmark_size=10, checkbox_size=12,
        corner_radius=4, checkmark_type='✓', border_color=(0, 0, 0, 1), border_thickness=0,
        spacing=10, font='assets/fonts/Poppins/Poppins.ttf', font_size=12, font_color=(0, 0, 0, 1),
        bold=False, italic=False, underline=False, strikeout=False,
        paddings=(5, 0, 0, 0), is_visible=True, opacity=1, tag=None,
        on_change=None)

    return ui_page
