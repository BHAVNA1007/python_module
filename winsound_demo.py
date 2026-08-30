'''
winsound is a built-in Python module for playing sounds on Windows. You don't need to install it with pip.
'''

import winsound 

winsound.Beep(1000, 500)

'''
1000 → frequency in Hertz (Hz) → controls the pitch
500 → duration in milliseconds (ms) → 0.5 seconds
'''