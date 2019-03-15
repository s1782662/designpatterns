
import abc

class ThemeFactory:

    def createdarktheme(self):
        return DarkTheme()


    def createlighttheme(self):
        return LightTheme()


class Theme(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def createToolbar(self):
        pass

    @abc.abstractmethod
    def createDialog(self):
        pass


    @abc.abstractmethod
    def setup(self):
        pass


class DarkTheme(Theme):

    def createToolbar(self):
        return DarkToolBar()

    def createDialog(self):
        return DarkDialog()

    def setup(self):
        print(self.createToolbar().toolbar())
        print(self.createDialog().dialog())

class LightTheme(Theme):

    def createToolbar(self):
        return LightToolBar()

    def createDialog(self):
        return LightDialog()

    def setup(self):
        print(self.createToolbar().toolbar())
        print(self.createDialog().dialog())


class ToolBar(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def toolbar(self):
        pass

class DarkToolBar(ToolBar):

    def toolbar(self):
        return 'Hey I am dark toolbar !!!'

class LightToolBar(ToolBar):

    def toolbar(self):
        return 'Hey I am white toolbar !!!'



class Dialog(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def dialog(self):
        pass

class DarkDialog(Dialog):

    def dialog(self):
        return 'Hey I am a Dark Dialog'

class LightDialog(Dialog):

    def dialog(self):
        return 'Hey I am a White Dialog'



if __name__== '__main__':
    theme = ThemeFactory()
    dark = theme.createdarktheme()
    dark.setup()
