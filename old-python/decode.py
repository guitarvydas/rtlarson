import py0d as zd


def install (reg):
    zd.register_component (reg, zd.Template ("Decode", None, instantiator))

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def handler (eh, msg):
    global digits
    i = int (msg.datum.raw ())
    if i >= 0 and i <= 9:
        zd.send_string (eh, digits[i], digits[i], msg)
    zd.send_bang (eh, "done", msg)

def instantiator (reg, owner, name, template_data):
    name_with_id = zd.gensymbol ("Decode")
    return zd.make_leaf (name_with_id, owner, None, handler)

