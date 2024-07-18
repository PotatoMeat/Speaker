import speech_recognition as speech_r
import pyaudio
import wave

import keyboard


class speech_decoder:

    def __init__(self, CHUNK=1024, FORMAT=pyaudio.paInt16, CHANNEL=1, RATE=44100, WRITE_LATTER='R'):
        self.CHUNK = CHUNK
        self.FRT = FORMAT
        self.CHAN = CHANNEL
        self.RT = RATE
        self.OUTPUT = "out/output.wav"

        self.WRITE_LATTER = WRITE_LATTER

        self.p = pyaudio.PyAudio()



    def record(self):
        self.stream = self.p.open(format=self.FRT, channels=self.CHAN, rate=self.RT, input=True,
                        frames_per_buffer=self.CHUNK)  # открываем поток для записи

        print('To record, press ' + self.WRITE_LATTER)
        keyboard.wait(self.WRITE_LATTER, suppress=True)
        print("rec")
        frames = []  # формируем выборку данных фреймов

        while keyboard.is_pressed(self.WRITE_LATTER):
            data = self.stream.read(self.CHUNK)
            frames.append(data)

        print("done")

        self.stream.stop_stream()  # останавливаем и закрываем поток
        self.stream.close()
        self.p.terminate()

        w = wave.open(self.OUTPUT, 'wb')
        w.setnchannels(self.CHAN)
        w.setsampwidth(self.p.get_sample_size(self.FRT))
        w.setframerate(self.RT)
        w.writeframes(b''.join(frames))
        w.close()

        sample = speech_r.WavFile('out/output.wav')

        ansver = self.decode_audio(sample)

        return ansver


    def decode_audio(self, sample):
        r = speech_r.Recognizer()

        ansver = ''

        with sample as audio:
            content = r.record(audio)
            r.adjust_for_ambient_noise(audio)
            ansver = r.recognize_google(content, language="ru-RU")

        return ansver

