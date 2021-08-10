from app import create_app,db

    app = create_app('prod')
    with app.app_context():
        db.create_all()

    app.run()