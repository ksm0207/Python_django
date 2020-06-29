import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "안녕하세요 나는 개발자 입니다"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="내 이름은 김성민 입니다",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}명 유저 대량 생성 완료"))
