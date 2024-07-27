counter = 0

def gensym (s):
    global counter
    name_with_id = f"{s}{subscripted_digit (counter)}"
    counter += 1
    return name_with_id
    
class Datum:
  def __init__(self):
    self.data = None
    self.clone = None
    self.reclaim = None
    self.srepr = None
    self.kind = None
    self.raw = None

