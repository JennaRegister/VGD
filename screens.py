class ScreenManager(object):
    """The screen 'manager' is the access point from your main game to your many screens. The manager keeps a dictionary
    of name->screen, and knows which one is currently "active". Each screen should, in turn, know about its manager so
    that from within the screen itself, it can call "self.manager.activate('someotherscreen')".

    Usage (where MenuScreen and GameScreen are subclasses of BaseScreen)

    mgr = ScreenManager()
    the_menu = MenuScreen()
    the_game = GameScreen()

    # OPTION 1
    the_menu.set_manager(mgr)
    the_game.set_manager(mgr)
    # OPTION 2

    mgr.activate("Menu")



    """

    def __init__(self):
        self.screens = {}
        self.active = None

    def add(self, name, screen_obj):
        self.screens[name] = screen_obj
        if screen_obj.manager is not self:
            screen_obj.manager = self

    def activate(self, name):
        sc = self.screens.get(name)
        if sc is not None:
            self.deactivate()
            self.active = sc
            self.active.on_activate()
        else:
            print("WARNING: no screen called '%s'" % name)

    def deactivate(self):
        if self.active is not None:
            self.active.on_deactivate()
            self.active = None

    def draw(self, surface):
        if self.active is not None:
            self.active.draw(surface)

    def handle_input(self, evt):
        if self.active is not None:
            self.active.handle_input(evt)

    def update(self):
        if self.active is not None:
            self.active.update()

class BaseScreen(object):
    def __init__(self, name, manager=None):
        self.name = name
        if manager:
            self.set_manager(manager, name)

    def set_manager(self, manager):
        self.manager = manager
        self.manager.add(self.name, self)

    def on_activate(self):
        raise NotImplementedError("%s has not yet implemented on_activate()" % self.__class__.__name__)

    def on_deactivate(self):
        raise NotImplementedError("%s has not yet implemented on_deactivate()" % self.__class__.__name__)

    def update(self):
        raise NotImplementedError("%s has not yet implemented update()" % self.__class__.__name__)

    def draw(self, surface):
        raise NotImplementedError("%s has not yet implemented draw()" % self.__class__.__name__)

    def handle_input(self, event):
        raise NotImplementedError("%s has not yet implemented handle_input()" % self.__class__.__name__)