from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    habits = relationship("Habit", back_populates="user")
    logs = relationship("HabitLog", back_populates="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    frequency = Column(String, default="daily")
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="habits")
    logs = relationship("HabitLog", back_populates="habit")

    def __repr__(self):
        return f"<Habit(name={self.name}, frequency={self.frequency})>"


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    habit = relationship("Habit", back_populates="logs")
    user = relationship("User", back_populates="logs")

    def __repr__(self):
        return f"<HabitLog(habit={self.habit_id}, user={self.user_id}, date={self.date})>"
