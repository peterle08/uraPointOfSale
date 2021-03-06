from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(id):
    """Query a user model by identifier

    Parameters:
        id: The user model identifier to query

    Returns:
        A user model
    """
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    """User model

    UserMixin
    db.Model

    Attributes:
        id:            The unique user identifier
        username:      The user name
        email:         The user email address
        creation_date: The user creation date and time
        password_hash: The user password hash
        country:       The user country code
        time_zone:     The user time zone
        user_notes:    The relationship to query all notes authored by this user
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True, unique=True)
    email = db.Column(db.String, index=True, unique=True)
    creation_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    country = db.Column(db.String, default='United States')
    time_zone = db.Column(db.String, default='America/New_York')
    user_notes = db.relationship('Note', backref='author', lazy='dynamic')

    def __repr__(self):
        """String representation of a user model

        Parameters:
            self: The user model

        Returns:
            A user model string identifier
        """
        return '<User: {}>'.format(self.username)

    def set_password(self, password):
        """Set the password hash generated with a plaintext password

        Parameters:
            self:     The user model
            password: The plaintext password used to generate the password hash
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check a plain text password generates the same password hash as the user model

        Parameters:
            self:     The user model
            password: The plaintext password used to generate the password hash check

        Returns:
            true:  The password hash generated from the plaintext password matches the user model password hash
            false: The password hash generated from the plaintext password does not match the user model password hash
        """
        return check_password_hash(self.password_hash, password)

class Tag(db.Model):
    """Tag model
    
    db.Model
    
    Attributes:
        id:    The tag identifier
        tag:   The name of the tage
        notes: The relationship of notes to this tag
    """
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String, index=True)
    notes = db.relationship('NoteTags', back_populates='tag')

    def __repr__(self):
        """String representation of a tag model

        Parameters:
            self: The tag model

        Returns:
            A tag model string identifier
        """
        return '<Tag: {}>'.format(self.tag)

class Note(db.Model):
    """Note model

    db.Model

    Attributes:
        id:               The unique note identifier
        user_id:          The user identifier of the author of the note
        title:            The note title
        note:             The note contents
        note_date:        The note creation date and time
        last_edited:      The UTC timestamp of the change to the note
        reminder_date:    The note reminder date and time if present
        already_reminded: Whether the reminder was already triggered
        tags:             The relationship for all tags associated with this note
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String, index=True)
    note = db.Column(db.String, index=True)
    note_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_edited = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reminder_date = db.Column(db.DateTime, index=True, nullable=True)
    already_reminded = db.Column(db.Boolean, index=True, default=False)
    tags = db.relationship('NoteTags', back_populates='note')

    def __repr__(self):
        """String representation of a note model

        Parameters:
            self: The note model

        Returns:
            A note model string identifier
        """
        return '<Note: {}>'.format(self.note)

class NoteTags(db.Model):
    """NoteTags model
    
    db.Model
    
    Attributes:
        note_id: The note identifier
        tag_id:  The tag identifier
        tag:     The relationship to the tag associated with the note
        note:    The relationship to the note associate with the tag
    """
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
    tag = db.relationship('Tag', back_populates='notes')
    note = db.relationship('Note', back_populates='tags')

