from __future__ import annotations
import psycopg2
from typing import Optional
from config import Config

class Db:
    """Lightweight psycopg2 connection manager."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.conn: Optional[psycopg2.extensions.connection] = None

    def connect(self) -> None:
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(
                dbname=self.cfg.DB_NAME,
                user=self.cfg.DB_USER,
                password=self.cfg.DB_PASSWORD,
                host=self.cfg.DB_HOST,
                port=self.cfg.DB_PORT,
            )
            self.conn.autocommit = False

    def cursor(self):
        self.connect()
        return self.conn.cursor()

    def commit(self) -> None:
        if self.conn:
            self.conn.commit()

    def rollback(self) -> None:
        if self.conn:
            self.conn.rollback()

    def close(self) -> None:
        if self.conn:
            self.conn.close()
            self.conn = None