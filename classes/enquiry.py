import json, datetime
from classes.quotes import Quotes
from classes.request_builder import Curl_Request


class Enquiry:
    payload = None
    headers = {}
    source_dir = None
    url = None

    def __init__(self, resource_dir, app, template, header, url, referrer=None):
        self.enquiry_url = url + '/enquiries'
        self.source_dir = resource_dir + app
        enquiry_file = self.source_dir + "/" + template
        with open(enquiry_file, 'r') as file:
            json_data = file.read()
            self.payload = json.loads(json_data)
        self.headers[header] = app
        self.set_policy_start_date()
        if referrer is not None:
            with open(self.source_dir + "/referrer.json"):
                json_data = file.read()
                referrers = json.loads(json_data)
            self.headers["x-qmg-referrer"] = referrers[json.dumps(referrer)]

    def set_policy_start_date(self):
        # update policy start date as today date:
        today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
        if "forms" in self.payload:
            for data_list in self.payload["forms"]:
                if "data" in data_list and "policy_start_date" in data_list["data"]:
                    data_list["data"].update({"policy_start_date": today})
        else:
            raise ValueError("Invalid json object enquiry: forms was not found.")

    def submit(self, jump_box, url):
        request = Curl_Request(jump_box)
        response = request.post(self.url, self.payload, headers=self.headers)
        body = eval(response)["body"]
        enquiry = json.loads(body)
        if enquiry["submission"]["isValid"] is False:
            Exception ("Submitted enquiry was not validated")
        version = enquiry.get("version")
        quotes = Quotes(version.get("quotes"))
        return {"enquiry": enquiry, "quotes": quotes}
