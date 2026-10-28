import sys
from datetime import date
from .io_utils import load_tasks

def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "sample.csv"
    today = date.today()
    
    try:
        tasks = load_tasks(csv_path)
        print(f"Successfully loaded {len(tasks)} tasks:\n")
        
        for task in tasks:
            days = task.days_left(today)
            print(f"- {task.title} (Due: {task.deadline})")
            print(f"  Importance: {task.importance}/5 | Effort: {task.effort_h}h | Days left: {days}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()