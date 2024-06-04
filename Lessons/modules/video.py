from time import sleep


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Название: {self.title}, Продолжительность: {self.duration} секунд, сейчас: {self.time_now}"

    def __repr__(self):
        return f"Видео({self.title}, {self.duration}, {self.time_now}, {self.adult_mode})"

    def play(self):
        print(f"Проиграть '{self.title}'")
        for i in range(self.duration - self.time_now):
            print(i)
            sleep(1)

        print("Конец")

    def pause(self):
        print("Пауза.")

    def resume(self):
        print("Воспроизвести")

    def replay(self):
        self.time_now = 0
        print("Перезапустить")
        self.play()
