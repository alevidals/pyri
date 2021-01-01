class Pyri:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.reminders = []

    def listen(self):
        try:
            with self.microphone as source:
                print('Listening...')
                self.recognizer.adjust_for_ambient_noise(source)
                self.recognizer.dynamic_energy_threshold = 3000
                audio = self.recognizer.listen(source, timeout=3.0)
                response = self.recognizer.recognize_google(audio, language='es-ES').lower()
                keywords = ' '.join(response.split(' ')[:2])
                command = ' '.join(response.split(' ')[2:])
                print(response)
                if keywords == KEY:
                    # self.speak('¿En qué puedo ayudarte?')
                    return command
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def is_find_command(self, command):
        if command.split(' ')[0] in SEARCH_WORDS:
            return True

    def is_play_command(self, command):
        if command.split(' ')[0] in PLAY_WORDS:
            return True

    def is_reminder_command(self, command):
        if command.split(' ')[0] in REMINDER_WORDS:
            return True

    def analyze_command(self, command):
        try:
            if self.is_find_command(command):
                self.speak('Esto es lo que he encontrado')
                webbrowser.open(f"https://www.google.es/search?q={command}")
            elif self.is_play_command(command): # TODO: hacer que abra la canción
                self.speak(f'Reproduciendo {command}')
                webbrowser.open(f"https://www.youtube.com/results?search_query={command}")
            elif command == 'abre youtube':
                self.speak('Ábriendo YouTube')
                webbrowser.open('https://www.youtube.com')
            elif self.is_reminder_command(command):
                command_without_keywork = slice_text(command, 1)
                if command_without_keywork.startswith('a las'):
                    command_without_keywork = slice_text(command_without_keywork, 2)
                    tiempo = slice_text(command_without_keywork, 0, 'position', '')
                    tiempo = tiempo if ':' in tiempo else tiempo + ':00'
                    hour = int(slice_text(tiempo, 0, 'position', '', ':'))
                    minutes = int(slice_text(tiempo, 1, 'position', '', ':'))
                    tarea =slice_text(command_without_keywork, 1)
                    timestamp = datetime.now().replace(hour=hour, minute=minutes, second=0)
                    self.reminders.append(Reminder(tarea, timestamp))
                    self.speak('Vale te lo recordaré')
        except TypeError:
            pass

    def check_reminders(self):
        now = datetime.now().time()
        if (now.second == 0 or now.second == 0):
            for reminder in self.reminders:
                if now.minute == reminder.time.minute and now.hour == reminder.time.hour:
                    print(self.reminders)
                    self.reminders.remove(reminder)
                    print(self.reminders)
                    make_notification('Pyri reminder', reminder.task)