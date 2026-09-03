import os
import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class DownloaderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text="ভিডিও লিঙ্ক দিন:")
        layout.add_widget(self.label)
        
        self.url_input = TextInput(hint_text="https://...", multiline=False)
        layout.add_widget(self.url_input)
        
        btn_mp4 = Button(text="Download MP4")
        btn_mp4.bind(on_press=self.download_mp4)
        layout.add_widget(btn_mp4)
        
        btn_3gp = Button(text="Convert & Download 3GP")
        btn_3gp.bind(on_press=self.download_3gp)
        layout.add_widget(btn_3gp)
        
        return layout

    def download_mp4(self, instance):
        url = self.url_input.text
        if url:
            cmd = f'yt-dlp -f "best[ext=mp4]/best" "{url}" -o "/sdcard/Download/%(title)s.mp4"'
            subprocess.Popen(cmd, shell=True)
            self.label.text = "MP4 ডাউনলোড শুরু হয়েছে..."

    def download_3gp(self, instance):
        url = self.url_input.text
        if url:
            cmd = f'yt-dlp -f "worst" "{url}" -o "temp.mp4" && ffmpeg -i temp.mp4 -s 176x144 -r 15 -b:v 120k -acodec amr_nb -ar 8000 -ac 1 -ab 12.2k "/sdcard/Download/video.3gp" && rm temp.mp4'
            subprocess.Popen(cmd, shell=True)
            self.label.text = "3GP কনভার্ট ও ডাউনলোড শুরু হয়েছে..."

if __name__ == "__main__":
    DownloaderApp().run()
      
