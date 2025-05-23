from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from app.database.session import Base


class Frase(Base):
    __tablename__ = "frases"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    phrase = Column(String(255), nullable=False)
    author = Column(String(100))
    is_sent = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default='CURRENT_TIMESTAMP')
