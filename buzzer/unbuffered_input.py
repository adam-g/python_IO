import sys
from select import select
import tty
import termios

try:
    # more correct to use monotonic time where available ...
    from time33 import clock_gettime
    def time(): return clock_gettime(0)
except ImportError:
    # ... but plain old 'time' may be good enough if not.
    from time import time
  
def input_with():
    """Read an input from the user or timeout"""
    sys.stdout.flush()

    # store terminal settings
    old_settings = termios.tcgetattr(sys.stdin)
    try:    
        tty.setcbreak(sys.stdin) # flush per-character
        c = sys.stdin.read(1)
    finally:
        # put terminal back the way it was
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    if c:
        return c.replace('\n','').strip()
    else:
        return 'q'
