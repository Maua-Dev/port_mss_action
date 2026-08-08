class CreateChatViewmodel:
    answer: str

    def __init__(self, answer: str):
        self.answer = answer

    def to_dict(self):
        return {
            'answer': self.answer,
        }
