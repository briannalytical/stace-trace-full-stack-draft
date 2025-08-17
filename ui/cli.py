class CliView:
    @staticmethod
    def intro():
        print("📋 Welcome to Stack Trace Job Application Tracker!")

    @staticmethod
    def main_menu():
        print("\nOptions:")
        print("VIEW - View applications")
        print("ENTER - Enter new application")
        print("UPDATE - Update status")
        print("TASKS - View tasks")
        print("BYE - Exit")

    @staticmethod
    def ask(prompt: str) -> str:
        return input(prompt).strip()