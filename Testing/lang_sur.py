from survey import AnonymosSurvey
import json

question = "Какую операционную систему предпочитаете?"
my_survey = AnonymosSurvey(question)

my_survey.show_question()
print("Нажми 'q' для выхода из опроса.")
while True:
    response = input()
    if response == 'q':
        break
    else:
        my_survey.store_responses(response)

my_survey.show_responses()

with open('list.json', 'w') as f:
    json.dump(my_survey.responses, f)
