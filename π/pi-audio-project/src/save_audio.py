def save_audio_file(audio_data, filename):
    with open(filename, 'wb') as audio_file:
        audio_file.write(audio_data)