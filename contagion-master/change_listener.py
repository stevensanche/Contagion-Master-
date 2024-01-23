"""Simple listener notes when any state change
has occurred.
"""

import mvc
import model

import logging
logging.basicConfig()
log = logging.getLogger("__name__")


class ChangeListener(mvc.Listener):
    """Detect changes in the population"""

    def __init__(self):
        self.changes = False

    def set(self, changes: bool):
        self.changes = changes

    def check(self) -> bool:
        return self.changes

    def notify(self, subject: mvc.Listenable, event: str):
        """A statechange event sets 'changes' to True"""
        assert isinstance(subject, model.Individual)  # because argument type is too general
        if event == "newstate":
            self.changes = True
            log.debug("State change")
        else:
            log.warning(f"ChangeListener does not handle event type '{event}'")
