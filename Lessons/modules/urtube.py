import time
from functools import partial

from Lessons.modules.user import User


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.check_login(login, password):
                self.current_user = user
                return True
        print("Неправильный логин или пароль")
        return False

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
            return
        self.users.append(User(nickname, password, age))
        self.current_user = self.users[-1]

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [vid.title for vid in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        titles = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return titles

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                break
        else:
            print("Видео не найдено.")
            return
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        video.play()
