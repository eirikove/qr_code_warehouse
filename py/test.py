
from warehouse_item import warehouse_item
from csv_methods import reg_new_item, item_already_exists
import datetime

testobjekt = warehouse_item("navnetest", "beskrivelsetest", datetime.date.today(), datetime.datetime.now(), "test_qr_id")

csv_rad = testobjekt.attributes_to_csv()

print(csv_rad)
# Pseudo: writer.writeLine(csv_rad)

reg_new_item("regtest", "yas", "123")
reg_new_item("sameqrcode", "jepp", "111")

print(item_already_exists(123))
print(item_already_exists(111))
