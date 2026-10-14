from kivy.app import App
from kivy.uix.label import Label
from threading import Thread
import uvicorn
class GersonAIApp(App):
    def build(self):
        def run():
            from server import app
            uvicorn.run(app, host="0.0.0.0", port=8000)
        Thread(target=run, daemon=True).start()
        return Label(text='Gerson AI ON')
GersonAIApp().run()
