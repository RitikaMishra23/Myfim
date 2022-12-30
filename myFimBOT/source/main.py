import cv2
import os
import modules.functions as function
import modules.speech as speech
import modules.getIntent as Intent
import modules.detect as detect

# create an object from speech module
engine = speech.Speech()
listening = False
intent = None


while True:
    cam = cv2.VideoCapture(0)
    # if above statement does not work, try cam = cv2.VideoCapture(0)

    if not listening:
        resp = engine.recognize_speech()
        if(resp != None):
            intent = Intent.get_intent(resp)
        if(intent == 'myFimBOT' and resp != None):
            listening = True

    else:
        engine.text_to_speech("What can I help you with?")
        intent = ''
        engine.text_to_speech("Listening")
        resp = engine.recognize_speech()
        engine.text_to_speech("Processing")

        if(resp != None):
            intent = Intent.get_intent(resp)
            intent = intent.lower()

            if(intent == 'Fund Transfer'):
                function.go_to_fund_transfer()


            elif(intent == 'read'):
                detect.read(cam=cam)

            elif(intent == 'Insurance'):
                function.show_Insurance()

            
            elif(intent == 'account statement'):
                function.go_to_services()
            elif(intent=='user'):
                function.go_user_profile()
            


            elif(intent == 'receipt'):
                detect.analyzeReceipt()

       

            elif intent == 'stop':
                listening = False
                engine.text_to_speech(
                    "OK Quitting now, Please tell me if you need my assistance again.")

            elif resp != None:
                # no intent matched
                engine.text_to_speech(
                    "Sorry, I did not understood. Can you say it again?")

    cam.release()
fs
