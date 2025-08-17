from dataclasses import dataclass
import datetime as dt
from typing import Optional

@dataclass
class Application:
    id: Optional[int]
    job_title: Optional[str]
    company: Optional[str]
    application_status: Optional[str]
    application_software: Optional[str]
    job_notes: Optional[str]
    follow_up_contact_name: Optional[str]
    follow_up_contact_details: Optional[str]
    next_action: Optional[str]
    check_application_status: Optional[dt.date]
    next_follow_up_date: Optional[dt.date]
    interview_date: Optional[dt.date]
    interview_time: Optional[dt.time]
    interviewer_name: Optional[str]
    interview_prep_notes: Optional[str]
    second_interview_date: Optional[dt.date]
    final_interview_date: Optional[dt.date]