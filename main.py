from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
import random

class SlayerAdBlocker(App):
    def build(self):
        self.root = BoxLayout(orientation="vertical", padding=30, spacing=20)
        with self.root.canvas.before:
            Color(0.1, 0.1, 0.1, 1) 
            self.rect = RoundedRectangle(size=self.root.size, pos=self.root.pos)
        self.root.bind(size=self._update_rect, pos=self._update_rect)

        self.title = Label(text="[b][color=00FF7F]SLAYER AD-BLOCKER[/color][/b]", markup=True, font_size="30sp")
        self.stats = Label(text="Starting Engine...", font_size="18sp", markup=True)

        self.root.add_widget(self.title)
        self.root.add_widget(self.stats)

        self.blocked = 0
        Clock.schedule_interval(self.tick, 0.5)
        return self.root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def tick(self, dt):
        self.blocked += random.randint(1, 3)
        self.stats.text = f"🚫 [b]Ads Blocked:[/b] {self.blocked}\n\n🌐 [b]Status:[/b] [color=00ff00]Active[/color]"

if __name__ == "__main__":
    SlayerAdBlocker().run()
