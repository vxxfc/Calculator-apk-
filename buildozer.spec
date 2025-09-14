# buildozer.spec - calculator app
# Put this file at the repo root (next to Main.py)

[app]

# (str) Title of your application
title = Calculator

# (str) Package name (no spaces, lowercase)
package.name = calculator

# (str) Package domain (reverse DNS)
package.domain = org.rev.dovia

# (str) Source code directory (relative)
source.dir = .

# (str) Main Python file (change to main.py if yours is lowercase)
source.main = Main.py

# (str) Application entrypoint (same as main)
entrypoint = Main.py

# (str) Application version
version = 0.1

# (list) Application requirements (python-for-android recipes)
# Add extra libs here if you need them, comma-separated
requirements = python3,kivy

# (str) Supported orientations: landscape, portrait or all
orientation = portrait

# (bool) fullscreen (0 = no, 1 = yes)
fullscreen = 0

# (list) Permissions (keep empty if not needed)
android.permissions = 

# (str) Minimum API your APK will support
android.minapi = 21

# (int) Target API (must match what you install in CI)
android.api = 31

# (str) Build-tools version used by Buildozer/p4a (must match CI)
android.build_tools = 33.0.2

# (str) SDK/NDK paths - FORCE Buildozer to use preinstalled SDK/NDK from CI
android.sdk_path = /home/yourusername/.buildozer/android/platform/android-sdk
android.ndk_path = /usr/lib/android-sdk/ndk/21.4.7075529

# (list) Supported architectures
# include both 32-bit and 64-bit if you want wider support
android.archs = armeabi-v7a, arm64-v8a

# (int) Number of jobs to use in compilation (optional)
# p4a.cpu_count = 2

# (str) Python-for-android branch to use
p4a.branch = master

# (bool) Copy libraries instead of building libpymodules.so (optional)
# android.copy_libs = 1

# (str) Icon / presplash (optional)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# (str) Additional source include patterns (optional)
# source.include_exts = py,png,jpg,kv,atlas
# source.exclude_dirs = tests,docs
# source.include_patterns = assets/*,images/*.png

# (str) Android logcat filters to use (optional)
# android.logcat_filters = *:S python:D

# (str) Signing options (for release builds) - leave commented for debug
# android.release_keystore = /path/to/keystore
# android.release_keyalias = myalias
# android.release_keypass = mypass
# android.release_storepass = storepass

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (bool) Warn when running as root
warn_on_root = 1

# (str) Build dir (optional)
# build_dir = .buildozer

# (int) Copy apk to bin folder after build
copy_to_bin = 1
