import librosa
from IPython.display import Audio
from pathlib import Path

sr = 22050

def write_audio(audio: Audio, filename: str = "app/static/audio/tmp.wav"):
    print(f"Writing {filename}")
    with open(filename, "wb") as f:
        f.write(audio.data)

def tone(note: str):
    print(f"Generating tone with root {note}")
    y_sweep = librosa.chirp(fmin=librosa.note_to_hz(note),
                            fmax=librosa.note_to_hz('C5'),
                            sr=sr,
                            duration=1)

    write_audio(Audio(data=y_sweep, rate=sr))