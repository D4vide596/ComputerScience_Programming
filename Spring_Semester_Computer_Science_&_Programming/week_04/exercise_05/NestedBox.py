class NestedBox:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value

        self.value=[]
        for obj in value:
            self.value.append(NestedBox(obj.value))
