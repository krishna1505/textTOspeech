name: Text-to-Speech Converter using Python & gTTS
description: |
  This is a simple Python project that converts the content of a text file into speech using Google's gTTS (Google Text-to-Speech) API.
  The output is saved as an MP3 audio file.

structure:
  - text.txt: Input file with the text to convert
  - text.mp3: Output audio file (generated)
  - main.py: Python script for conversion

features:
  - Converts text to clear audio
  - Saves as `.mp3` file
  - Easy to customize
  - Uses free gTTS library

technologies_used:
  - Python 3.x
  - gTTS (Google Text-to-Speech)

getting_started:
  instructions:
    - Clone the repository
    - Install dependencies
    - Add your text in `text.txt`
    - Run the script using: `python main.py`
  install_dependencies:
    - pip install gTTS
  run_script:
    - python main.py

how_it_works:
  code: |
    from gtts import gTTS
    import os

    with open("text.txt", "r") as abc:
        text = abc.read()

    obj = gTTS(text=text, lang="en", slow=False)
    obj.save("text.mp3")

    # Optional - For Windows
    os.system("start text.mp3")

output:
  description: |
    The script creates an audio file from the text and plays it (optional on Windows).
    Ideal for accessibility tools, voice assistants, or educational purposes.

useful_links:
  - gTTS Documentation: https://pypi.org/project/gTTS/
  - gTTS GitHub Repo: https://github.com/pndurette/gTTS

contribute:
  - Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

license:
  - This project is licensed under the MIT License.

author: Krishna Mohan Yadav
