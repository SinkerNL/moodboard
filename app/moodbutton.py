from nicegui import ui
import json
from pathlib import Path
from datetime import datetime

class MoodStats:
    def __init__(self, filename='stats.json'):
        self.filepath = Path(__file__).parent / filename
        self.entries = []
        if self.filepath.exists():
            self.load()
        else:
            self.save()

    def load(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                self.entries = data
            else:
                # Convert old dict format to list
                self.entries = []
                for mood, count in data.items():
                    for _ in range(count):
                        self.entries.append({
                            "datetime": "unknown",
                            "mood": mood
                        })

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.entries, f)

    def add_entry(self, mood):
        entry = {
            "datetime": datetime.now().isoformat(timespec='seconds'),
            "mood": mood
        }
        self.entries.append(entry)
        self.save()

    def all(self):
        return self.entries

class MoodButton(ui.button):
    def __init__(self, *args, stats: MoodStats = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if args[0] == '😊':
            self.mood = 'happy'
        elif args[0] == '🤔':
            self.mood = 'neutral'
        elif args[0] == '😫':
            self.mood = 'sad'
        else:
            self.mood = 'unknown'

        self.stats = stats or MoodStats()
        self.on('click', self.handle_click)

    def handle_click(self) -> None:
        ui.notify(f'You clicked the {self.mood} button!')
        if self.mood in ['happy', 'neutral', 'sad']:
            self.stats.add_entry(self.mood)
        self.update()

