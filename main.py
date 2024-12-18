class ThreadData:
    __share_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__= self.__share_attrs