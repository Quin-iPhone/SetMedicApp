from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

# Dummy data for services and blog posts
services = [
    {"id": 1, "name": "On-Set Medic", "description": "Certified medical professionals for film and TV sets.", "price": 150},
    {"id": 2, "name": "Event Medical Support", "description": "Medical standby for public and private events.", "price": 200},
    {"id": 3, "name": "Risk Assessment", "description": "Pre-production safety and health evaluations.", "price": 100}
]

posts = [
    {"id": 1, "title": "Why Every Set Needs a Medic", "snippet": "Safety is not optional on set...", "date": "2025-06-01", "content": "Full article content here."},
    {"id": 2, "title": "Event Safety Tips", "snippet": "Planning an event? Here's what to consider...", "date": "2025-06-10", "content": "Full article content here."}
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services_page():
    return render_template('services.html', services=services)

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        invoice = {
            "invoice_number": "INV20250617",
            "name": request.form['name'],
            "company": request.form['company'],
            "service": next((s for s in services if str(s["id"]) == request.form['service']), None),
            "total_amount": next((s["price"] for s in services if str(s["id"]) == request.form['service']), 0)
        }
        return render_template('invoice.html', invoice=invoice)
    return render_template('quote.html', services=services)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    invoice = {
        "invoice_number": "INV20250617",
        "total_amount": 150
    }
    if request.method == 'POST':
        receipt = {
            "receipt_number": "RCPT20250617",
            "name": "John Doe",
            "company": "Set Medic App",
            "service": {"name": "On-Set Medic"},
            "total_amount": invoice["total_amount"]
        }
        return render_template('receipt.html', receipt=receipt)
    return render_template('payment.html', invoice=invoice)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)

@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template('blog_detail.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
Save the corrected app.py file for the Set Medic App Flask project
app_py_content = """

# Write the content to app.py
with open('app.py', 'w') as f:
    f.write(app_py_content)

# Create a zip package with the updated app.py
import zipfile

with zipfile.ZipFile('set_medic_app.zip', 'w') as zipf:
    zipf.write('app.py')
    for root, dirs, files in os.walk('templates'):
        for file in files:
            zipf.write(os.path.join(root, file))

print("The app.py file has been saved and the deployment package has been updated.")