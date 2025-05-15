import asyncio
import json
import vosk
import pyaudio
from pythonosc.udp_client import SimpleUDPClient

# OSC Setup
osc_ip = "127.0.0.1"
osc_port = 10002
osc_address = "/speech"
osc_client = SimpleUDPClient(osc_ip, osc_port)

# Vosk Model Path
model_path = "/Users/myLaptop/Desktop/TD_Teaching/TD SpeechToText/Models/vosk-model-en-us-0.22"
model = vosk.Model(model_path)

# Output text file path
output_file_path = "/Users/myLaptop/Desktop/osc-td-test/recognized_text.txt"

def setup_stream():
    #Initialize PyAudio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=8192)
    return p, stream

async def recognize_and_send():
    #Continuously recognize speech and send via OSC
    rec = vosk.KaldiRecognizer(model, 16000)
    p, stream = setup_stream()

    print("-Listening for speech. Say 'Terminate' to stop.")
    with open(output_file_path, "w") as output_file:
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                recognized_text = result.get("text", "").strip()

                if recognized_text:
                    print(f"Recognized: {recognized_text}")
                    output_file.write(recognized_text + "\n")
                    output_file.flush()
                    osc_client.send_message(osc_address, recognized_text)

                    if "terminate" in recognized_text.lower():
                        print("-Termination keyword detected. Stopping...")
                        break

            await asyncio.sleep(0.01)  # Small sleep to yield control

    stream.stop_stream()
    stream.close()
    p.terminate()

async def main():
    await recognize_and_send()

if __name__ == "__main__":
    asyncio.run(main())
