reader = csv.reader(open(os.path.join(BASE_DIR, 'Book1.csv')))
for line in reader:
    print(line[0])
    d = KeySkill.objects.get_or_create(skill=line[0])
    print(d)
    KeySkill.objects.create(skill=line[0])
