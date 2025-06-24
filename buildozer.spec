[app]
title = TTZAlarm
package.name = ttzalarm
package.domain = org.tapstechzone
source.dir = .
source.include_exts = py,kv,flac,mp3,ogg,wav,png,jpg,atlas
version = 0.1
requirements = python3,kivy,ffpyplayer,pyjnius
orientation = portrait
fullscreen = 1
android.permissions = MODIFY_AUDIO_SETTINGS
# Add any other permissions you need

[buildozer]
log_level = 2
warn_on_root = 1
