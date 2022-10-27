## A question with a text and an answer.
class Question:
    def __init__(self):
        self._text = ""
        self._answer = ""

 ## Sets the question text.
 # @param questionText the text of this question
 
    def setText(self, questionText):
        self._text = questionText

 ## Sets the answer for this question.
 # @param correctResponse the answer
 
    def setAnswer(self, correctResponse):
        self._answer = correctResponse

 ## Checks a given response for correctness.
 # @param response the response to check
 # @return True if the response was correct, False otherwise

    def checkAnswer(self, response):
        return response == self._answer

 ## Displays this question.
 
    def display(self):
        print(self._text)
 
# NumericQuestion inherits from Superclass Question

class NumericQuestion(Question):
    def __init__(self):
        super().__init__()
    
# Overrides Superclass

    def checkAnswer(self,response):
        return abs(float(response) - float(self._answer)) < 0.01
    

num1 = NumericQuestion()

num1.setText("State the value of Square Root of 99?")
num1.setAnswer(9.9498)

num1.checkAnswer(9.95)  # Returns True as expected
num1.checkAnswer(9.93)   # Returns False as expected
