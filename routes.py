from flask import render_template

class Routes:

    @staticmethod
    def initRoutes(app):

        @app.route('/')
        def index():
            return render_template('index.html')
        
        return app