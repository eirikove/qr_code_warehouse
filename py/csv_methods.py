from warehouse_item import warehouse_item
import csv
import datetime


log_file_path = "YOUR_FILE_PATH_HERE"
storage_file_path = "YOUR_FILE_PATH_HERE"


def reg_new_item(name, description, qr_code_id):

    date_registered = ""
    time_registered = ""

    if item_already_exists(qr_code_id):
        print("Can't register new item. Item with QR code already exist.", qr_code_id)
    else:
        item = warehouse_item(name, description, datetime.date.today(), datetime.datetime.now(), qr_code_id)
        csv_row = item.attributes_to_csv()

        with open(storage_file_path, mode='a') as storage_file:
            storage_writer = csv.writer(storage_file, delimiter=";", quotechar="'", quoting=csv.QUOTE_MINIMAL)
            storage_writer.writerow([csv_row])


def item_already_exists(scanned_qr_code):
    with open(storage_file_path, mode='r') as warehouse_file:
        csv_reader = csv.reader(warehouse_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # print(row)
            if str(scanned_qr_code) == row[4]:
                line_count += 1
                # print("Found duplicate QR ID")
                return True
            else:
                line_count += 1

    # print("Processed lines: ", line_count)
    return False


def extract_item():
    # Skriv til utleie_logg
    pass


def return_item():
    pass
