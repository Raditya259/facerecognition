import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('D:/Kuliah/facerecognition/venv/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-aaa34-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "111111":
        {
            "name": "Bayu Rizkhi",
            "major": "Informatics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "222222":
        {
            "name": "Andika Wira Yumna",
            "major": "Informatika",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "666666":
        {
            "name": "Sultan Rizqyllah",
            "major": "Informatics",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2024-05-14 17:35:34"
        },
    "777777":
        {
            "name": "Daffa Tungga Wisesa",
            "major": "Informatics",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2024-05-14 17:35:34"
        },
    "888888":
        {
            "name": "Raditya Lungguk Satya Putra",
            "major": "Informatics",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2024-05-14 17:35:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)