from api import app,db

with app.app_context(): #creates the database
    db.create_all()
