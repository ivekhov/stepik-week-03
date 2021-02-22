from flask import Flask, render_template, request
import json

WEEKDAYS = {
    'mon': 'Понедельник',
    'tue': 'Вторник',
    'wed': 'Среда',
    'thu': 'Четверг',
    'fri': 'Пятница',
    'sat': 'Суббота',
    'sun': 'Воскресенье',
}

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/all')
def show_all_tutors():
    return render_template("all.html")


@app.route('/goals/<goal>')
def find_goal(goal):
    return render_template("goal.html")


@app.route('/profiles/<profile_id>')
def show_tutor_profile(profile_id):
    with open('data_teachers.json', 'r') as data_file:
        teachers = json.load(data_file)
    return render_template("profile.html", data=teachers[int(profile_id)],
                           weekdays=WEEKDAYS, profile_id=profile_id)


@app.route('/request/')
def make_request():
    return render_template("request.html")


@app.route('/request_done/')
def confirm_request():
    return render_template("request_done.html")


@app.route('/booking/<profile_id>/<weekday>/<time>/')
def reserve_tutor(profile_id, weekday, time):
    with open('data_teachers.json', 'r') as data_file:
        teachers = json.load(data_file)

    # client_name = request.form.get["clientName"]
    # client_phone = request.form.get["clientPhone"]
    # client_time = request.form.get["clientTime"]
    # client_weekday = request.form.get["clientWeekday"]

    # visit = {
    #     'client_name': client_name,
    #     'client_phone': client_phone,
    #     'weekday': client_weekday,
    #     'time': client_time,
    # }
    # with open('booking.json', 'a') as data_file:
    #     json.dump(visit, data_file)


    return render_template("booking.html", data=teachers[int(profile_id)],
                           weekdays=WEEKDAYS, profile_id=profile_id,
                           weekday=weekday, time=time)


@app.route('/booking_done/<clientName>')
def confirm_reservation(clientName):
    print(clientName)
    return render_template("booking_done.html")


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', 5000)
