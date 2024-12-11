from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))
        
        jobs = []
        
        for row in result.all():
            jobs.append(row._asdict())
        
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs WHERE id = :val'), {'val' : id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()