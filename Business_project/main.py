from task import Project
from utils import validate_date

def main():
    print("🚀 Welcome to ProjectNest – Business Productivity CLI")
    project_name = input("Enter your project name: ")
    project = Project(project_name)

    while True:
        print("\n📋 Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Show Progress")
        print("5. Filter Tasks")
        print("6. Exit")

        choice = input("Choose an option (1–6): ").strip()

        if choice == '1':
            desc = input("Task description: ")
            due = input("Due date (YYYY-MM-DD): ")
            if not validate_date(due):
                print("❌ Invalid date format. Use YYYY-MM-DD.")
                continue
            priority = input("Priority (Low/Medium/High): ").capitalize()
            if priority not in ["Low", "Medium", "High"]:
                print("❌ Invalid priority. Choose Low, Medium, or High.")
                continue
            project.add_task(desc, due, priority)
            print("✅ Task added.")

        elif choice == '2':
            project.list_tasks()

        elif choice == '3':
            project.list_tasks()
            if not project.tasks:
                continue
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                project.mark_task_done(index)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '4':
            progress = project.show_progress()
            print(f"📊 Project is {progress}% complete.")

        elif choice == '5':
            print("\n🔎 Filter Options:")
            print("1. Incomplete Tasks")
            print("2. Completed Tasks")
            print("3. By Priority")
            print("4. Due Today")
            filter_choice = input("Choose filter (1–4): ").strip()

            if filter_choice == "1":
                project.filter_tasks(status="incomplete")
            elif filter_choice == "2":
                project.filter_tasks(status="complete")
            elif filter_choice == "3":
                pr = input("Enter priority (Low/Medium/High): ").capitalize()
                project.filter_tasks(priority=pr)
            elif filter_choice == "4":
                project.filter_tasks(due_today=True)
            else:
                print("❌ Invalid filter option.")

        elif choice == '6':
            print("👋 Goodbye! Keep being productive!")
            break

        else:
            print("❌ Invalid choice. Please pick 1–6.")


if __name__ == "__main__":
    main()
