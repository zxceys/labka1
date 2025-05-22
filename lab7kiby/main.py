from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from room import Room
from apartment import Apartment
from building import Building

class Interface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        self.inputs = {}
        fields = [
            ('Длина', 'length'),
            ('Ширина', 'width'),
            ('Комнат', 'rooms'),
            ('Этажей', 'floors'),
            ('Квартир на этаже', 'flats')
        ]

        for label, key in fields:
            box = BoxLayout(size_hint_y=None, height=30)
            box.add_widget(Label(text=label, size_hint_x=0.5))
            self.inputs[key] = TextInput(multiline=False)
            box.add_widget(self.inputs[key])
            self.add_widget(box)

        self.result = Label(text='')
        self.add_widget(self.result)

        self.add_widget(Button(text="Комната", on_press=self.calculate_room))
        self.add_widget(Button(text="Квартира", on_press=self.calculate_apartment))
        self.add_widget(Button(text="Дом", on_press=self.calculate_building))

    def calculate_room(self, instance):
        try:
            r = Room(float(self.inputs['length'].text), float(self.inputs['width'].text))
            self.result.text = f"Комната площадью {r.area} м²\nМощность: {r.heating_power()} ккал/ч"
        except Exception as e:
            self.result.text = f"Ошибка: {e}"

    def calculate_apartment(self, instance):
        try:
            a = Apartment(float(self.inputs['length'].text), float(self.inputs['width'].text), int(self.inputs['rooms'].text))
            self.result.text = f"Квартира с {a.rooms} комнатами, площадью {a.area} м²\nМощность: {a.heating_power()} ккал/ч"
        except Exception as e:
            self.result.text = f"Ошибка: {e}"

    def calculate_building(self, instance):
        try:
            b = Building(
                float(self.inputs['length'].text),
                float(self.inputs['width'].text),
                int(self.inputs['rooms'].text),
                int(self.inputs['floors'].text),
                int(self.inputs['flats'].text)
            )
            self.result.text = f"{b}\nМощность: {b.heating_power()} ккал/ч"
        except Exception as e:
            self.result.text = f"Ошибка: {e}"

class SpaceApp(App):
    def build(self):
        return Interface()

if __name__ == '__main__':
    SpaceApp().run()
