from settings import *

class Timer:
    def __init__(self, duration, func = None, repeat = None, autostart = False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.func = func
        self.repeat = repeat
        self.activate() if autostart else None

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def start(self):
        while True:
            if pygame.time.get_ticks() - self.start_time >= self.duration:
                if self.func and self.start_time != 0:
                    self.func()
                    if self.repeat:
                        self.activate()
                        continue
                self.deactivate()
            break

    def update(self):
        self.start()
