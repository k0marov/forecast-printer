class EnvKeyException(Exception):
    def __init__(self, *args, key: str):
        super().__init__(*args)
        self.key = key
    def __repr__(self):
        return f"Could not find {self.key} environment variable!"
    def __str__(self):
        return self.__repr__()