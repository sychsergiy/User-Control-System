from .queries import Selecter
from .utils import session_scope


def test_selections():
    with session_scope() as session:
        selecter = Selecter(session)
        print('Social App selecions /--------------')
        selecter.run_socialapp_selections()
        print('\nRoles selecions /--------------')
        selecter.run_roles_selections()
        print('\nPermission selecions /--------------')
        selecter.run_permission_selections()


if __name__ == '__main__':
    test_selections()
