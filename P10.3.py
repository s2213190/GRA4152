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

 ##### This modification of method strips spaces and also ignores the lower/upper case
    def checkAnswer(self, response):
        return response.replace(" ","").lower() == self._answer.replace(" ","").lower()

 ## Displays this question.
 
    def display(self):
        print(self._text)
        
q1 = Question()

q1.setText("Who is the inventor of Python?")
q1.setAnswer("Guido Van Rossum")
q1.checkAnswer("guido van      rossum")  #Expected True as it strips spaces and also ignores the lower/upper case