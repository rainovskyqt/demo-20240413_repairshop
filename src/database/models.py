class User:
    def __init__(self, new_id: int, name: str, post: int, post_name: str = ""):
        self._id = new_id
        self._name = name
        self._post = post
        self._post_name = post_name


class Order:
    def __init__(self, add_date, resolve_date, equipment_id, fault_id,
                 description, client_id, status_id, worker_id, base_id = 0):
        self.add_date = add_date
        self.resolve_date = resolve_date
        self.equipment_id = equipment_id
        self.fault_id = fault_id
        self.description = description
        self.client_id = client_id
        self.status_id = status_id
        self.worker_id = worker_id
        self.base_id = base_id
