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
        

class MultiChoiceQuestion(Question):
    
# Adding the __init__() function, the child class will no longer inherit the parent's __init__() function
# To keep the inheritance of the parent's __init__() function, adding a call to the parent's __init__() function

    def __init__(self):
        super().__init__()
                
    
    def setAnswer(self,*correctResponses):
        self._answer = [x.lower() for x in correctResponses]
        
    def checkAnswer(self, *response):
        return all(elem in response  for elem in self._answer)

q2 = MultiChoiceQuestion()
    
q2.setText("Name 3 OOP programming languages")
q2.setAnswer("Python","C++", "Javascript" )
q2.checkAnswer("python", "c++", "javascript") # Returns True as expected

q2.checkAnswer("python", "c++", "java") # Returns False as not all 3 responses match the answers