from fastapi import FastAPI
from app.database import engine
from app.models import base, company, agent, company_config, theme, role

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API CRM WhatsApp online."}

def create_tables():
    base.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
