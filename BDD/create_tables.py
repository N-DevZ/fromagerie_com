from database import engine, Base

Base.metadata.create_all(bind=engine)

print("Tables créées avec succès dans la base de données MySQL")
