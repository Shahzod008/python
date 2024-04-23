import pyttsx3
import speech_recognition as sr
import webbrowser
import urllib.parse
import os
import time
import random
import pyautogui
from pathlib import Path

engine = pyttsx3.init()
engine.setProperty('rate', 250)
engine.setProperty('volume', 1)
engine.setProperty('pitch', 0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.5
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ru")
        return text
    except sr.UnknownValueError:
        command = recognize_speech().lower()
        print("Распознал: ", command)
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи: ".format(e))
    return ""

print("Ассистент деактивирован для активации говорите имя ассистента (Джарвис)")

def google(command):
    webbrowser.open("https://www.google.com")
    speak("Открываю гугл.")
    speak("Что вы хотите найти?")
    query = recognize_speech() 
    if query == "ничего":
        speak("Удачи вам!")
    elif not query:
        speak("Что вы хотите найти?")
    else:
        speak(f"Ищу {query} в Google.")
        query_encoded = urllib.parse.quote(query)
        webbrowser.open(f"https://www.google.com/search?q={query_encoded}")

def youtube(command):
    webbrowser.open("https://www.youtube.com")
    speak("Открываю ютуб") 
    speak("Что ищем в ютубе?")
    query = recognize_speech() 
    if query == "ничего":
        speak("Приятного просмотра")
    else:
        speak(f"Ищу {query} в ютубе.")
        query_encoded = urllib.parse.quote(query)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query_encoded}")

def jokess(command):
    jokes = ["Мой разработчик не научил меня анекдотам ха ха ха ха",
            "Мат не украшает речь, но делает ее намного более понятной.",
            "Деньги - зло, но чем больше у меня этого зла, тем я добрее.",
            "Не говорите мне, что у вас в жизни все хорошо - мне от этого плохо!",
            "Почему после двадцать девятого числа идет тридцатое, а не двадцать десятое?",
            "Какое животное всегда готово поддержать разговор на любую тему? Попугай!"]
    jokes = random.choice(jokes)
    speak(jokes)

def mkdr(command):
    speak("признесите название папки")
    folder_path = Path(recognize_speech())
    if not folder_path.exists():
        folder_path.mkdir()
        print("Папка успешно создана")
    else:
        print("Папка уже существует")

def mkd(command):
    speak("ведите название файла")
    file_path = input("Ведите название файла: ")
    with open(file_path, 'w'):
        print("Файл успешно создан и записан")

def on(command):
    speak("Вы подтверждаете действие?")
    response = recognize_speech().lower()
    if response in ["да", "ес", "выруби", "отключи"]:
        speak("Отключаю")
        os.system("shutdown /s /t 0")
    else:
        speak("Принято, отменяю.")


jarvic = "джарвис"


def handle_command(command):
    if any(keyword in command.lower()for keyword in ["скрой окна", "востанови все окна", "скрой окно", "окно скрой"]):
        pyautogui.hotkey("win", "Shift", "m")
        speak("скрываю")

    elif any(keyword in command.lower()for keyword in ["новая папка"]):
        mkdr(command)
        speak("Папка успешно создана")

    elif any(keyword in command.lower()for keyword in ["новый файл"]):
        mkd(command)
        speak("Файл успешно создана")

    elif any(keyword in command.lower()for keyword in ["мой адрес", "где я живу"]):
        speak("Вы живёте по адресу город Химки, деревня Брёхово микрайон школьный корпус восемь квартира 205")

    elif any(keyword in command.lower()for keyword in ["сверни окна", "сверни все окна", "сверни окно", "окно сверни"]):
        pyautogui.hotkey("win", "m")
        speak("закрываю")

    elif any(keyword in command.lower()for keyword in ["переключи раскладки клавиатуры", "переключи раскладку", "раскладка", " смени язык", "переключить раскладку"]):
        speak("сменил")
        pyautogui.hotkey("alt", "Shift")

    elif any(keyword in command.lower()for keyword in ["скриншот", "сделай скрин", "скрин экрана", "сделай скриншот"]):
        pyautogui.hotkey("win", "PrtSc")
        speak("сделала")

    elif any(keyword in command.lower()for keyword in ["открой настроечку", "настроечку открой", "настройка", "открой настройку"]):
        pyautogui.hotkey("win", "i")
        speak("сделала")
    
    elif any(keyword in command.lower() for keyword in ["телеграмм", "telegram", "телега", "открой телеграмм", "открой telegram", "телеграммчик", "открой телегу", "открой телеграммчик",]):
        os.startfile(r"C:\Users\shakh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram.lnk")
        speak("Открываю телеграмм")

    elif any(keyword in command.lower() for keyword in ["инстаграмм", "instagram", "инста", "открой инстаграмм", "открой instagram", "инстаграммчик", "открой инсту", "открой инстаграммчик",]):
        webbrowser.open("https://www.instagram.com/")
        speak("открываю самый любымий сайт инстаграмм")

    elif any(keyword in command.lower() for keyword in ["вк", "вконтакте", "vk", "открой вконтакте", "сайт вк"]):
        webbrowser.open("https://m.vk.com/")
        speak("открываю сайт вк")

    elif any(keyword in command.lower() for keyword in ["metanit", "метанит", "открой метанит", "открой сайт metanit"]):
        webbrowser.open("https://metanit.com/")
        speak("открываю сайт метанит")
    
    elif any(keyword in command.lower() for keyword in ["kino poisk", "кинопоиск", "открой кинопоиск", "открой сайт кинопоиск"]):
        webbrowser.open("https://www.kinopoisk.ru/")
        speak("открываю сайт кино поиск")

    elif any(keyword in command.lower() for keyword in ["открой чат", "чат gpt", "искуственный интелект"]):
        webbrowser.open("https://chat.openai.com/?model=text-davinci-002-render-sha")
        speak("Браузер, открыт")

    elif any(keyword in command.lower() for keyword in ["музыка", "музыку", "включи музончик", "включи музон", "врубай музон", "мияги", " miyagi"]):
        os.startfile(r"C:\Users\shakh\OneDrive\Рабочий стол\Моя папка\Miyagi & Эндшпиль —  Все лучшие треки (Плейлист 2023).mp4")
        speak("Включаю музон")

    elif any(keyword in command.lower() for keyword in ["браузер", "поисковик"]):
        webbrowser.open("https://www.google.com")
        speak("Браузер, открыт")

    elif any(keyword in command.lower() for keyword in ["здарова", "привет", "хай"]):
        speak("Приветствую, чем могу помочь?")

    elif any(keyword in command.lower() for keyword in ["время", "который час", "текущее время"]):
        speak(time.strftime("Сейчас %H:%M"))

    elif any(keyword in command.lower() for keyword in ["дата", "число", "сегодняшняя дата"]):
        speak(time.strftime("севодня %d %m %Y"))

    elif any(keyword in command.lower()for keyword in ["гугл", "google", "открой гугл", "открой google", "open google", "open гугл"]):
        google(command)

    elif any(keyword in command.lower() for keyword in ["открой ютуб", "ютуб", "youtube", "ютубчик", "открой youtube", "открой ютубчик"]):
        youtube(command)

    elif any(keyword in command.lower() for keyword in ["проводник", "папка", "открой папку"]):
        os.startfile(os.path.expanduser("~"))
        speak("Открываю проводник")

    elif any(keyword in command.lower() for keyword in ["выруби ноут", "отключи ноутбук", "выключи ноутбук"]):
        on(command)

    elif any(keyword in command.lower()for keyword in ["открой калькулятор", "калькулятор", "калкулатор"]):
        os.startfile("calc.exe")
        speak("Открываю калькулятор")

    elif any(keyword in command.lower() for keyword in ["скажи шутку", "расскажи шутку", "анекдот", "расскажи анекдот"]):
        jokess(command)

    elif any(keyword in command.lower() for keyword in ["панель управление", "панель"]):
        os.startfile(r"C:\Users\shakh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Control Panel.lnk")
        speak("Открываю панель управления")

    elif any(keyword in command.lower() for keyword in ["vs","открой визуал студио", "открой редактор кода", "редактор кода", "идел", "visual studio"]):
        os.startfile(r"C:\Users\shakh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
        speak("Открываю редактор")

    elif any(keyword in command.lower() for keyword in ["открой смд", "цмд", "командную строку", "смд", "терминал", "cmd"]):
        os.system("start cmd")
        speak("Открываю терминал")

    elif any(keyword in command.lower()for keyword in ["благодарю", "спасибо", "рахмат", "спасыбочка", "благодырочка", "спосибо", "ташакур", "ташакор"]):
        speak("ич гап не")

    elif any(keyword in command.lower()for keyword in ["расскажи о себе", "твоя история", "о себе", "о боте", "кто основал бота",]):
        speak("мне нечего рассказать вам")

    elif any(keyword in command.lower()for keyword in ["джарвис", "лили", "марсель"]):
        privetstvie = ["Как я могу быть полезным?",
                       "Слушаюсь",
                       "Приветствую",
                       "Привет",
                       "Здравствуйте",
                       "Всегда рад помочь",
                       "Слушаю",
                       "Чем могу помочь?",
                       "Всегда готов помочь.",
                       "К вашим услугам.",
                       "Слушаю и выполняю.",
                       "Приветствую вас!",]
        privetstvie = random.choice(privetstvie)
        speak(privetstvie)
 
    elif any(keyword in command.lower()for keyword in ["прекратить", "прекрати", "на сегодня всё", "вырубись", "отключайся", "пока"]):
        speak("Рада была помочь")
        quit()

    else:
        speak("я не понимаю. перефразируй.")

def index():
    engine = pyttsx3.init()
    engine.setProperty('rate', 250)
    engine.setProperty('volume', 1)
    engine.setProperty('pitch', 50)
    activated = False
    while True:
        if not activated:
            command = recognize_speech().lower()
            if command in ["лили", "джарвис"]:
                activated = True
                privetstvie = ["Как я могу быть полезным?",
                                "Слушаюсь",
                                "Приветствую",
                                "Привет",
                                "Здравствуйте",
                                "Всегда рад помочь",
                                "Слушаю",
                                "Чем могу помочь?"
                                "Всегда готов помочь."
                                "К вашим услугам."
                                "Слушаю и выполняю."
                                "Приветствую вас!"]
                privetstvie = random.choice(privetstvie)
                speak(privetstvie)
                print("Ассистент активирован")

        else:
            command = recognize_speech()
            if command:
                command = command.lower()
                print("Вы сказали:", command)

                if any(keyword in command for keyword in ["отдыхать", "отдыхай"]):
                    speak("Спасибо, рада была помочь!")
                    activated = False
                    print("Ассистент деактивирован")

                else:
                    handle_command(command)

if __name__ == "__main__":
    index()