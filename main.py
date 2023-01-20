import re
import long_responses as long
from datetime import date
from datetime import datetime

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    today = date.today()
    now = datetime.now()
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', "what's up?"], single_response=True)
    response('See you!', ['bye', 'goodbye', "bye-bye"], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Of course... why not, you are very kind hearted', ['do', 'want', 'you', 'to', 'friends', 'with', 'me', 'be'], required_words=['want', 'to', 'friends', 'be'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('I am chatbots made with complicated logic', ['who', 'are', 'you', 'human', 'animal'], required_words=['are', 'you'])
    response('I know, today\'s date: ' + today.strftime("%d %B, %y"), ['what', 'date', 'today', 'is'], required_words=['date', 'today'])
    response('What a good time to have fun, because it\'s ' + now.strftime("%H:%M") + ' o\'clock now', ['what', 'is', 'it', 'time'], required_words=['what', 'time', 'is', 'it'])

    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Bot: ' + get_response(input('You: ')))
