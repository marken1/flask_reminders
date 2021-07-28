import datetime
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for, request
import config
message = ''


def Add_reminder(text, date):
    query = f'INSERT INTO reminders (ID, text, date_add) VALUES (null, "{text}", "{date}")'
    cursor.execute(query)
    config.db_con.commit()
    return message + str('Připomnka byla zapsána')


def Delete_reminder(id):
    query = f'DELETE FROM reminders WHERE ID = "{id}"'
    cursor.execute(query)
    config.db_con.commit()
    return message + str('Připomínka byla odstraněna')


cursor = config.db_con.cursor()
query = 'SELECT * FROM reminders'
cursor.execute(query)
result = cursor.fetchall()
numbering = len(result)
table_headings = ['ID', 'Připomínka', 'Datum dokončení']

for i in result:
    table_data = [i[0], i[1], i[2]]

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        add_form = request.form['add_form']
        del_form = request.form['del_form']
        add_reminder = request.form['add_reminder']
        del_reminder = request.form['del_reminder']
        end_date = request.form['end_date']
        Add_reminder(add_reminder, end_date)
        Delete_reminder(del_reminder)

        print(del_reminder, add_reminder, end_date)
        print(Delete_reminder(del_reminder))

        return redirect(url_for('index'))
    else:
        pass
    return render_template('index.html', table_headings=table_headings, data=result, message=message)


if __name__ == '__main__':
    app.debug = True
    app.run()
