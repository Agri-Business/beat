
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("Beat and Outlet.csv")
data.columns = data.columns.str.strip()

@app.route('/get_beats', methods=['GET'])
def get_beats_by_contact():
    contact = request.args.get('contact')
    if not contact:
        return jsonify({'error': 'Missing required parameter: contact'}), 400

    data['contact'] = data['contact'].astype(str).str.strip()
    matched_rows = data[data['contact'] == str(contact).strip()]
    if matched_rows.empty:
        return jsonify({'error': 'contact not found'}), 404

    beat_names = matched_rows['Beat Name'].dropna().unique().tolist()

    return jsonify({'Beat Names': beat_names})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
