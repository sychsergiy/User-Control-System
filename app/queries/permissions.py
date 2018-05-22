from app.tables import Role, User, Operation, role_permission, Object, user_extra_permission


def select_permissions(session):
    # select permissions for each role
    permissions = session.query(Role).join(role_permission).join(Operation).join(Object) \
        .with_entities(Role.title, Operation.title, Object.title).all()
    print(permissions)

    user = session.query(User).first()
    # user extra permissions
    print(user.permission)
    # user role permissions
    print(user.role.permission)

    # select all user permissions
    role_permissions = session.query(User).filter_by(id=user.id).join(Role).join(role_permission).join(Operation).join(
        Object).with_entities(User.first_name, Operation.title, Object.title)
    extra_permissions = session.query(User).filter_by(id=user.id).join(user_extra_permission).join(Operation).join(
        Object).with_entities(User.first_name, Operation.title, Object.title)
    print(role_permissions.all())
    print(extra_permissions.all())
    print(role_permissions.union(extra_permissions).all())

    # select object operations
    object_ = session.query(Object).first()
    print(object_.operations)
