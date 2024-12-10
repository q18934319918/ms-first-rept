import os
import time


def get_screen_shot_path():
    file_name = "截图{}.png".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", file_name)
    return path


def get_logo_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "logo.txt")
    return path


def download_file_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file")
    return path


def get_yaml_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
    return path


def get_ini_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "setting.ini")
    return path


def get_log_path():
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.relpath(__file__))), "log")
    return path


if __name__ == '__main__':
    print(get_yaml_path())
