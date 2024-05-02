import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app

    """ __name__ description
        __name__ is the name of the current Python 
        module. The app needs to know where it's located 
        to set up some paths, and __name__ is a convenient 
        way to tell it that.
    """

    """ instance_relative_config description

        instance_relative_config=True tells the app that configuration 
        files are relative to the instance folder. The instance 
        folder is located outside the flaskr package and can hold local 
        data that shouldn't be committed to version control, such as 
        configuration secrets and the database file.
    """
    app = Flask(__name__, instance_relative_config=True)

    """ app.config.from_mapping() description

        app.config.from_mapping() sets some default configuration that the app will use:

            SECRET_KEY is used by Flask and extensions 
            to keep data safe. It's set to 'dev' to 
            provide a convenient value during development, 
            but it should be overridden with a random value 
            when deploying.

            DATABASE is the path where the SQLite 
            database file will be saved. It's under 
            app.instance_path, which is the path that 
            Flask has chosen for the instance folder. 
            You'll learn more about the database in 
            the next section.
    """
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'techconnect.sqlite'),
    )

    """ app.config.from_pyfile() desc
        app.config.from_pyfile() overrides the default 
        configuration with values taken from the config.py 
        file in the instance folder if it exists. For 
        example, when deploying, this can be used to set
        a real SECRET_KEY.
    """

    """ test_config desc
        test_config can also be passed to the factory, 
        and will be used instead of the instance 
        configuration. This is so the tests you'll 
        write later in the tutorial can be configured 
        independently of any development values you have 
        configured.
    """
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    """ os.makedirs() desc
        os.makedirs() ensures that app.instance_path 
        exists. Flask doesn't create the instance folder 
        automatically, but it needs to be created because 
        your project will create the SQLite database file there.
    """
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass  

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import interests
    app.register_blueprint(interests.bp)

    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    return app