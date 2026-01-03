class StateStore:
    def __init__(self):
        self._store = {}
    def set(self, key, value):
        self._store[key] = value
    def get(self, key, default=None):
        return self._store.get(key, default)
    def as_text(self):
        return "\n".join(f"{k}: {v}" for k, v in self._store.items())
