records = [
('mashrur@example.com','Hello World'),
('johndoe@example.com','Hello to you too'),
('janedoe@example.com','Python is awesome'),
]

for index, record in enumerate(records):
    key, value = record
    if key == 'johndoe@example.com':
        break

print(records[index])
