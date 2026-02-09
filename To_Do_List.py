import json
import os
from datetime import datetime

class ToDoList:
    
    def __init__(self):
        self.filename = 'tasks.json'
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except:
                return []
        return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self):
        print("\n" + "="*50)
        print("➕ ADD NEW TASK")
        print("="*50)
        
        title = input("\n📝 Task title: ").strip()
        if not title:
            print("❌ Task title cannot be empty!")
            return
        
        print("\n🎯 Priority Level:")
        print("   1. High 🔴")
        print("   2. Medium 🟡")
        print("   3. Low 🟢")
        
        priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
        priority_choice = input("\nSelect priority (1-3): ")
        priority = priority_map.get(priority_choice, 'Medium')
        
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'priority': priority,
            'completed': False,
            'created_date': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        
        self.tasks.append(task)
        self.save_tasks()
        
        print(f"\n✅ Task added successfully! (ID: {task['id']})")
    
    def view_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks yet! Add your first task.")
            return
        
        print("\n" + "="*70)
        print("📋 YOUR TO-DO LIST")
        print("="*70)
        
        pending = [t for t in self.tasks if not t['completed']]
        completed = [t for t in self.tasks if t['completed']]
        
        if pending:
            print("\n🔄 PENDING TASKS:")
            print("-"*70)
            for task in pending:
                priority_emoji = {'High': '🔴', 'Medium': '🟡', 'Low': '🟢'}
                emoji = priority_emoji.get(task['priority'], '⚪')
                print(f"ID: {task['id']:3} | {emoji} {task['priority']:6} | {task['title']}")
                print(f"         Created: {task['created_date']}")
                print("-"*70)
        
        if completed:
            print("\n✅ COMPLETED TASKS:")
            print("-"*70)
            for task in completed:
                print(f"ID: {task['id']:3} | ✓ {task['title']}")
                print("-"*70)
        
        print(f"\nTotal: {len(pending)} pending, {len(completed)} completed")
    
    def complete_task(self):
        if not self.tasks:
            print("\n📭 No tasks to complete!")
            return
        
        self.view_tasks()
        
        try:
            task_id = int(input("\n✓ Enter task ID to mark as complete: "))
            
            for task in self.tasks:
                if task['id'] == task_id:
                    if task['completed']:
                        print(f"\n⚠️  Task '{task['title']}' is already completed!")
                    else:
                        task['completed'] = True
                        task['completed_date'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                        self.save_tasks()
                        print(f"\n🎉 Congrats! Task '{task['title']}' completed!")
                    return
            
            print(f"\n❌ Task ID {task_id} not found!")
            
        except ValueError:
            print("\n❌ Please enter a valid task ID!")
    
    def delete_task(self):
        """Delete a task"""
        if not self.tasks:
            print("\n📭 No tasks to delete!")
            return
        
        self.view_tasks()
        
        try:
            task_id = int(input("\n🗑️  Enter task ID to delete: "))
            
            for i, task in enumerate(self.tasks):
                if task['id'] == task_id:
                    confirm = input(f"\n⚠️  Delete '{task['title']}'? (y/n): ").lower()
                    if confirm == 'y':
                        deleted_task = self.tasks.pop(i)
                        self.save_tasks()
                        print(f"\n🗑️  Task '{deleted_task['title']}' deleted!")
                    else:
                        print("\n❌ Deletion cancelled.")
                    return
            
            print(f"\n❌ Task ID {task_id} not found!")
            
        except ValueError:
            print("\n❌ Please enter a valid task ID!")
    
    def view_statistics(self):
        if not self.tasks:
            print("\n📭 No tasks yet!")
            return
        
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t['completed'])
        pending = total - completed
        
        high = sum(1 for t in self.tasks if t['priority'] == 'High' and not t['completed'])
        medium = sum(1 for t in self.tasks if t['priority'] == 'Medium' and not t['completed'])
        low = sum(1 for t in self.tasks if t['priority'] == 'Low' and not t['completed'])
        
        completion_rate = (completed / total) * 100 if total > 0 else 0
        
        print("\n" + "="*50)
        print("📊 TASK STATISTICS")
        print("="*50)
        print(f"\n📌 Total Tasks: {total}")
        print(f"✅ Completed: {completed}")
        print(f"🔄 Pending: {pending}")
        print(f"\n🔴 High Priority: {high}")
        print(f"🟡 Medium Priority: {medium}")
        print(f"🟢 Low Priority: {low}")
        print(f"\n📈 Completion Rate: {completion_rate:.1f}%")
        
        bar_length = 30
        filled = int(bar_length * completion_rate / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\n[{bar}] {completion_rate:.1f}%")
        print("="*50)
    
    def search_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks to search!")
            return
        
        keyword = input("\n🔍 Enter search keyword: ").strip().lower()
        
        results = [t for t in self.tasks if keyword in t['title'].lower()]
        
        if not results:
            print(f"\n❌ No tasks found containing '{keyword}'")
            return
        
        print(f"\n🔍 Found {len(results)} task(s) containing '{keyword}':")
        print("-"*70)
        for task in results:
            status = "✅" if task['completed'] else "🔄"
            print(f"ID: {task['id']:3} | {status} | {task['title']}")
            print(f"         Priority: {task['priority']} | Created: {task['created_date']}")
            print("-"*70)


def display_menu():
    print("="*48 )
    print(" "*15 + "SMART TO-DO LIST" + " "*15)
    print("="*48 )
    print("\n📝 MENU OPTIONS:")
    print("   1. ➕ Add New Task")
    print("   2. 📋 View All Tasks")
    print("   3. ✅ Complete Task")
    print("   4. 🗑️  Delete Task")
    print("   5. 📊 View Statistics")
    print("   6. 🔍 Search Tasks")
    print("   7. 🚪 Exit")


def main():
    todo = ToDoList()
    
    print("\n" + "🎯"*20)
    print("Welcome to Smart To-Do List Manager!")
    print("Stay organized and productive! 🚀")
    print("🎯"*20)
    
    while True:
        display_menu()
        
        choice = input("\n👉 Enter your choice (1-7): ").strip()
        
        if choice == '1':
            todo.add_task()
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.complete_task()
        elif choice == '4':
            todo.delete_task()
        elif choice == '5':
            todo.view_statistics()
        elif choice == '6':
            todo.search_tasks()
        elif choice == '7':
            print("\n👋 Thanks for using Smart To-Do List!")
            print("🎯 Stay productive! Goodbye! 🚀\n")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-7.")
        
        input("\n⏸️  Press Enter to continue...")


if __name__ == "__main__":
    main()