from database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String , Integer


class Logs(Base):
    __tablename__ = 'logs'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    website_url: Mapped[str] = mapped_column(String(50))
    duration: Mapped[int] = mapped_column(Integer)
    error_message: Mapped[str] = mapped_column(String(50),nullable=True)

    class Config:
        orm_mode = True