# Lightsync

A repo containing some python scripts that are used for setting the rgb-color of my Logitech Mouse to black.

I use these together with elgato stream deck to have shortcuts for turning of the lights of the mouse when watching films for example.

By running the files `open_black.py`, `kill_black.py` and `toggle_black.py` using `pythonw` with the System > Open in the stream deck you can set the color.


There is also a C# project that increases a number in `cycle.txt`, this was an earlier experiment where I tried to sync the brightness of my Corsair keyboard to the Logitech mouse. I then added, an action where the brightness key ran the compiled C# project. (Needed to compile to .exe to be able to run it from iCUE)
But because I would need to have a python-process running and updating the brightness I didn't really like the solution.

The code is terrible with hard-coded paths everywhere, but it would be fun if you'd want to use this so please add issues and ask for clarification. And I could probably rewrite some of it to work for everyone.
