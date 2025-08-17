from models.application import Application
from typing import List, Optional, Tuple, Dict
import datetime as dt

class ApplicationRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self) -> List[Application]:
        with self.db.cursor() as cur:
            cur.execute("SELECT * FROM application_tracking ORDER BY id")
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            return [Application(**dict(zip(columns, row))) for row in rows]

    def insert(self, app: Application):
        with self.db.cursor() as cur:
            cur.execute("""
                INSERT INTO application_tracking (
                    job_title, company, application_software, job_notes,
                    follow_up_contact_name, follow_up_contact_details
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                app.job_title, app.company, app.application_software, app.job_notes,
                app.follow_up_contact_name, app.follow_up_contact_details
            ))
        self.db.commit()

    def update_status(self, app_id: int, new_status: str):
        with self.db.cursor() as cur:
            cur.execute("""
                UPDATE application_tracking
                SET application_status = %s
                WHERE id = %s
            """, (new_status, app_id))
        self.db.commit()