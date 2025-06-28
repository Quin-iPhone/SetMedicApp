from flask import Flask, render_template
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev')

# Load config from env.txt or environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///setmedic.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db
from models import invoice  # Ensure models are loaded

db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints
from routes.invoices import invoices_bp
from routes.quotes import quotes_bp

app.register_blueprint(invoices_bp)
app.register_blueprint(quotes_bp)

@app.route('/')
def home():
return render_template('index.html')

# If you want to define a simple quotes route directly in app.py, you can do so here, but it's better to use the blueprint.
# @app.route('/quotes')
# def quotes():
#     return render_template('quotes/list.html')

if __name__ == '__main__':
app.run(debug=True)
