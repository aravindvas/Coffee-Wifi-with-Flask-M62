from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mynameisvas'
Bootstrap(app)


class CafeForm(FlaskForm):
    cf = StringField('Cafe name', validators=[DataRequired()])
    loc = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    opn = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    cls = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    crat = SelectField("Coffee Rating", choices=["☕", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wrat = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    prat = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    sbt = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("csv2.csv", mode="a", encoding="utf-8") as csvf:
            csvf.write(f"\n{form.cf.data},"
                           f"{form.loc.data},"
                           f"{form.opn.data},"
                           f"{form.cls.data},"
                           f"{form.crat.data},"
                           f"{form.wrat.data},"
                           f"{form.prat.data}")
        return redirect(url_for('caf'))
    return render_template('add.html', frm=form)


@app.route('/cafes')
def caf():
    with open('csv2.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    # print(list_of_rows)
    return render_template('cafes.html', lcafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
