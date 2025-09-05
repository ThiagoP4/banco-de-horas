import pyvisual as pv


def create_page_2_ui(window,ui):
    """
    Create and return UI elements for Page 2.
    :param container: The page widget for Page 2.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["nav_user"] = pv.PvRectangle(container=window, x=-4, y=0, width=736,
        height=44, idle_color=(39, 39, 39, 1), border_color=None, border_thickness=0,
        corner_radius=0, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["user_area"] = pv.PvRectangle(container=window, x=113, y=73, width=445,
        height=406, idle_color=(51, 48, 48, 1), border_color=None, border_thickness=0,
        corner_radius=18, border_style="solid", opacity=0.75, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_2"] = pv.PvText(container=window, x=218, y=10, width=264,
        height=25, idle_color=(194, 155, 215, 0), text='Informações de Usuário', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=22,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["menu_btn"] = pv.PvIcon(container=window, x=13, y=12, width=21,
        height=21, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/6b3cdb5a6f.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["Text_4"] = pv.PvText(container=window, x=145, y=276, width=73,
        height=27, idle_color=(194, 155, 215, 0), text='Carga Horária', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=10,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_5"] = pv.PvText(container=window, x=277, y=276, width=73,
        height=27, idle_color=(194, 155, 215, 0), text='', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=10,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["return"] = pv.PvIcon(container=window, x=129, y=87, width=18,
        height=18, idle_color=(255, 255, 255, 1), preserve_original_colors=False, icon_path='assets/icons/41bff9c3d6.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=lambda el: ui["pages"].set_current_page(0), on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["Text_7"] = pv.PvText(container=window, x=147, y=189, width=73,
        height=27, idle_color=(194, 155, 215, 0), text='Email', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["user_label"] = pv.PvText(container=window, x=148, y=129, width=73,
        height=27, idle_color=(194, 155, 215, 0), text='Usuário', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=14,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_9"] = pv.PvText(container=window, x=256, y=276, width=27,
        height=27, idle_color=(194, 155, 215, 0), text='Perfil', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Lexend/Lexend.ttf', font_size=10,
        font_color=(255, 255, 255, 1), bold=False, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["user_value"] = pv.PvTextInput(container=window, x=147, y=156, width=363,
        height=27, background_color=(255, 255, 255, 1), is_visible=True, placeholder='',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(116, 116, 116, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=5, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='')

    ui_page["email_value"] = pv.PvTextInput(container=window, x=147, y=216, width=363,
        height=27, background_color=(255, 255, 255, 1), is_visible=True, placeholder='',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(116, 116, 116, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=5, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='')

    ui_page["CH_value"] = pv.PvTextInput(container=window, x=147, y=303, width=70,
        height=27, background_color=(255, 255, 255, 1), is_visible=True, placeholder='',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(116, 116, 116, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=5, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='')

    ui_page["perfil_value"] = pv.PvTextInput(container=window, x=256, y=303, width=128,
        height=27, background_color=(255, 255, 255, 1), is_visible=True, placeholder='',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(116, 116, 116, 1), border_color=(196, 196, 196, 1), border_thickness=1,
        border_style="solid", corner_radius=5, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag='')

    return ui_page
