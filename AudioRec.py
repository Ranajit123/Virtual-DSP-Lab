import pyaudio
import wave
import numpy as np

sec = 2
def audioPlot(sec):
  global audio_array
  global times
  FRAMES_PER_BUFFER = 3200
  FORMAT = pyaudio.paFloat32
  CHANNELS = 1
  RATE = 16000

  pa = pyaudio.PyAudio()

  stream = pa.open(
      format=FORMAT,
      channels=CHANNELS,
      rate=RATE,
      input=True,
      frames_per_buffer=FRAMES_PER_BUFFER
  )

  print('start recording')
  seconds=sec
  frames = []
  second_tracking = 0
  second_count = 0
  for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)
    second_tracking += 1
    if second_tracking == RATE/FRAMES_PER_BUFFER:
        second_count += 1
        second_tracking = 0
        print(f'Time Left: {seconds - second_count} seconds')

  stream.stop_stream()
  stream.close()
  pa.terminate()

  obj = wave.open('lemaster_tech.wav', 'wb')
  obj.setnchannels(CHANNELS)
  obj.setsampwidth(pa.get_sample_size(FORMAT))
  obj.setframerate(RATE)
  obj.writeframes(b''.join(frames))
  # obj.close()

  file = wave.open('lemaster_tech.wav', 'rb')

  sample_freq = file.getframerate()
  frames = file.getnframes()
  signal_wave = file.readframes(-1)

  # file.close()

  time = frames / sample_freq

  audio_array = np.frombuffer(signal_wave, dtype='float32')
  print (audio_array)

  times = np.linspace(0, time, num=frames)
  print(times)

  # return audio_array, time

# audioPlot()