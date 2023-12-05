from flask import flask, render_template, request, redirect, url_for

app = flask(__name__)

plants = []

class Plant:
    def __init__(self, name):
        self.name = name
        self.watered = False
        self.fertilized = False

@app.route('/')
def index():
    return render_template('index.html', plants=plants)

@app.route('/add_plant', methods=['POST'])
def add_plant():
    plant_name = request.form['plant_name']
    new_plant = Plant(plant_name)
    plants.append(new_plant)
    return redirect(url_for('index'))

@app.route('/water/<int:plant_id>')
def water_plant(plant_id):
    plants[plant_id].watered = True
    return redirect(url_for('index'))

@app.route('/fertilize/<int:plant_id>')
def fertilize_plant(plant_id):
    plants[plant_id].fertilized = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    