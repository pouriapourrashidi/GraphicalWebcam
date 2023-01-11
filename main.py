from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.start_stop.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.start_stop.text = 'Start Camera'
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        currentTime = time.strftime('%Y%m%d-%H%M%S')
        self.fileName = f"files\{currentTime}.png"
        self.ids.camera.export_to_png(self.fileName)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.fileName


class ImageScreen(Screen):
    link_message="Creat Link First"
    def creat_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.fileName
        file_share = FileSharer(filePath=file_path)
        self.link = file_share.share()
        #print(link)
        self.ids.link.text = self.link

    def copyLink(self):
        try:
            Clipboard.copy(self.link)
        except:
            self.ids.link.text =self.link_message

    def openLink(self):
        try:
            webbrowser.open(self.link)
        except:
            self.ids.link.text = self.link_message

    def back(self):
        self.manager.current='camera_screen'
class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
