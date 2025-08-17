from config import Config
from db.connection import Db
from repositories.application_repo import ApplicationRepository
from services.task_service import TaskService
from ui.cli_view import CliView
from models.application import Application

def main():
    config = Config()
    db = Db(config)
    repo = ApplicationRepository(db)
    service = TaskService(repo)
    view = CliView()

    view.intro()

    while True:
        view.main_menu()
        choice = view.ask("\nChoice: ").upper()

        if choice == "VIEW":
            apps = repo.get_all()
            for app in apps:
                print(f"{app.id}: {app.job_title} @ {app.company}")
        elif choice == "ENTER":
            job_title = view.ask("Job title: ")
            company = view.ask("Company: ")
            software = view.ask("Platform used: ")
            notes = view.ask("Notes: ")
            contact_name = view.ask("Contact name: ")
            contact_details = view.ask("Contact details: ")
            app = Application(
                id=None,
                job_title=job_title,
                company=company,
                application_status="applied",
                application_software=software,
                job_notes=notes,
                follow_up_contact_name=contact_name,
                follow_up_contact_details=contact_details,
                next_action=None,
                check_application_status=None,
                next_follow_up_date=None,
                interview_date=None,
                interview_time=None,
                interviewer_name=None,
                interview_prep_notes=None,
                second_interview_date=None,
                final_interview_date=None
            )
            repo.insert(app)
            print("✅ Added!")
        elif choice == "BYE":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

    db.close()

if __name__ == "__main__":
    main()