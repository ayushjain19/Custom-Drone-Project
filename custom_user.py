from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.settings import SettingsWithSidebar
import json


Builder.load_string("""
<WelcomeScreen>:
    FloatLayout:
        Label:
            font_size: 35
            text: 'Welcome to XYZ!'
            size_hint: (.26, .10)
            pos: (300, 380)

        Label:
            font_size: 35
            text: 'Plug in the drone to your PC.'
            size_hint: (.26, .10)
            pos: (300, 280)

        Button:
            text: 'Click to configure your drone'
            font_size: 20
            size_hint: (.33, .10)
            pos: (280, 180)
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'sensors_page'
            

<SensorsScreen>:
    FloatLayout:
        Label:
            text: 'Select the sensors you connected externally.'
            size_hint: (.26, .10)
            font_size: 30
            pos: (280, 510)
    GridLayout:
        cols: 2
        padding: [100,100,100,100]
        row_default_height: 30
        Label:
            text: 'Sensor 1'
            size_hint_x:None
            font_size: 15
            width:30
        CheckBox:
            size_hint_x:None    
            width:30
            on_active: root.ping('sensor1')

        Label:
            text: 'Sensor 2'
            width:30
        CheckBox:         
            width:30
            on_active: root.ping('sensor2')

        Label:
            text: 'Sensor 3'
            width:30
        CheckBox:       
            width:30
            on_active: root.ping('sensor3')

        Label:
            text: 'Sensor 4'
            width:30
        CheckBox:        
            width:30
            on_active: root.ping('sensor4')
    FloatLayout:
        Button:
            font_size: 20
            text: 'Next >>'
            size_hint: (.26, .07)
            pos: (200, 80)
            on_press:
                root.manager.current = 'usage_page'

        Button:
            font_size: 20
            text: '<< Back'
            size_hint: (.17, .07)
            pos: (450, 80) 
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'welcome_page'

<UsageScreen>:
    FloatLayout:
        Label:
            text: 'We would love to know your purpose of usage'
            size_hint: (.26, .10)
            font_size: '27sp'
            pos: (280, 510)
    
    BoxLayout:
        orientation: "vertical"
        padding: [45, 150, 45, 60]
        
        BoxLayout:
            padding: [0,0,0,15]
            BoxLayout:
                padding: [15,0,15,0]
                Button:
                    font_size: 30
                    text: "Agriculture"
                    on_release: app.open_settings()
                        
                    
            BoxLayout:
                padding: [15,0,15,0]
                Button:
                    font_size: 20
                    text: "Pipeline Inspection"
                    on_release: app.open_settings()
                    
            BoxLayout:
                padding: [15,0,15,0]
                Button:
                    font_size: 17
                    text: "Electrical Line Inspection"
                    on_release: app.open_settings()
                    
                    

        BoxLayout:
            padding: [0,15,0,0]
            BoxLayout:
                padding: [15,0,15,0]
                Button:
                    font_size: 30
                    text: "Border Patrol"
                    on_release: app.open_settings()
                    
                    
            BoxLayout:
                padding: [15,0,15,0]
                Button:
                    font_size: 17
                    text: "Wind Turbines Inspection"
                    on_release: app.open_settings()
                    
                    
            BoxLayout:
                padding: [15,0,15,0]
                Button:
                    font_size: 20
                    text: "Aerial Photography"
                    on_release: app.open_settings()
                    

    FloatLayout:
        Label:
            text: 'When you are done with the configurations, click on '
            size_hint: (.26, .10)
            font_size: '20sp'
            pos: (250, 2)

        Button:
            font_size: 20
            text: 'Next >>'
            size_hint: (.12, .05)
            pos: (580, 15)
            on_press:
                root.manager.current = 'final_page'

<FinalScreen>:
    FloatLayout:
        Label:
            font_size: 26
            text: 'Congratulations! You are done with the configurations of your drone.'
            size_hint: (.26, .10)
            pos: (300, 380)

        Label:
            font_size: 35
            text: 'Happy Flying!'
            size_hint: (.26, .10)
            pos: (300, 280)

        Button:
            font_size: 20
            text: 'Exit'
            size_hint: (.07, .05)
            pos: (611, 20)
            on_press: app.stop()

        Label:
            text: 'THE APP'
            size_hint: (.26, .10)
            font_size: '20sp'
            pos: (610, 7)

""")

agriculture_data = json.dumps([
    {'type': 'title',
    'title': 'Agriculture Settings'},
    {'type': 'numeric',
    'title': 'Height above crops',
    'desc': '(in metres)',
    'section': 'agriculture_section',
    'key': 'height'},
    {'type': 'options',
    'title': 'Spray Intensity',
    'desc': 'Note: Spray time decreases for higher intensity',
    'options': ['Low', 'Medium', 'High'],
    'section': 'agriculture_section',
    'key': 'spray'},
    {'type': 'numeric',
    'title': 'Maximum Height for drone',
    'desc': '(in metres)',
    'section': 'agriculture_section',
    'key': 'max_height'},
    {'type': 'options',
    'title': 'Initial Payload Weight',
    'desc': 'Give approximation (in kilograms)',
    'options': ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5'],
    'section': 'agriculture_section',
    'key': 'payload'}
    ])


pipeline_data = json.dumps([
    {'type': 'title',
    'title': 'Pipeline Inspection Settings'},
    {'type': 'numeric',
    'title': 'Height above pipelines',
    'desc': '(in metres)',
    'section': 'pipeline_section',
    'key': 'height'},
    {'type': 'options',
    'title': 'Camera attached to the drone',
    'options': ['Camera A', 'Camera B', 'Camera C', 'Camera D', 'Camera E'],
    'section': 'pipeline_section',
    'key': 'camera'},
    {'type': 'numeric',
    'title': 'Maximum Height for drone',
    'desc': '(in metres)',
    'section': 'pipeline_section',
    'key': 'max_height'},
    ])


electrical_data = json.dumps([
    {'type': 'title',
    'title': 'Electrical Line Inspection Settings'},
    {'type': 'numeric',
    'title': 'Approximate height of operation',
    'desc': '(in metres)',
    'section': 'electrical_section',
    'key': 'height'},
    {'type': 'numeric',
    'title': 'Maximum Height for drone',
    'desc': '(in metres)',
    'section': 'electrical_section',
    'key': 'max_height'},
    {'type': 'options',
    'title': 'Camera attached to the drone',
    'options': ['Camera A', 'Camera B', 'Camera C', 'Camera D'],
    'section': 'electrical_section',
    'key': 'camera'}
    ])


border_patrol_data = json.dumps([
    {'type': 'title',
    'title': 'Border Patrol Settings'},
    {'type': 'numeric',
    'title': 'Approximate Height of operation',
    'desc': '(in metres)',
    'section': 'border_patrol_section',
    'key': 'height'},
    {'type': 'bool',
    'title': 'Transmission from the drone',
    'section': 'border_patrol_section',
    'key': 'transmission'},
    {'type': 'numeric',
    'title': 'Maximum Height for drone',
    'desc': '(in metres)',
    'section': 'border_patrol_section',
    'key': 'max_height'},
    {'type': 'options',
    'title': 'Payload Weight',
    'desc': 'Give approximation (in kilograms)',
    'options': ['0', '0.25', '0.5', '0.75', '1', '1.25', '1.5'],
    'section': 'border_patrol_section',
    'key': 'payload'}
    ])

wind_turbine_data = json.dumps([
    {'type': 'title',
    'title': 'Wind Turbine Inspection Settings'},
    {'type': 'numeric',
    'title': 'Approximate height of operation',
    'desc': '(in metres)',
    'section': 'wind_turbine_section',
    'key': 'height'},
    {'type': 'options',
    'title': 'Camera attached to the drone',
    'options': ['Camera A', 'Camera B', 'Camera C', 'Camera D', 'Camera E'],
    'section': 'wind_turbine_section',
    'key': 'camera'},
    {'type': 'numeric',
    'title': 'Maximum Height for drone',
    'desc': '(in metres)',
    'section': 'wind_turbine_section',
    'key': 'max_height'},
    ])

photography_data = json.dumps([
    {'type': 'title',
    'title': 'Aerial Photography Settings'},
    {'type': 'options',
    'title': 'Manual/Pre-plan My Shot',
    'options': ['Manual flight', 'Plan the Shot'],
    'section': 'aerial_photography_section',
    'key': 'plan'},
    {'type': 'options',
    'title': 'Camera attached to the drone',
    'options': ['Camera A', 'Camera B', 'Camera C', 'Camera D', 'Camera E'],
    'section': 'aerial_photography_section',
    'key': 'camera'},
    {'type': 'numeric',
    'title': 'Maximum Height for drone',
    'desc': '(in metres)',
    'section': 'aerial_photography_section',
    'key': 'max_height'},
    ])

advanced_settings_data = json.dumps([
    {'type': 'title',
    'title': 'Advanced Settings'},
    {'type': 'options',
    'title': 'Maximum Speed',
    'desc': '(in m/s)',
    'options': ['2', '2.5', '3', '3.5', '4'],
    'section': 'advanced_settings_section',
    'key': 'speed'},
    {'type': 'options',
    'title': 'Maximum Ascend Rate',
    'desc': '(in m/s)',
    'options': ['0.5', '1', '1.5', '2', '2.5', '3'],
    'section': 'advanced_settings_section',
    'key': 'ascend'},
    {'type': 'options',
    'title': 'Maximum Descend Rate',
    'desc': '(in m/s)',
    'options': ['0.5', '1', '1.5', '2', '2.5', '3'],
    'section': 'advanced_settings_section',
    'key': 'descend'},
    {'type': 'bool',
    'title': 'Activate/Deactivate Return to launch on communication loss',
    'desc': 'When activated, RTL will be triggerd after 15 seconds of communication loss',
    'section': 'advanced_settings_section',
    'key': 'rtl'},
    {'type': 'numeric',
    'title': 'Maximum Range (in metres)',
    'desc': 'Do not exceed 500 metres',
    'section': 'advanced_settings_section',
    'key': 'range'},
    {'type': 'options',
    'title': 'Vehicle Handling',
    'options': ['Smooth', 'Acrobatic', 'Sharp'],
    'section': 'advanced_settings_section',
    'key': 'handling'},
    ])

class WelcomeScreen(Screen):
    pass

class SensorsScreen(Screen):
    def __init__(self, **kw):
        super(SensorsScreen, self).__init__(**kw)
        self.sensors_name = {'sensor1':'False','sensor2':'False','sensor3':'False','sensor4':'False'}

    def ping(self, n):
        if self.sensors_name[n] == 'False':
            self.sensors_name[n] = 'True'
        else:
            self.sensors_name[n] = 'False'

class UsageScreen(Screen):
    pass

class FinalScreen(Screen):
    pass



# Create the screen manager
sm = ScreenManager(transition = FadeTransition())
sensors_screen = SensorsScreen(name = 'sensors_page')
welcome_screen = WelcomeScreen(name = 'welcome_page')
usage_screen = UsageScreen(name = 'usage_page')
final_screen = FinalScreen(name = 'final_page')

sm.add_widget(welcome_screen)
sm.add_widget(sensors_screen)
sm.add_widget(usage_screen)
sm.add_widget(final_screen)


class TestApp(App):
    
    use_kivy_settings = False

    def build(self):
        self.settings_cls = SettingsWithSidebar
        return sm

    def build_config(self, config):
        config.setdefaults('agriculture_section', {
            'height': 1,
            'spray': 'Medium',
            'max_height': 10,
            'payload': 0.5
            })

        config.setdefaults('pipeline_section', {
            'height': 5,
            'camera': 'Camera A',
            'max_height': 20,
            })

        config.setdefaults('electrical_section', {
            'height': 10,
            'max_height': 70,
            'camera': 'Camera A',
            })

        config.setdefaults('border_patrol_section', {
            'height': 1,
            'transmission': 'False',
            'max_height': 10,
            'payload': 0.5
            })

        config.setdefaults('wind_turbine_section', {
            'height': 15,
            'camera': 'Camera A',
            'max_height': 10,
            })

        config.setdefaults('aerial_photography_section', {
            'plan': 'Manual',
            'camera': 'Camera A',
            'max_height': 30,
            })

        config.setdefaults('advanced_settings_section', {
            'speed': '3',
            'ascend': '1',
            'descend': '1',
            'rtl': 'True',
            'range': 100,
            'handling': 'Smooth'
            })

    def build_settings(self, settings):
        settings.add_json_panel('Agriculture',
                                self.config,
                                data = agriculture_data)

        settings.add_json_panel('Pipeline',
                                self.config,
                                data = pipeline_data)

        settings.add_json_panel('Electrical Lines',
                                self.config,
                                data = electrical_data)

        settings.add_json_panel('Border Patrol',
                                self.config,
                                data = border_patrol_data)

        settings.add_json_panel('Wind Turbine',
                                self.config,
                                data = wind_turbine_data)

        settings.add_json_panel('Aerial Photography',
                                self.config,
                                data = photography_data)

        settings.add_json_panel('Advanced Settings',
                                self.config,
                                data = advanced_settings_data)


if __name__ == '__main__':
    TestApp().run()

