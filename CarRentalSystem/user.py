class User:
    def __init__(self, user_id: int, name: str, driving_license: str):
        self._user_id = user_id
        self._name = name
        self._driving_license = driving_license

    def get_user_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_driving_license(self) -> str:
        return self._driving_license
