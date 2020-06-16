
class InitializationError(Exception):

    def __init__(self, message):
        self.message = message


class StateMachine:
    def __init__(self):
        self.handler = {}
        self.currentState = None
        self.startState = None

    def set_start(self, name):
        self.startState = name.upper()
        self.currentState = self.startState

    def add_state(self, name, handler):
        name = name.upper()
        self.handler[name] = handler

    def get_state(self):
        return self.currentState

    def get_default(self):
        return self.startState

    def run(self, cargo, protocol = 'L'):
        try:
            handler = self.handler[self.currentState]
        except:
            raise InitializationError("Not Initialized -- use add_state() and set_start() before run()")

        newState = handler(cargo, protocol)
        if newState == 'errorState':
            self.currentState = self.startState
            return 'An error occured --Resetting to Default'

        self.currentState = newState.upper()


