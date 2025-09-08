[app]
# (str) Title of your application
title = Calculator

# (str) Package name
package.name = calculator

# (str) Package domain (reverse DNS)
package.domain = org.example

# (str) Source code where main.py lives
source.dir = .

# (str) Main Python file
source.main = main.py

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations: landscape, portrait or all
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions (if needed)
android.permissions = INTERNET

# ✅ Use preinstalled SDK/NDK from workflow
android.sdk_path = /usr/lib/android-sdk
android.ndk_path = /usr/lib/android-sdk/ndk/21.4.7075529

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Target API (must match one installed via sdkmanager in workflow)
android.api = 31

# (int) Build-tools version (must match workflow)
android.build_tools = 33.0.2

# (str) Supported architectures
android.archs = armeabi-v7a

# (str) Entry point
entrypoint = main.py

# (str) Python-for-android branch
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
