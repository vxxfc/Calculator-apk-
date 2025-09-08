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

# (str) Versioning
version = 0.1

# (str) Application versioning (method 1)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
# You can add more (e.g. "numpy, kivy[base]")
requirements = python3,kivy

# (str) Supported orientations: landscape, portrait or all
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions (if needed, else keep empty)
android.permissions = INTERNET

# ✅ Force Buildozer to use the preinstalled SDK/NDK (matches workflow)
android.sdk_path = /usr/lib/android-sdk
android.ndk_path = /usr/lib/android-sdk/ndk/21.4.7075529

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Target API (must match one installed via sdkmanager in workflow)
android.api = 31

# (int) Build-tools version (must match workflow)
android.build_tools = 33.0.2

# (bool) Copy library instead of making a libpymodules.so
# Use this if you hit issues with loading modules
# android.copy_libs = 1

# (list) Presplash and icon images (optional)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# (str) Supported architectures
# You can add arm64-v8a, x86 if needed
android.archs = armeabi-v7a

# (str) Entry point
entrypoint = main.py

# (str) Python for android branch to use
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
