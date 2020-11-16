
from .models import Question, Participant, QuestionResponse

"""
If you were trying to figure out if a person lived in Los Angeles
or not, the above question would be helpful to you.
"""


def populateDB():
    questionTextList = [
        "I can get from my house to the beach by car in less than an hour.",
        "I have been to a place that I have seen in the background of a movie.",
        "I don't own any heavy coats or heavy jackets.",
        "I eat Mexican food at least once a month.",
        "I live somewhere where the seasons are distinct from each other ",
        "I have seen a food truck near my work or school in the last month.",
        "I have been To Dodger Stadium in the last year ",
        "I own a car ",
        "I live within a 30 minute drive to a hospital",
        "I feel safe walking in my neighborhood at night",
        "I wear a watch almost every day ",
        "I sleep 7 hours or less on most nights ",
        "I usually take at least one freeway to get to work or school ",
        "I take a walk outdoors at least once a week ",
        "I have a garden near my living area that I work on at least once a month",
        "I have at least one living brother or sister",
        "I have at least one dog or cat as a pet",
        "I enjoy gambling",
        "I hear police or firefighter sirens at least once a day",
        "I have had a conversation with a stranger that made me uncomfortable in the last week"
        ]

    for questionText in questionTextList:
        print("adding db entry for {}...".format(questionText))
        tempQuestion = Question(text = questionText)
        tempQuestion.save()

"""
    for x in range(10):
        p = Participant(livesInLA = False)
        p.save()

        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 1), answer = 0, rating = 2)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 2), answer = 0, rating = 4)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 3), answer = 0, rating = 3)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 4), answer = 0, rating = 4)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 5), answer = 1, rating = 5)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 6), answer = 1, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 7), answer = 0, rating = 3)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 8), answer = 1, rating = 4)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 9), answer = 1, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 10), answer = 1, rating = 4)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 11), answer = 0, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 12), answer = 0, rating = 5)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 13), answer = 1, rating = 4)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 14), answer = 1, rating = 4)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 15), answer = 0, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 16), answer = 1, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 17), answer = 1, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 18), answer = 1, rating = 1)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 19), answer = 0, rating = 5)
        qr1.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 20), answer = 0, rating = 4)
        qr1.save()





    for x in range(10):
        p = Participant(livesInLA = True)
        p.save()
        qr1 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 1), answer = 1, rating = 4)
        qr1.save()
        qr2 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 2), answer = 1, rating = 5)
        qr2.save()
        qr3 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 3), answer = 1, rating = 3)
        qr3.save()
        qr4 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 4), answer = 1, rating = 3)
        qr4.save()
        qr5 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 5), answer = 0, rating = 2)
        qr5.save()
        qr6 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 6), answer = 1, rating = 5)
        qr6.save()
        qr7 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 7), answer = 0, rating = 5)
        qr7.save()
        qr8 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 8), answer = 1, rating = 1)
        qr8.save()
        qr9 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 9), answer = 1, rating = 3)
        qr9.save()
        qr10 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 10), answer = 0, rating = 2)
        qr10.save()
        qr11 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 11), answer = 1, rating = 1)
        qr11.save()
        qr12 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 12), answer = 1, rating = 1)
        qr12.save()
        qr13 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 13), answer = 1, rating = 4)
        qr13.save()
        qr14 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 14), answer = 1, rating = 3)
        qr14.save()
        qr15 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 15), answer = 1, rating = 5)
        qr15.save()
        qr16 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 16), answer = 0, rating = 1)
        qr16.save()
        qr17 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 17), answer = 1, rating = 2)
        qr17.save()
        qr18 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 18), answer = 1, rating = 1)
        qr18.save()
        qr19 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 19), answer = 1, rating = 4)
        qr19.save()
        qr20 = QuestionResponse(participant = Participant.objects.get(pk=p.id), question = Question.objects.get(pk = 20), answer = 1, rating = 1)
        qr20.save()

"""
