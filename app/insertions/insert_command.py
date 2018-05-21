class InsertCommand(object):
    def __init__(self, session):
        super(InsertCommand, self).__init__()
        self.session = session

    def execute(self):
        raise NotImplementedError()
