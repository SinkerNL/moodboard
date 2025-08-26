from nicegui import ui, context

class StickyMenu:
    def __init__(self):
        with ui.page_sticky(x_offset=18, y_offset=18):
            with ui.button(icon='settings').props('flat color=accent'):
                with ui.menu() as menu:
                    current_route = context.client.page.path
                    if current_route == '/':
                        ui.menu_item('Stats', lambda: ui.navigate.to('/stats'))
                    elif current_route == '/stats':
                        ui.menu_item('Home', lambda: ui.navigate.to('/'))
                    ui.separator()
                    ui.menu_item('Close', menu.close)