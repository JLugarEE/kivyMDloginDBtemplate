from kivymd.app import MDApp
from screens.firebaseloginscreen import FirebaseLoginScreen
#from screens.firebaseloginscreen.FirebaseLoginScreen import FirebaseLoginScreen
#from screens.firebaseloginscreen.FirebaseLoginScreen import FirebaseLoginScreen
from screens.welcomescreen import WelcomeScreen
from screens.signinscreen import SignInScreen
from screens.createaccountscreen import CreateAccountScreen
from kivy.app import App
from kivy import utils
from kivy.lang import Builder
from kivy.factory import Factory
import certifi

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
from screens.send import SendScreen
from screens.receive import ReceiveScreen
from screens.mainscreen import MainScreen


class MainApp(MDApp):
    # Kivy has a naming convention where if your class that inherits from App
    # (or MDApp) has a name of FooApp, it will automatically try to load foo.kv
    # as the app's root widget.

    # In this case, that means we can remove your build function, and instead
    # put the ScreenManager as the root widget in your main.kv (since your class
    # is named MainApp. This is a little cleaner than using the build function
    # in my opinion.
    pass


if __name__ == '__main__':
    MainApp().run()
