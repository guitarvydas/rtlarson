import py0d as zd


def install (reg):
    zd.register_component (reg, zd.Template ("Reverser", None, instantiator))


reverser_state = "J"
def handler (eh, msg):
    global reverser_state
    if reverser_state == "K":
        if msg.port == "J":
            zd.send_bang (eh, "", msg)
            reverser_state = "J"
        else:
            pass
    elif reverser_state == "J":
        if msg.port == "K":
            zd.send_bang (eh, "", msg)
            reverser_state = "K"
        else:
            pass
def instantiator (reg, owner, name, template_data):
    name_with_id = zd.gensym ("Reverser")
    return zd.make_leaf (name_with_id, owner, None, handler)

