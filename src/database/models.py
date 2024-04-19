class User:
    def __init__(self, new_id: int, name: str, post: int, post_name: str = ""):
        self._id = new_id
        self._name = name
        self._post = post
        self._post_name = post_name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def post(self):
        return self._post

    @post.setter
    def post(self, new_post):
        self._post = new_post

    @property
    def post_name(self):
        return self._post_name
