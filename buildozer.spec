[app]

title = Calculator
package.name = calculator
package.domain = org.rev.dovia
source.dir = .
source.main = calculator.py
version = 1.0.0

# requirements
requirements = python3,kivy

# orientation
orientation = portrait

# fullscreen (0 = no, 1 = yes)
fullscreen = 0

# permissions (none needed, but internet is safe default)
android.permissions = INTERNET

# entry point
entrypoint = calculator.py

# output format
package.format = apk

[buildozer]

log_level = 2
warn_on_root = 1
copy_to_bin = 1
