from app.tables import Object, SocialApp, Operation


def insert_all(session):
    socialapp1 = session.query(SocialApp).first()

    object1 = Object(title='object1', socialapp=socialapp1)
    object2 = Object(title='object2', socialapp=socialapp1)
    object3 = Object(title='object3', socialapp=socialapp1)
    object4 = Object(title='object4', socialapp=socialapp1)

    operations = [
        Operation(title='create', object=object1),
        Operation(title='update', object=object1),

        Operation(title='create', object=object2),
        Operation(title='update', object=object2),

        Operation(title='post', object=object3),
        Operation(title='view', object=object3),

        Operation(title='post', object=object4),
        Operation(title='view', object=object4),
    ]
    session.add_all(operations)

    extra_object = Object(title='extra', socialapp=socialapp1)
    operations = [
        Operation(title='extra_permission1', object=extra_object),
        Operation(title='extra_permission2', object=extra_object),
    ]
    session.add(extra_object)
    session.add_all(operations)
