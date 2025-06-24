from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform

class AlarmApp(App):
    #load app UI
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Play Alarm Sound at Full Volume', font_size=24)
        btn.bind(on_press=self.play_alarm)
        layout.add_widget(btn)
        return layout

    #plays alarm sound
    def play_alarm(self, instance):
        if platform == 'android':
            self.play_android_alarm()
        else:
            self.play_generic_alarm()

    #android specific code to play alarm sound at max volume
    def play_android_alarm(self):
        from jnius import autoclass

        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        activity = PythonActivity.mActivity

        Context = autoclass('android.content.Context')
        AudioManager = autoclass('android.media.AudioManager')

        audio_service = activity.getSystemService(Context.AUDIO_SERVICE)
        #set volume to max for media stream
        max_volume = audio_service.getStreamMaxVolume(AudioManager.STREAM_MUSIC)
        audio_service.setStreamVolume(AudioManager.STREAM_MUSIC, max_volume, 0)

        #play alarm.mp3 at max app volume
        self.play_generic_alarm()

    #sets volume to max and plays alarm sound
    def play_generic_alarm(self):
        from kivy.core.audio import SoundLoader
        sound = SoundLoader.load('alarm.mp3')
        if sound:
            sound.volume = 1.0
            sound.play()

#actually load and run app
if __name__ == '__main__':
    AlarmApp().run()
