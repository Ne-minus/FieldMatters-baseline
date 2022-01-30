#/Users/eneminova/speech_rec1
import time
from subprocess import Popen
from speech_recognition import (Recognizer, AudioFile)
from speech_recognition import (UnknownValueError, RequestError)


class SpeechOggAudioFileToText:
    def __init__(self):
        self.recognizer = Recognizer()

    def ogg_to_wav(self, file):
        args = ['ffmpeg','-i', file, 'audio_noise.wav']
        process = Popen(args)
        process.wait()
    @property
    def text(self):
        AUDIO_FILE = 'audio_noise.wav'
        with AudioFile(AUDIO_FILE) as source:
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_google(audio, language='RU')
            return text
        except UnknownValueError:
            print("Не удаётся распознать аудио файл")
        except RequestError as error:
            print("Не удалось запросить результаты: {0}".format(error))

def main():
    start_time = time.time()
    speech_ogg = SpeechOggAudioFileToText()
    speech_ogg.ogg_to_wav('audio_noise.ogg')
    print(speech_ogg.text, time.time()-start_time, sep='\n')

if __name__ == '__main__':
    main()