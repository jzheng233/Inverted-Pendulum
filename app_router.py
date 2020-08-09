from flask import Flask, render_template, request, jsonify
from ip_mtor_simulator import InvertedPudulemSimulator


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    (x_path, t_angle) = simulator.run_simulation(tfinal, dt)

    # Need to format list to string before return to javascript
    x_str = [format(flt) for flt in x_path]
    t_str = [format(flt) for flt in t_angle]

    resp = {'x_path': x_str, "angle": t_str}
    return resp


tfinal: float = 5.0
dt: float = 0.001
simulator = InvertedPudulemSimulator()

if __name__ == '__main__':
    app.run(debug=True)

