class Entry:
    def __init__(self, v) -> None:
        self.value = v
        if v == '.':
            self.range = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        else:
            self.range = {v}

    def set_val(self, v):
        self.value = v
        self.range = {v}

    def eliminate_val(self, v):
        self.range.discard(v)

    def get_liberty(self):
        return len(self.range)
