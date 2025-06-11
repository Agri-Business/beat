
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("DSM_Incentive.csv")
data.columns = data.columns.str.strip()

@app.route('/salesman', methods=['GET'])
def get_salesman_by_contact():
    contact = request.args.get('contact')
    if not contact:
        return jsonify({'error': 'Missing required parameter: contact'}), 400

    data['contact'] = data['contact'].astype(str).str.strip()
    record = data[data['contact'] == str(contact).strip()]
    if record.empty:
        return jsonify({'error': 'contact not found'}), 404

    row = record.iloc[0]

    def safe_cast(value, cast_type):
        return cast_type(value) if pd.notnull(value) else None

    response = {
        'Salesman Name': safe_cast(row['Salesman Name'], str),
        'HO-DSM Type': safe_cast(row['HO-DSM Type'], str),
        'Listed Outlet': safe_cast(row['Listed Outlet'], str),
        'New_Outlet_Addition_Tgt': safe_cast(row['New_Outlet_Addition_Tgt'], str),
        'ECO Target': safe_cast(row['ECO Target'], str),
        'ECO_MTD': safe_cast(row['ECO_MTD'], str),
        'ECO_BTD': safe_cast(row['ECO_BTD'], str),
        'Oil_Tgt': safe_cast(row['Oil_Tgt'], str),
        'Oil_Vol_MT': safe_cast(row['Oil_Vol_MT'], str),
        'Oil_Ach_Per': safe_cast(row['Oil_Ach_Per'], str),
        'Oil_Ach_Per_Slab': safe_cast(row['Oil_Ach_Per_Slab'], str),
        'Oil_Ach_Amount': safe_cast(row['Oil_Ach_Amount'], str),
        'Oil_Vol_BTD': safe_cast(row['Oil_Vol_BTD'], str),
        'Food_Tgt': safe_cast(row['Food_Tgt'], str),
        'Food_Vol_MT': safe_cast(row['Food_Vol_MT'], str),
        'Food_Ach_Per': safe_cast(row['Food_Ach_Per'], str),
        'Food_Ach_Per_Slab': safe_cast(row['Food_Ach_Per_Slab'], str),
        'Food_Ach_Amount': safe_cast(row['Food_Ach_Amount'], str),
        'Food_Vol_BTD': safe_cast(row['Food_Vol_BTD'], str),
        'Total_Vol_MT': safe_cast(row['Total_Vol_MT'], str),
        'Perfect_Store': safe_cast(row['Perfect_Store'], str),
        'Perfect_Store_Amount': safe_cast(row['Perfect_Store_Amount'], str),
        'Perfect_Store_Criteria': safe_cast(row['Perfect_Store_Criteria'], str),
        'Super_Charge_Product': safe_cast(row['Super_Charge_Product'], str),
        'Super_Charge_Product_PDO': safe_cast(row['Super_Charge_Product_PDO'], str),
        'Super_Charge_No_of_Product': safe_cast(row['Super_Charge_No_of_Product'], str),
        'Super_Charge_Tgt': safe_cast(row['Super_Charge_Tgt'], str),
        'Super_Charge_Ach': safe_cast(row['Super_Charge_Ach'], str),
        'Super_Charge_Ach_Per': safe_cast(row['Super_Charge_Ach_Per'], str),
        'Super_Charge_Ach_Per_Slab': safe_cast(row['Super_Charge_Ach_Per_Slab'], str),
        'Super_Charge_Ach_Amount': safe_cast(row['Super_Charge_Ach_Amount'], str),
        'Super_Charge_BTD': safe_cast(row['Super_Charge_BTD'], str),
        'Manday': safe_cast(row['Manday'], str),
        'ASE Name': safe_cast(row['ASE Name'], str),
        'ASE Emp Code': safe_cast(row['ASE Emp Code'], str),
        'ASM Name': safe_cast(row['ASM Name'], str),
        'ASM Emp Code': safe_cast(row['ASM Emp Code'], str),
        'RSM Name': safe_cast(row['RSM Name'], str),
        'RSM Emp Code': safe_cast(row['RSM Emp Code'], str)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
