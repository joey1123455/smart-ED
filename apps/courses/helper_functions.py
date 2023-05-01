"""0 1111000 1100110 1110000 1110011 - 
    A king who made this possible"""

def parse(questions):
    questionsArray = []
    questionsObject = {
        "question": "",
        "answers": [],
        "answer": ""
    }

    splitQuestions = questions.split("\n")
    # print(splitQuestions)

    questionChunkCount = len(splitQuestions) // 7

    index = 0

    while index < questionChunkCount:
        questionChunk = splitQuestions[:7]
        

        questionsObject["question"] = questionChunk[0]

        answersChunk = questionChunk[1 : 6]
        for i in answersChunk:
            questionsObject["answers"].append(i)

        questionsObject["answer"] = questionChunk[6]
        
        questionsArray.append(questionsObject)
    
        questionsObject = {
            "question": "",
            "answers": [],
            "correct": ""
        }

        splitQuestions = splitQuestions[8 :]
        
        index += 1

    return questionsArray



