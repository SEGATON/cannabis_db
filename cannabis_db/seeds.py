from .models import Dispensary
from faker import Faker 

fake = Faker()



def seed_db():
	for i in range(0, n):
		Dispensary.objects.create(
				dispensary = fake.title()
			)