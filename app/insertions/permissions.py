from app.tables import Role, User, Operation

from .insert_command import InsertCommand


class InsertPermissionsCommand(InsertCommand):
    def execute(self):
        admin_role = self.session.query(Role).filter(Role.title == 'admin').first()
        moderator_role = self.session.query(Role).filter(Role.title == 'moderator').first()
        user_role = self.session.query(Role).filter(Role.title == 'user').first()

        admin = self.session.query(User).filter(User.role == admin_role).first()
        moderator = self.session.query(User).filter(User.role == moderator_role).first()

        # add permission to create and update to admin_role
        operations_for_admin = self.session.query(Operation).filter(
            Operation.title == 'create' or Operation.title == 'update'
        ).all()

        for operation in operations_for_admin:
            admin_role.permission.append(operation)

        # add permission to post and view to moderator_role
        operations_for_moderator = self.session.query(Operation).filter(
            Operation.title == 'post' or Operation.title == 'view'
        ).all()
        for operation in operations_for_moderator:
            moderator_role.permission.append(operation)

        # add permission to view to user_role
        operations_for_user = self.session.query(Operation).filter(Operation.title == 'view').all()
        for operation in operations_for_user:
            user_role.permission.append(operation)

        # add extra permission to admin and moderator
        admin_extra_perm = self.session.query(Operation).filter(Operation.title == 'extra_permission1').first()
        moderator_extra_perm = self.session.query(Operation).filter(Operation.title == 'extra_permission2').first()

        admin.permission.append(admin_extra_perm)
        moderator.permission.append(moderator_extra_perm)

        # add changed to self.session
        self.session.add_all([admin, moderator, admin_role, moderator_role, user_role])
