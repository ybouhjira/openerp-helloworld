from osv import osv, fields 

class Book(osv.Model) :
  """ A book """

  _name = 'helloworld.book'
  
  _columns = {
    'isbn' : fields.char(
      string = 'ISBN',
      size = 9,
      required = True
    ),
    'title' : fields.char(
      string = 'Title', 
      size = 100,
      required = True
    ),
    'author_id' : fields.many2one(
      obj = 'helloworld.author',
      string = 'Author',
      required = True
    )
  }

  _sql_constraints = [
    ('unique_isbn', 'unique(isbn)', 'The ISBN must be unique'),
    ('unique_title', 'unique(title)', 'The title must be unique')
  ] 