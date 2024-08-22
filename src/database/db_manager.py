
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Content

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def add_user(self, username, email, password_hash):
        session = self.Session()
        new_user = User(username=username, email=email, password_hash=password_hash)
        session.add(new_user)
        session.commit()
        session.close()

    def add_content(self, title, body, author_id):
        session = self.Session()
        new_content = Content(title=title, body=body, author_id=author_id)
        session.add(new_content)
        session.commit()
        session.close()

    def get_user_by_id(self, user_id):
        session = self.Session()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    def get_content_by_id(self, content_id):
        session = self.Session()
        content = session.query(Content).filter(Content.id == content_id).first()
        session.close()
        return content

if __name__ == "__main__":
    db_manager = DatabaseManager("sqlite:///ai_content_generator.db")
    db_manager.create_tables()
    # Add example usage here
