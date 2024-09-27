import py0d as zd


def install (reg):
    zd.register_component (reg, zd.Template ("Count", None, instantiator))

counter = 0
direction = 1
def handler (eh, msg):
    global counter, direction
    if msg.port == "adv":
        counter = counter + direction
        zd.send_int (eh, "", counter, msg)
    elif msg.port == "rev":
        direction = direction * -1
def instantiator (reg, owner, name, template_data):
    name_with_id = zd.gensym ("Count")
    return zd.make_leaf (name_with_id, owner, None, handler)
