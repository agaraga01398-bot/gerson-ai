[app]
title = Gerson AI Studio
package.name = gersonaistudio
package.domain = com.gerson.ai
source.dir =.
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET

[buildozer]
log_level = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
