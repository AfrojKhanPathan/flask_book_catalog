from app import create_app,db
from app.auth.model import user
from sqlalchemy import exc

    app = create_app('prod')

    with app.app_context():
        db.create_all()
        try:
            if not User.query.filter_by(user_name="harry").first():
                User.create_user(user='harry',email='harry@pooters.com',password='secret')
        except exc.IntegrityError:
            app.run()