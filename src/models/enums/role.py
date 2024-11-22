import enum

class Role(enum.Enum):
    user="user"
    admin="admin"

    def get_value(self):
        return self.value