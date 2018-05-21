from app.tables import Role, User, SocialApp

from .insert_command import InsertCommand


class InsertRolesCommand(InsertCommand):
    def execute(self):
        socialapp = self.session.query(SocialApp).first()

        admin_role = Role(title='admin', socialapp=socialapp, )
        moderator_role = Role(title='moderator', socialapp=socialapp, )
        user_role = Role(title='user', socialapp=socialapp, )

        admin = User(
            first_name='test1', last_name='user1', phone_number='+380965440904', profile_picture='link',
            role=admin_role,
        )
        moderator = User(
            first_name='test2', last_name='user2', phone_number='+380965440904', profile_picture='link',
            role=moderator_role,
        )
        user = User(
            first_name='test3', last_name='user3', phone_number='+380965440904', profile_picture='link',
            role=user_role,
        )

        self.session.add_all([admin_role, moderator_role, user_role])
        self.session.add_all([admin, moderator, user])
