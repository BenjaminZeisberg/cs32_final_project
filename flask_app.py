from flask import Flask, render_template
import flask
from requests import get
from backend import *

app = Flask(__name__)

@app.route('/')
def index():
    get_map_from_backend = return_map(0)
    get_map_from_backend.save('templates/map0.html')
    get_map_from_backend = return_map(1)
    get_map_from_backend.save('templates/map1.html')
    get_map_from_backend = return_map(2)
    get_map_from_backend.save('templates/map2.html')
    get_map_from_backend = return_map(3)
    get_map_from_backend.save('templates/map3.html')
    get_map_from_backend = return_map(4)
    get_map_from_backend.save('templates/map4.html')
    get_map_from_backend = return_map(5)
    get_map_from_backend.save('templates/map5.html')
    get_map_from_backend = return_map(6)
    get_map_from_backend.save('templates/map6.html')
    get_map_from_backend = return_map(7)
    get_map_from_backend.save('templates/heat.html')

    return render_template('home.html')

@app.route('/map0')
def map():
    return render_template('map0.html')

@app.route('/map1')
def map1():
    return render_template('map1.html')

@app.route('/map2')
def map2():
    return render_template('map2.html')

@app.route('/map3')
def map3():
    return render_template('map3.html')

@app.route('/map4')
def map4():
    return render_template('map4.html')

@app.route('/map5')
def map5():
    return render_template('map5.html')

@app.route('/map6')
def map6():
    return render_template('map6.html')
    
@app.route('/heatmap')
def heatmap():
    return render_template('heat.html')


@app.route('/day1')
def first_map_total():
    get_map_from_backend = return_map(0)
    return get_map_from_backend._repr_html_()

@app.route('/day2')
def second_map_total():
    get_map_from_backend = return_map(1)
    return get_map_from_backend._repr_html_()

@app.route('/day3')
def third_map_total():
    get_map_from_backend = return_map(2)
    return get_map_from_backend._repr_html_()

@app.route('/day4')
def fourth_map_total():
    get_map_from_backend = return_map(3)
    return get_map_from_backend._repr_html_()

@app.route('/day5')
def fifth_map_total():
    get_map_from_backend = return_map(4)
    return get_map_from_backend._repr_html_()

@app.route('/day6')
def sixth_map_total():
    get_map_from_backend = return_map(5)
    return get_map_from_backend._repr_html_()

@app.route('/day7')
def seventh_map_total():
    get_map_from_backend = return_map(6)
    return get_map_from_backend._repr_html_()

@app.route('/heat')
def heat_map_total():
    get_map_from_backend = return_map(7)
    return get_map_from_backend._repr_html_()

# @app.route('/day2/')
# def second_map():
#     flask.send_file('./maps/map2.html')
#     return render_template('maps/map2.html')


# @app.route('/maps/map.html')
# def show_map():
#     return flask.send_file('./maps/map.html')

# @app.route('/maps/map2.html')
# def second_map():
#     return flask.send_file('./maps/map2.html')



# def index():
#     map_test()
#     return render_template('index.html')

# @app.route('/map')
# def map():
#     return render_template('map.html')



# #rendering the HTML page which has the button
# @app.route('/json')
# def json():
#     return render_template('json.html')

# #background process happening without any refreshing
# @app.route('/background_process_test')
# def background_process_test():
#     print ("Hello")
#     return ("nothing")

if __name__ == '__main__':
    app.run(debug=True)
