from abc import ABC,abstractmethod
class Button(ABC):
    @abstractmethod
    def render(self):
        pass
class WindowsButton(Button):
    def render(self):
        print("rendering window button")
class LinuxButton(Button):
    def render(self):
        print("rendering linux button")
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
class LinuxFactory(UIFactory):
    def create_button(self):
        return LinuxButton()
def create_ui(factory: UIFactory):
    button = factory.create_button()
    button.render()
create_ui(WindowsFactory())
create_ui(LinuxFactory())
    
