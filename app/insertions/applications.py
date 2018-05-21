from app.tables import SocialApp, Admin


def insert_socialapps_and_admins(session):
    socialapp1 = SocialApp(title='Test application1', client_id='943178168', secret_key='943178168')
    socialapp2 = SocialApp(title='Test application2', client_id='431785874', secret_key='410252482')

    admin1 = Admin(first_name='admin1', last_name='test', is_superuser=True)
    admin2 = Admin(first_name='admin2', last_name='test', )
    admin3 = Admin(first_name='admin2', last_name='test', )

    socialapp1.admin.append(admin1)
    socialapp1.admin.append(admin2)

    socialapp2.admin.append(admin2)
    socialapp2.admin.append(admin3)

    session.add_all([admin1, admin2, admin3])
    session.add_all([socialapp1, socialapp2])
