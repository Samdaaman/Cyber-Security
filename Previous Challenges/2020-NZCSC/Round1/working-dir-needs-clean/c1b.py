import wave
import pyaudio

p = pyaudio.PyAudio()
wf = wave.open('audio.wav', 'rb')
CHUNK = 1024
stream = p.open(
    format=pyaudio.paInt16,
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True
)
buffer = wf.readframes(CHUNK)
print(buffer)
counter = 0
while len(buffer) > 0:
    stream.write(buffer)
    buffer = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()



