quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

for i in range(4):
    quizFile.write(' %s. %s\n' % ('ABCD' [i], answerOptions[i]))
quizFile.write('\n')
    
