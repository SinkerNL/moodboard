from nicegui import ui
from moodbutton import MoodButton, MoodStats
from sticky_menu import StickyMenu
import plotly.graph_objs as go

def plot_stats(stats):
    mood_map = {'sad': 0, 'neutral': 1, 'happy': 2}
    mood_emojis = {0: '😫', 1: '🤔', 2: '😊'}
    times = [entry['datetime'] for entry in stats]
    values = [mood_map.get(entry['mood'], None) for entry in stats]
    emojis = [mood_emojis.get(val, '') for val in values]

    return {
        'data': [{
            'type': 'scatter',
            'x': times,
            'y': values,
            'mode': 'text',
            'text': emojis,
            'textposition': 'middle center',
            'textfont': {'size': 24},
            'showlegend': False,
            'marker': {'opacity': 0},
        }],
        'layout': {
            'yaxis': {
                'tickmode': 'array',
                'tickvals': [0, 1, 2, 3],
                'ticktext': ['Sad', 'Neutral', 'Happy', ''],
            },
            'margin': {'l': 50, 'r': 20, 't': 50, 'b': 40},  # more left and top margin
            'autosize': True,
            'height': 400,  # increased height
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
        },
        'config': {
            'displayModeBar': False
        }
    }

@ui.page('/')
async def index():
    with ui.row().classes('w-full flex justify-center items-center gap-4'):
        MoodButton('😊').props('flat size="xl"').style('color: #FF0080')
        MoodButton('🤔').props('flat size="xl"').style('color: #FF0080')
        MoodButton('😫').props('flat size="xl"').style('color: #FF0080')
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

# dark_mode=True 

# on_air=True, 
