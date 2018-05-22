from app.tables import PermissionsPack, Operation, SocialApp

from .insert_command import InsertCommand


class InsertPermissionsPackCommand(InsertCommand):
    def execute(self):
        socialapp = self.session.query(SocialApp).first()
        perm_pack = PermissionsPack(title='Test Permissions Pack', socialapp=socialapp)

        operations_for_moderator = self.session.query(Operation).filter(
            Operation.title == 'post' or Operation.title == 'view'
        ).all()
        for operation in operations_for_moderator:
            perm_pack.permission.append(operation)

        self.session.add(perm_pack)
