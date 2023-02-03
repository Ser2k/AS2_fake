from random import shuffle

students = [
    'Abdylmälik',
    'Dawut',
    'Döwran',
    'Erkin',
    'Eziz',
    'Hamza',
    'Iskender',
    'Muhammetali',
    'Muhammetemir',
    'Mukam',
    'NurmuhammetB',
    'NurmuhammetG',
    'Ogulnabat',
    'Ogulşeker',
    'Orazmyrat',
    'Resul',
    'Şazada',
    'Serdargeldi',
    'Seýdylla',
]

shuffle(students)

for i in range(len(students)):
    print(i+1, students[i])