# Pi Audio Project

This project generates an audio file containing the first one million digits of pi (π) and saves it as an audio file. It is designed as a fun gift for mathematics enthusiasts.

## Project Structure

```
pi-audio-project
├── src
│   ├── generate_pi.py       # Generates the first n digits of pi
│   ├── text_to_speech.py    # Converts text to speech and saves audio
│   └── save_audio.py        # Saves audio data to a file
├── requirements.txt          # Lists project dependencies
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pi-audio-project.git
   cd pi-audio-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Generate the digits of pi:
   - The `generate_pi.py` script contains a function `generate_pi_digits(n)` that generates the first `n` digits of pi. You can modify the script to generate one million digits.

2. Convert the digits to speech:
   - Use the `text_to_speech.py` script to convert the generated digits into speech. The `TextToSpeech` class has a method `speak(text)` that handles this.

3. Save the audio file:
   - The audio can be saved using the `save_audio.py` script, which contains a function `save_audio_file(audio_data, filename)`.

## Example

To generate an audio file of the first one million digits of pi, you can run the following commands in your Python environment:

```python
from src.generate_pi import generate_pi_digits
from src.text_to_speech import TextToSpeech
from src.save_audio import save_audio_file

# Generate 1 million digits of pi
pi_digits = generate_pi_digits(1000000)

# Convert to speech
tts = TextToSpeech()
audio_data = tts.speak(pi_digits)

# Save the audio file
save_audio_file(audio_data, 'pi_digits.wav')
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.