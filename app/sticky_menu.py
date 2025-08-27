from nicegui import ui

class StickyMenu:
    def __init__(self):
        with ui.page_sticky(x_offset=25, y_offset=25):
            btn = ui.button(icon='settings').props('outline round').classes('shadow-lg')
            with ui.menu() \
                .props(' transition-show="jump-down" transition-hide="jump-up"') \
                .style('width:14rem') \
                .classes("bg-base-200 rounded-box") as menu:

                # MENU ITEMS
                ui.menu_item('Home', on_click=lambda: ui.navigate.to('/'))
                ui.menu_item('Stats', on_click=lambda: ui.navigate.to('/stats'))

            # link button and menu explicitly
            btn.on('click', lambda: menu.open())

            # Force pre‑mount: open once immediately, then close
            ui.timer(0.05, lambda: (menu.open(), ui.timer(0.05, lambda: menu.close(), once=True)), once=True)
