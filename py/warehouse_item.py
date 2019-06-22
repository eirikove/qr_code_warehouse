import datetime


class warehouse_item(object):

    def __init__(self, name, description, date_registered, time_registered, qr_code_id):
        self.name = name
        self.description = description
        self.date_registered = date_registered
        self.time_registered = time_registered
        self.qr_code_id = qr_code_id

    def attributes_to_csv(self):
        return "{},{},{},{},{}".format(self.name, self.description, self.date_registered.strftime("%d"+"."+"%b"+"."+"%Y"), self.time_registered.strftime("%H"+":"+"%M"), self.qr_code_id)
