import psycopg2
import logging
import time
from src.config import settings

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

def init_db():
    try:
        # Connect to defaultdb to create tasktango database if it doesn't exist
        default_dsn = settings.DATABASE_URL.replace("/tasktango", "/defaultdb")
        conn = psycopg2.connect(default_dsn)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS tasktango")
        logger.info("Ensured tasktango database exists")
        cur.close()
        conn.close()

        # Connect to tasktango database to create tables
        for attempt in range(3):
            try:
                conn = psycopg2.connect(settings.DATABASE_URL)
                conn.autocommit = True
                cur = conn.cursor()
                cur.execute("""
                    CREATE SEQUENCE IF NOT EXISTS user_id_seq START 1;
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY DEFAULT nextval('user_id_seq'),
                        username VARCHAR(50) UNIQUE NOT NULL,
                        hashed_password VARCHAR(255) NOT NULL
                    );
                    CREATE SEQUENCE IF NOT EXISTS task_id_seq START 1;
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY DEFAULT nextval('task_id_seq'),
                        title VARCHAR(255) NOT NULL,
                        description TEXT,
                        completed BOOLEAN DEFAULT FALSE,
                        user_id INTEGER,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                    )
                """)
                logger.info("Database initialized successfully")
                cur.close()
                conn.close()
                break
            except psycopg2.OperationalError as e:
                logger.warning(f"Connection attempt {attempt + 1} failed: {str(e)}")
                time.sleep(2)
                if attempt == 2:
                    raise
    except psycopg2.Error as e:
        logger.error(f"Database error during initialization: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during database initialization: {str(e)}")
        raise

def get_db():
    conn = psycopg2.connect(settings.DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()