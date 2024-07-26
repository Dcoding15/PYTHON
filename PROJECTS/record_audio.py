import pyaudio
import wave

def record_audio(output_filename, duration=5, sample_rate=44100, channels=2, format=pyaudio.paInt16):
    """
    Record audio from the microphone and save it to a WAV file.

    Parameters:
    - output_filename: Filename to save the recorded audio (e.g., 'recorded_audio.wav')
    - duration: Recording duration in seconds (default is 5 seconds)
    - sample_rate: Sampling rate of the audio (default is 44100 Hz)
    - channels: Number of audio channels (default is 2 for stereo)
    - format: Audio sample format (default is 16-bit signed integer)
    """
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set parameters for recording
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=1024)

    print("Recording...")

    frames = []
    # Record audio in chunks and store in frames
    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {output_filename}")

if __name__ == "__main__":
    output_filename = "recorded_audio.wav"
    record_audio(output_filename, duration=5)