from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://admin:KanishMohariya27$@database-1.c3q48e8q683x.ap-south-1.rds.amazonaws.com/5_cent_career?charset=utf8mb4",                 
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))
        
        jobs = []
        
        for row in result.all():
            jobs.append(row._asdict())
        
        return jobs