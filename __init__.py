from osv import osv, fields

class Author(osv.Model):
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

  # _sql_constraints = [
  #   ('unique_isbn', 'unique(isbn)', 'The ISBN must be unique'),
  #   ('unique_title', 'unique(title)', 'The title must be unique')
  # ] 


Author()
Book()