from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class KilometresConverterApp(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_float_miles()
        result = value * 1.60934
        self.root.ids.output_label.text = "{:.3f}".format(result)

    def handle_increment(self, change):
        value = self.get_float_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_float_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

KilometresConverterApp().run()