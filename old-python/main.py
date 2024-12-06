import py0d as zd

[palette, env] = zd.initialize ()

import delay, count, reverser, decode, monitor
delay.install (palette)
count.install (palette)
reverser.install (palette)
decode.install (palette)
monitor.install (palette)

zd.start (palette, env)
