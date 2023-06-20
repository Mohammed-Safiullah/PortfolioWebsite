from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
)
app.config.from_prefixed_env()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit_form", methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'FORM SUBMITTED, I WILL GET BACK TO YOU SHORTLY'
            return render_template('thankyou.html', message=message)
        except:
            message = 'DID NOT SAVE TO DATABASE'
            return render_template('thankyou.html', message=message)

    else:
        message = 'FORM NOT SUBMITTED'
        return render_template('thankyou.html', message=message)


@app.route("/<string:page_name>")
def page(page_name = '/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')
    
def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email, subject, message])

    

    

    