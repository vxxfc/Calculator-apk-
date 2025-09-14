[app]
title = Calculator
package.name = calculator
package.domain = org.example

# MUST HAVE EITHER version OR version.regex
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy

orientation = portrait

# Android specific
android.api = 34
android.minapi = 24
android.ndk = 23b
