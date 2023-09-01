


from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    predicted_price = None
    if request.method == 'POST':
        marka = request.form.get('marka')
        araba_model = request.form.get('model')
        yil = int(request.form.get('yil'))
        yakit = request.form.get('yakit')
        vites = request.form.get('vites')
        km = float(request.form.get('km'))
        camtavan = request.form.get('camtavan')
        motor_new = float(request.form.get('motor'))

        data = pd.DataFrame({
            'marka': [marka],
            'model': [araba_model],
            'yıl': [yil],
            'yakıt': [yakit],
            'vites': [vites],
            'km': [km],
            'camtavan': [camtavan],
            'motor_new': [motor_new]
        })

        predicted_price = format(round(model.predict(data)[0]), ",")

    return render_template('index.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
