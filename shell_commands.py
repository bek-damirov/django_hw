from employee.models import *
from django.db.models import Q, Subquery

bek = Employee.objects.create(name='Bek Damirov', birth_date="1998-12-17", position="Director",
                              salary=500000, work_experience="2010-09-01")
samat = Employee.objects.create(name='Samat Raev', birth_date="1998-11-01", position="Zam-Director",
                                salary=400000, work_experience="2012-09-22")
rinat = Employee.objects.create(name='Rinat Aliev', birth_date="1999-03-12", position="Secretar",
                                salary=300000, work_experience="2014-08-17")
askat = Employee.objects.create(name='Askat Alymbekov', birth_date="1996-09-12", position="Zam-Secretar",
                                salary=200000, work_experience="2015-11-25")
pass_1 = Passport.objects.create(inn='123456789', id_card='23424324', worker=bek)
pass_2 = Passport.objects.create(inn='289789792', id_card='27826876', worker=samat)
pass_3 = Passport.objects.create(inn='153456789', id_card='345252344', worker=rinat)
pass_4 = Passport.objects.create(inn='253455789', id_card='7656557524', worker=askat)

Employee.objects.get(id=4).delete()

project = WorkProject.objects.create(project_name="Business")
project.persons.set([bek, samat, rinat], through_defaults={'data_joined': '2010-11-25'})

Employee.objects.filter(name='Rinat Aliev').delete()

nuradil = Employee.objects.create(name='Nuradil Turdubaev', birth_date="1999-12-21", position="Secretar",
                                  salary=300000, work_experience="2015-03-29")

client_1 = Client.objects.create(name="someclient", birth_date="1993-11-21", address="Bishkek", phone_number="+996700987656")
client_2 = Client.objects.create(name="someclient_1", birth_date="1990-10-13", address="Tokmok", phone_number="+996500987656")
client_3 = Client.objects.create(name="someclient_2", birth_date="1989-09-24", address="Naryn", phone_number="+996701983656")

vip = VipClient.objects.create(name="somevipclient", birth_date="1982-11-21", vip_status_start="2021-12-12",
                               domination_amount="9000000")

Client.objects.get(id=1).delete()

Employee.objects.all()
Passport.objects.all()
WorkProject.objects.all()
Client.objects.all()
VipClient.objects.all()

