class Enemy:
    def __init__(self, kind, damage):
        self.kind = kind
        self.damage = damage
    
    def show_info(self):
        print(f"Враг: {self.kind}, урон: {self.damage}")