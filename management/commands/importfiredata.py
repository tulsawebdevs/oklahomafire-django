import csv
import requests
import StringIO

from datetime import datetime
from django.utils.timezone import utc
from django.core.management.base import BaseCommand, CommandError

from oklahomafire.models import Location

class Command(BaseCommand):
    def handle(self, *args, **options):
        all_locations_response = requests.get("http://firms.modaps.eosdis.nasa.gov/active_fire/text/USA_contiguous_and_Hawaii_24h.csv")

        f = StringIO.StringIO(all_locations_response.text)
        reader = csv.DictReader(f)
        
        for row in reader:
            row['acq_datetime'] = datetime.strptime("%s %s" % (row['acq_date'], row['acq_time'].strip()), "%Y-%m-%d %H%M").replace(tzinfo=utc)
            del row['acq_date']
            del row['acq_time']
            Location.objects.get_or_create(**row)
#            location = Location()
#            location.latitude = row['latitude']
#            location.longitude = row['longitude']
#            location.brightness = row['brightness']
#            location.scan = row['scan']
#            location.track = row['track']
#            location.acq_datetime = datetime.strptime("%s %s" % (row['acq_date'], row['acq_time'].strip()), "%Y-%m-%d %H%M")
#            location.satellite = row['satellite']
#            location.confidence = row['confidence']
#            location.version = row['version']
#            location.bright_t31 = row['bright_t31']
#            location.frp = row['frp']
#            location.save()

        f.close()
