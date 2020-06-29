from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "안녕하세요 나는 개발자 입니다"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="내 이름은 김성민 입니다",
    #     )
    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
            self.stdout.write(self.style.SUCCESS(f"{len(facilities)} 시설 데이터 대량 생성 완료"))
