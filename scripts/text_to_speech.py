import pyttsx3


def convert_headlines_to_speech(headlines):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
    engine.say(headlines)
    engine.runAndWait()
