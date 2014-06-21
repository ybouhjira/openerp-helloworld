from osv import osv, fields

class Author(osv.osv):
  """ An author """
  
  _name = 'helloworld.author'

  _columns = {
    'firstName' : fields.char(
      string = 'First name',
      size = 30,
      required = True
    ),
    'lastName' : fields.char(
      string = 'Last name',
      size = 30,
      required = True
    ),
    'book_ids' : fields.one2many(
      obj = 'helloworld.book',
      fields_id = 'author_id',
      string = 'Books'
    )
  }
