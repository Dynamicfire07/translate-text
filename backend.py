import requests

def converstion(input_lang,output_lang):
    languages = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Chinese": "zh",
        "Japanese": "ja",
        "Russian": "ru",
        "Arabic": "ar",
        "Portuguese": "pt",
        "Hindi": "hi",
        "Bengali": "bn",
        "Korean": "ko",
        "Italian": "it",
        "Dutch": "nl",
        "Turkish": "tr",
        "Swedish": "sv",
        "Polish": "pl",
        "Vietnamese": "vi",
        "Thai": "th",
        "Indonesian": "id"
    }
    ISO_input = languages[input_lang]
    ISO_output = languages[output_lang]

    return ISO_input,ISO_output


def translate(input,output,translate_text):
        url = f"https://api.mymemory.translated.net/get?q={translate_text}!&langpair={input}|{output}"
        response = requests.get(url)
        text = response.json()
        text = text['responseData']['translatedText']
        return text


if __name__ == "__main__":
    input,output = converstion("English","French")
    x = translate(input,output,"Hello world")
    print(x)

