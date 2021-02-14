from flask import Flask, render_template
import data


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
    return render_template("profile.html")


@app.route('/request/')
def make_request():
    return render_template("request.html")


@app.route('/request_done/')
def confirm_request():
    return render_template("request_done.html")


@app.route('/booking/<profile_id>/<weekday>/<time>/')
def reserve_tutor(profile_id, weekday, time):
    return render_template("booking.html")

@app.route('/booking_done/')
def confirm_reservation():
    return render_template("booking_done.html")


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', 5000)
