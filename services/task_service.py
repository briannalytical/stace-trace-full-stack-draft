class TaskService:
    AUTO_STATUS_MAP = {
        'check_application_status': 'interviewing_first_scheduled',
        'follow_up_with_contact': 'interviewing_first_scheduled',
        'send_follow_up_email': 'interviewing_first_followed_up',
        'prepare_for_interview': 'interviewing_first_completed',
        'send_thank_you_email': 'interviewing_first_followed_up',
        'prepare_for_second_interview': 'interviewing_second_completed',
        'send_thank_you_email_second_interview': 'interviewing_second_followed_up',
        'prepare_for_final_interview': 'interviewing_final_completed',
        'send_thank_you_email_final_interview': 'interviewing_final_followed_up',
    }

    def __init__(self, repo):
        self.repo = repo

    def auto_update_status(self, app_id: int, next_action: str, current_status: str) -> str:
        new_status = self.AUTO_STATUS_MAP.get(next_action, current_status)
        if new_status != current_status:
            self.repo.update_status(app_id, new_status)
        return new_status