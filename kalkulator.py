import tkinter as tk
from tkinter import messagebox

# Fungsi kalkulator medis
def bmi(weight, height):
    """Menghitung Body Mass Index (BMI)"""
    return weight / (height ** 2)

def heart_rate(age, resting_heart_rate):
    """Menghitung target heart rate berdasarkan rumus Karvonen"""
    max_heart_rate = 220 - age
    return 0.5 * (max_heart_rate - resting_heart_rate) + resting_heart_rate, 0.85 * (max_heart_rate - resting_heart_rate) + resting_heart_rate

def ideal_body_weight(height, gender):
    """Menghitung berat badan ideal berdasarkan tinggi dan jenis kelamin"""
    if gender == 'male':
        return 50 + 2.3 * ((height * 39.37) - 60)
    else:
        return 45.5 + 2.3 * ((height * 39.37) - 60)

def body_fat_percentage(weight, waist, neck, hip, gender):
    """Menghitung persentase lemak tubuh berdasarkan rumus US Navy"""
    if gender == 'male':
        return 86.010 * (waist - neck) / weight - 70.041
    else:
        return 163.205 * (waist + hip - neck) / weight - 97.684

def calorie_needs(weight, height, age, gender, activity_level):
    """Menghitung kebutuhan kalori dasar"""
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    if activity_level == 'low':
        return bmr * 1.2
    elif activity_level == 'moderate':
        return bmr * 1.55
    else:
        return bmr * 1.9

def glascow_coma_scale(eye_response, verbal_response, motor_response):
    """Menilai tingkat kesadaran dengan skala Glasgow"""
    return eye_response + verbal_response + motor_response

def apgar_score(heart_rate, respiration, muscle_tone, reflex_response, skin_color):
    """Menghitung skor Apgar untuk bayi baru lahir"""
    return heart_rate + respiration + muscle_tone + reflex_response + skin_color

def chad_score(age, history_of_stroke, heart_failure, diabetes, hypertension):
    """Menghitung skor CHAD-VASC untuk risiko stroke"""
    score = 0
    if age >= 75:
        score += 2
    elif age >= 65:
        score += 1
    if history_of_stroke or heart_failure:
        score += 1
    if diabetes or hypertension:
        score += 1
    return score

def glomerular_filtration_rate(age, serum_creatinine, weight, gender):
    """Menghitung GFR (Glomerular Filtration Rate)"""
    if gender == 'male':
        return 140 - age * weight / serum_creatinine
    else:
        return (140 - age) * weight / serum_creatinine * 0.85

def anion_gap(sodium, chloride, bicarbonate):
    """Menghitung anion gap"""
    return sodium - (chloride + bicarbonate)

def qt_interval(heart_rate):
    """Menghitung QT interval"""
    return 0.35 * heart_rate

def fluid_resuscitation(weight, deficit_percentage):
    """Menghitung volume cairan untuk resusitasi"""
    return weight * deficit_percentage

def ascvd_risk(age, cholesterol, systolic_blood_pressure, smoking_status, diabetes, gender):
    """Menghitung risiko ASCVD (Atherosclerotic Cardiovascular Disease)"""
    risk = (age * 0.5) + (cholesterol * 0.25) + (systolic_blood_pressure * 0.2)
    if smoking_status:
        risk += 1
    if diabetes:
        risk += 1
    if gender == 'male':
        risk += 2
    return risk

def otitismedia_calculation(age, fever, ear_pain, drainage):
    """Perhitungan gejala otitis media"""
    score = 0
    if age < 2:
        score += 2
    if fever > 38:
        score += 2
    if ear_pain:
        score += 1
    if drainage:
        score += 1
    return score

def pregnancy_due_date(last_menstrual_period):
    """Perkiraan tanggal lahir berdasarkan tanggal haid terakhir"""
    from datetime import datetime, timedelta
    lmp = datetime.strptime(last_menstrual_period, '%Y-%m-%d')
    return lmp + timedelta(weeks=40)

def paediatric_wells_score(fever, cough, runny_nose, breathing_difficulty, chest_pain):
    """Skor Wells Pediatrik untuk infeksi saluran pernapasan"""
    score = 0
    if fever:
        score += 1
    if cough:
        score += 1
    if runny_nose:
        score += 1
    if breathing_difficulty:
        score += 2
    if chest_pain:
        score += 3
    return score

def respiratory_rate(age, breathing):
    """Menghitung tingkat pernapasan untuk evaluasi"""
    if age < 1:
        return 30 - 40
    elif age < 2:
        return 25 - 35
    elif age < 5:
        return 20 - 30
    return breathing

def bmi_category(bmi_value):
    """Menentukan kategori BMI"""
    if bmi_value < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi_value <= 24.9:
        return 'Normal weight'
    elif 25 <= bmi_value <= 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

def ejection_fraction(stroke_volume, end_diastolic_volume):
    """Menghitung fraksi ejeksi jantung"""
    return (stroke_volume / end_diastolic_volume) * 100

def pack_years(smoking_years, packs_per_day):
    """Menghitung pack years untuk perokok"""
    return smoking_years * packs_per_day

def temperature_conversion(celsius):
    """Mengonversi suhu dari Celcius ke Fahrenheit"""
    return (celsius * 9/5) + 32

# Antarmuka Grafis dengan Tkinter
def show_result():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        age = int(entry_age.get())
        gender = gender_var.get()
        if gender == "Male":
            gender = 'male'
        else:
            gender = 'female'

        result = bmi(weight, height)
        result_label.config(text=f'BMI: {result:.2f}')
    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan data yang valid!")

# UI
root = tk.Tk()
root.title("Kalkulator Medis Lengkap")

# Label dan entry untuk input
tk.Label(root, text="Berat (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

tk.Label(root, text="Tinggi (m):").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

tk.Label(root, text="Usia (tahun):").grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

gender_var = tk.StringVar(value="Male")
tk.Label(root, text="Jenis Kelamin:").grid(row=3, column=0)
tk.Radiobutton(root, text="Laki-laki", variable=gender_var, value="Male").grid(row=3, column=1)
tk.Radiobutton(root, text="Perempuan", variable=gender_var, value="Female").grid(row=3, column=2)

# Tombol untuk menghitung BMI
tk.Button(root, text="Hitung BMI", command=show_result).grid(row=4, column=0, columnspan=2)

# Label untuk hasil
result_label = tk.Label(root, text="BMI: ", font=("Helvetica", 14))
result_label.grid(row=5, column=0, columnspan=2)

# Jalankan aplikasi
root.mainloop()
