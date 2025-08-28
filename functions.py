from datetime import datetime, timedelta
from db import SessionLocal
from models import User, Habit, HabitLog

session = SessionLocal()

# --- Functions ---

def add_user():
    username = input("Enter username: ").strip()
    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f"👋 User '{username}' already exists!")
        return user
    user = User(username=username)
    session.add(user)
    session.commit()
    print(f"✅ User '{username}' created!")
    return user

def add_habit(user):
    name = input("Enter habit name: ").strip()
    frequency = input("Enter frequency (daily/weekly/etc): ").strip()
    habit = Habit(name=name, frequency=frequency, user=user)
    session.add(habit)
    session.commit()
    print(f"✅ Habit '{name}' added for {user.username}")

def log_habit(user):
    habits = session.query(Habit).filter_by(user_id=user.id).all()
    if not habits:
        print("❌ No habits to log.")
        return
    print("Select a habit to log:")
    for i, h in enumerate(habits, 1):
        print(f"{i}. {h.name}")
    choice = int(input("Enter number: ")) - 1
    if 0 <= choice < len(habits):
        log = HabitLog(habit=habits[choice], user=user, date=datetime.utcnow())
        session.add(log)
        session.commit()
        print(f"✅ Logged habit '{habits[choice].name}'")
    else:
        print("❌ Invalid choice.")

def show_habits(user):
    habits = session.query(Habit).filter_by(user_id=user.id).all()
    if not habits:
        print("❌ No habits found.")
        return
    print(f"\nHabits for {user.username}:")
    for h in habits:
        print(f"- {h.name} ({h.frequency})")

def show_streak():
    habit_id = int(input("Enter habit ID to see streak: "))
    habit = session.query(Habit).get(habit_id)
    if not habit or not habit.logs:
        print("❌ No logs for this habit.")
        return
    logs = sorted([log.date.date() for log in habit.logs])
    streak = 1
    best_streak = 1
    for i in range(1, len(logs)):
        if logs[i] == logs[i-1] + timedelta(days=1):
            streak += 1
            best_streak = max(best_streak, streak)
        else:
            streak = 1
    print(f"Current streak: {streak} days | Best streak: {best_streak} days")

def show_all_habits():
    habits = session.query(Habit).all()
    if not habits:
        print("❌ No habits found.")
        return
    print("\nAll habits:")
    for h in habits:
        print(f"{h.id}. {h.name} (User: {h.user.username}, Frequency: {h.frequency})")
