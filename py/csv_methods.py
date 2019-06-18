from warehouse_item import warehouse_item

log_file_path = ""
storage_file_path = ""

def reg_new_item(name, description, qr_code_id):
    if item_already_exists:
        return "Item already exists" # Popup-melding her
    item = warehouse_item(name, description, date_registered, time_registered, qr_code_id)
    csv_row = attributes_to_csv
    # TODO:
    # CSV READER
    # Finn en tom rad
    # Writer
    # Skriv csv_rad til raden
    # Lagre filen

def item_already_exists(scanned_qr_code):
    # # TODO:
    # CSV READER
    # Les varelager.csv filen
    # Søk gjennom listen på lager_gjenstand.qr_code_id
        #if(scannet_qr_kode = kode_fra_csv[i])
            #return true
    return false

def extract_item():
    # Skriv til utleie_logg
    pass

def return_item():
    pass
