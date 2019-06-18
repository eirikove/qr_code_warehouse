
from warehouse_item import warehouse_item
#import csv_metoder
import datetime

testobjekt = warehouse_item("navnetest", "beskrivelsetest", datetime.date.today(), datetime.datetime.now(), "test_qr_id")

csv_rad = testobjekt.attributes_to_csv()

print(csv_rad)
# Pseudo: writer.writeLine(csv_rad)
