from app.database import engine
from app.models.base import Base

# Importe todos os modelos
from app.models import company, agent, company_config, theme, role

print("🔧 Criando tabelas...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso.")
