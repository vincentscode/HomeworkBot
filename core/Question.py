class Question:
    def __init__(self, raw_question):
        self.raw_question = raw_question
        self.processed_question = None
        self.answer = None

    def get_raw_question(self):
        return self.raw_question

    def set_processed_question(self, processed):
        self.processed_question = processed

    def get_processed_question(self):
        return self.processed_question

    def set_answer(self, answer):
        self.answer = answer
