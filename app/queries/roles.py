from app.tables import Role, User, SocialApp


def run_roles_selections(session):
    # select admin_role
    admin_role = session.query(Role).filter_by(title='admin').first()
    print(admin_role)
    # select accessible operation for admin_role
    print(admin_role.permission)
    # select users who are admins
    print(admin_role.users)

    # select user and his role
    users = session.query(User).join(Role) \
        .with_entities(User.first_name, User.last_name, User.phone_number, Role.title).all()
    print(users)

    # select roles at the first socialapp
    app = session.query(SocialApp).first()
    roles = session.query(Role).filter_by(socialapp=app).all()
    print(roles)

    # select socialapp and his roles
    socialapps = session.query(SocialApp).join(Role).with_entities(SocialApp.title, Role.title).all()
    print(socialapps)

    # select socialapp and his roles even if there is no role
    socialapps = session.query(SocialApp).outerjoin(Role).with_entities(SocialApp.title, Role.title).all()
    print(socialapps)
