import speech_recognition as sr
from flask import logging, Flask, render_template, request, flash

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.secret_key = "Oyekanmi"

@app.route('/')
def index():
    flash(" Welcome to Tamil Speech to Text Platform")
    return render_template('index.html')

@app.route('/speechrecognize/')
def audio_to_text():
    flash(" Press Start to begin recording audio and press Stop to end recording audio")
    return render_template('speechrecognize.html')

@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)
  
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='ta-IN', show_all=True)
        print(text)
        return_text = " You said : <br> "
        try:
            romanOrthography = ["Alai", "Muganool", "Alai (Azhai)", "Azhai", 
            "ALaippithal", "azhaippithazh", "ALaippithal (azhaippithazh)",
            "ViLuppuram (Vizhuppuram)", "Kallu", "KaLLu", "PiLai (pizhai)",
            "Valu", "vaalkkai (vaazhkkai)", "vannam (vaNNam)", "vilakku (viLakku)", "Palani (Pazhani)",
            "Maattu", "Meettu", "Kaalai", "ThozhilaaLi", "Kalai (kaLai)", "Muttu", "KiLai",
             "Kuttu", "KiLi (Kizhi)", "Maettu", "Thoguppaalar (ThoguppaaLar)", "ENNai", 
             "EttrukkoL", "ELuthugoL (Ezhuthugol)", "Manappanmai", "Valu"]

            tamilOrthography = ["அலை", 
            "முகநூல்", "முக நூல்", 
            "முக நூல் முக நூல்", 
            "அலை", "அழை", "அலை  அழை", 
            "அலை அழை", 
            "அளைப்பிதல்", 
            "அழைப்பிதழ்", 
            "அளைப்பிதல் அழைப்பிதழ்", 
            "அளைப்பிதல் (அழைப்பிதழ்)",
            "விளுப்புரம் (விழுப்புரம்)",
            "விளுப்புரம் விழுப்புரம்",
            "விளுப்புரம்", "விழுப்புரம்", 
            "கல்லு", "கள்ளு", 
            "பிளை (பிழை)", 
            "பிளை பிழை", 
            "பிளை", "பிழை", 
            "வாலு",
            "வால்க்கை", "வாழ்க்கை",
            "வால்க்கை (வாழ்க்கை)",
            "வால்க்கை வாழ்க்கை", 
            "வன்னம்", "வண்ணம்", 
            "வன்னம் (வண்ணம்)", 
            "வன்னம் வண்ணம்", 
            "விலக்கு",
            "விளக்கு",
            "விலக்கு (விளக்கு)", 
            "விலக்கு விளக்கு", 
            "பலனி", 
            "பழனி",
            "பலனி (பழனி)", 
            "பலனி பழனி", 
            "மாட்டு", 
            "மீட்டு", 
            "காலை",
            "தொழிலாளி", 
            "கலை",
            "களை",
            "கலை களை",
            "கலை (களை)", 
            "முட்டு", "கிளை",
            "குட்டு", 
            "கிளி",
            "கிழி",
            "கிளி கிழி",
            "கிளி (கிழி)", 
            "மேட்டு", 
            "தொகுப்பாலர்",
            "தொகுப்பாளர்", 
            "தொகுப்பாலர் தொகுப்பாளர்",
            "தொகுப்பாலர் (தொகுப்பாளர்)",
            "எண்ணை", 
            "ஏற்றுக்கொள்",
            "எளுதுகோள்",
            "எழுதுகோல்", 
            "எளுதுகோள் (எழுதுகோல்)",
            "எளுதுகோள் எழுதுகோல்",
            "மனப்பான்மை"]

            for num, texts in enumerate(text['alternative']):
                if texts['transcript'] in tamilOrthography:
                    return_text = texts['transcript']  + " <br> "
                else:
                    return_text = "Word not found in given Tamil Orthography"
        except:
            return_text = " Sorry! Voice was not detected "
        
    return str(return_text)


if __name__ == "__main__":
    app.run(debug=True)