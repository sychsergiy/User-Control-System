from app.tables import PermissionsPack, Operation

from .insert_command import InsertCommand


class InsertPermissionsPackCommand(InsertCommand):
    def execute(self):
        perm_pack = PermissionsPack(title='Test Permissions Pack')

        operations_for_moderator = self.session.query(Operation).filter(
            Operation.title == 'post' or Operation.title == 'view'
        ).all()
        for operation in operations_for_moderator:
            perm_pack.permission.append(operation)

        self.session.add(perm_pack)
