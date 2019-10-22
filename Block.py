import GameManager
class Block:
    coords = [0,0]
    value = 2
    def Stack(self, otherBlock):
        self.value *= 2;
        GameManager.GameManager.Score += self.value
        otherBlock.value = 0