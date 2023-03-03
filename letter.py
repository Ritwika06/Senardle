class LetterState:
    def __init__(self, char:str):
        self.char: str = char
        self.is_in_word: bool = False
        self.is_in_position: bool = False
        
    def __repr__(self):
        return f"[{self.char} is_in_word: {self.is_in_word}is_in_position: {self.is_in_position}]"
    