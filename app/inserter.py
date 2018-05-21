from .insertions import (
    InsertSocialappsCommand, InsertObjectsCommand, InsertPermissionsPackCommand, InsertRolesCommand,
    InsertPermissionsCommand
)

from .utils import session_scope


class Inserter(object):
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()


def fill_the_database_with_test_date():
    with session_scope() as session:
        inserter = Inserter()
        inserter.add(InsertSocialappsCommand(session))
        inserter.add(InsertObjectsCommand(session))
        inserter.add(InsertRolesCommand(session))
        inserter.add(InsertPermissionsCommand(session))
        inserter.add(InsertPermissionsPackCommand(session))
        inserter.run()


if __name__ == '__main__':
    fill_the_database_with_test_date()
