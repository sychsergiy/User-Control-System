from .applications import run_socialapp_selections
from .permissions import run_permission_selections
from .roles import run_roles_selections


class Selecter(object):
    def __init__(self, session):
        self.session = session

    def run_roles_selections(self):
        run_roles_selections(self.session)

    def run_permission_selections(self):
        run_permission_selections(self.session)

    def run_socialapp_selections(self):
        run_socialapp_selections(self.session)
