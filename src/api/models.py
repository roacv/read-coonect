from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # follow_user_id = db.Column(
    #     db.Integer, db.ForeignKey("follows_users.id_follow"))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    img = db.Column(db.String(200), unique=False, nullable=True)
    follows = db.relationship('Follow_user', backref='user')
    reads = db.relationship('Read_usuer', backref='user')
    xreads = db.relationship('Xread_usuer', backref='user')
    ranks = db.relationship('Rank_book', backref='user')
    reviews = db.relationship('Review_book', backref='user')

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "img": self.img,
            # do not serialize the password, its a security breach
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)


class Follow_user(db.Model):
    __tablename__ = 'follows_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    id_follow = db.Column(db.Integer, nullable=False)
    # user = db.relationship('User', backref='follows_users')

    def __repr__(self):
        return f'<User {self.id_user}>'

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.user_id,
            "id_follor": self.id_follow,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    isbn = db.Column(db.String(120), unique=True, nullable=False)
    pageCount = db.Column(db.Integer)
    publishedDate = db.Column(db.DateTime)
    thumbnailUrl = db.Column(db.String(200), unique=True, nullable=False)
    shortDescription = db.Column(db.Text)
    longDescription = db.Column(db.Text)
    status = db.Column(db.String(50))
    authors = db.Column(db.String(200))
    categories = db.Column(db.String(300))

    def __repr__(self):
        return f'<Book {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "isbn": self.isbn,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)


class Read_usuer(db.Model):
    __tablename__ = 'reads_users'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer,
                        db.ForeignKey("users.id"), primary_key=True)
    id_book = db.Column(db.Integer,
                        db.ForeignKey("books.id"), primary_key=False)

    def __repr__(self):
        return f'<Id_User {self.id_user}>'

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_book": self.id_book
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)


class Xread_usuer(db.Model):
    __tablename__ = 'xread_user'
    id_user = db.Column(db.Integer,
                        db.ForeignKey("users.id"), primary_key=True)
    id_book = db.Column(db.Integer,
                        db.ForeignKey("books.id"), primary_key=False)

    def __repr__(self):
        return f'<Id_User {self.id_user}>'

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_book": self.id_book
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)


class Rank_book(db.Model):
    __tablename__ = 'rank_book'
    id_user = db.Column(db.Integer,
                        db.ForeignKey("users.id"), primary_key=True)
    id_book = db.Column(db.Integer,
                        db.ForeignKey("books.id"), primary_key=False)
    rank = db.Column(db.Integer)

    def __repr__(self):
        return f'<Id_User {self.id_user}>'

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_book": self.id_book,
            "rank": self.rank,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)


class Review_book(db.Model):
    __tablename__ = 'review_book'
    id_user = db.Column(db.Integer,
                        db.ForeignKey("users.id"), primary_key=True)
    id_book = db.Column(db.Integer,
                        db.ForeignKey("books.id"), primary_key=False)
    review = db.Column(db.Text(), unique=False, nullable=True)

    def __repr__(self):
        return f'<Id_User {self.id_user}>'

    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_book": self.id_book,
            "rank": self.review,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.add(self)
