from osv import osv, fields

class Message(osv.Model):
  """ A message like 'Hello world' or something """
  
  _name = 'helloworld.message'

  _columns = {
    'content' : fields.char('Content', size=64, required=True, translate=True)
  }