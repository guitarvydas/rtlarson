import py0d as zd


def install (reg):
    zd.register_component (reg, zd.Template ("👀", None, instantiator))

def instantiator (reg, owner, name, template_data):      
    name_with_id = zd.gensym ("?")
    return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=handler)

def handler (eh, msg):
    s = msg.datum.srepr ()
    i = int (s)
    while i > 0:
        print (" ", end='')
        i -= 1
    print (f"{s}")

