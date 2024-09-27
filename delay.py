import py0d as zd


def install (reg):
    zd.register_component (reg, zd.Template ("Delay", None, instantiator))

                           
class Delay_Info:
    def __init__ (self, counter=0, saved_message=None):
        self.counter = counter
        self.saved_message = saved_message

def instantiator (reg, owner, name, template_data):
    name_with_id = zd.gensym ("delay")
    info = Delay_Info ()
    return zd.make_leaf (name_with_id, owner, info, handler)

DELAYDELAY = 50000

def first_time (m):
    return not zd.is_tick (m)

def handler (eh, msg):
    info = eh.instance_data
    if first_time (msg):
        info.saved_message = msg
        zd.set_active (eh) ## tell engine to keep running this component with 'ticks'
    count = info.counter
    count += 1
    if count >= DELAYDELAY:
        zd.set_idle (eh) ## tell engine that we're finally done
        zd.forward (eh=eh, port="", msg=info.saved_message)
        count = 0
    info.counter = count


