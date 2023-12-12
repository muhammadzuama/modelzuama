# app.py
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Mengambil data dari request JSON
        data = request.get_json()
        # Membuat DataFrame dari data yang diberikan
        df = pd.DataFrame(data)

        # Mengubah data kategorikal (Jenis_Kelamin) menjadi numerik
        df['Jenis_Kelamin'] = df['Jenis_Kelamin'].map({'Laki-laki': 0, 'Perempuan': 1})

        # Memisahkan fitur dan label
        X = df.drop('Risiko_Stunting', axis=1)
        y = df['Risiko_Stunting']

        # Melakukan prediksi menggunakan model yang telah dilatih
        y_pred = model.predict(X)

        # Mengembalikan hasil prediksi
        return jsonify({'predictions': list(y_pred)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Membuat dan melatih model Decision Tree saat aplikasi dijalankan
    data = pd.read_csv('DeteksiFIx/datasetfix2.csv')
    df = pd.DataFrame(data)
    df['Jenis_Kelamin'] = df['Jenis_Kelamin'].map({'Laki-laki': 0, 'Perempuan': 1})
    X = df.drop('Risiko_Stunting', axis=1)
    y = df['Risiko_Stunting']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Jalankan aplikasi Flask
    app.run(debug=True)
