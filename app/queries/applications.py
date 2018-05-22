from app.tables import SocialApp, Admin, application_admin


def run_socialapp_selections(session):
    # select admins for the first socialapp
    app1 = session.query(SocialApp).first()
    print(app1.admin)

    # the same query using join
    admins = session.query(Admin).join(application_admin).filter_by(socialapp_id=app1.id).all()
    print(admins)

    # select socialapps for the first admin
    admin = session.query(Admin).first()
    print(admin.socialapps)

    # select socialapps and their's admins
    socialapps = session.query(SocialApp).join(application_admin).join(Admin) \
        .with_entities(SocialApp.title, Admin.first_name, Admin.last_name).all()
    print(socialapps)

    # select admins from the first socialapps
    admins = session.query(Admin).join(application_admin).filter_by(socialapp_id=app1.id).all()
    print(admins)

