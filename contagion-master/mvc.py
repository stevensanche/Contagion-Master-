"""Generic Model-View-Controller mechanics
 (abstract base classes) for
attaching view components to model components and
communicating events to view components.
"""

from typing import List

# Event listeners are in the View component
class Listener:
    def notify(self, subject: "Listenable", event: str):
        raise NotImplementedError("The 'notify' method must be defined in concrete classes")

# Model components should be listenable

class Listenable:
    """Model components should be listenable, and should notify
    listeners of significant state changes.
    """

    def __init__(self):
        self._listeners: List[Listener] = []

    def add_listener(self, listener: Listener):
        self._listeners.append(listener)

    def notify_all(self, event: str):
        for listener in self._listeners:
            listener.notify(self, event)