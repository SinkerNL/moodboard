from nicegui import ui
from moodbutton import MoodButton, MoodStats
from sticky_menu import StickyMenu
from plot import plot_stats

@ui.page('/')
async def index():
    with ui.column().classes('w-full h-screen justify-center items-center gap-8'):
        ui.label('What is your mood today?') \
            .classes('mx-auto text-6xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-purple-500 text-center mb-8')

        with ui.row().classes('w-full flex justify-center items-center gap-4'):
            MoodButton('😊').props('flat').classes('text-7xl').style('color: #FF0080')
            MoodButton('🤔').props('flat').classes('text-7xl').style('color: #FF0080')
            MoodButton('😫').props('flat').classes('text-7xl').style('color: #FF0080')
    StickyMenu()

@ui.page('/stats')
async def stats_page():
    stats = MoodStats().all()
    if stats:
        ui.plotly(plot_stats(stats)).classes('w-full')
    else:
        ui.label('No stats yet.')
    StickyMenu()

ui.run(title='Mood Board')
