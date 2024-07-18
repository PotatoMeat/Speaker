from speech_decoder import speech_decoder
from speaker import speaker

import keyboard
import json


decod = speech_decoder()
speaker = speaker()


def what_to_say(input, requests, answers):

    for i in requests:
        if i['req'] in input:
            return answers[i['id']]['ans']
    return 'Спасибо'


def mode_record(requests, answers):
    ans = decod.record()
    print(ans)
    ans = what_to_say(ans.lower(), requests, answers)
    print(ans)
    speaker.talk(ans)

def mode_transcibe(input, requests, answers):
    ans = decod.decode_audio(input)
    ans = what_to_say(ans.lower(), requests, answers)
    speaker.talk(ans)


with open('scenarios.json', 'r', encoding="UTF-8") as json_file:
    data = json.load(json_file)

    requests = data['request']
    answers = data['answer']

mode_record(requests, answers)

