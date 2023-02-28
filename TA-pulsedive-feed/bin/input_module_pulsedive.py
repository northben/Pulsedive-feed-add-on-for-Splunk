
# encoding = utf-8

import json
import csv


def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # api_key = definition.parameters.get('api_key', None)
    pass

def collect_events(helper, ew):

    parameters = {
        "key": helper.get_arg('api_key'),
        "header": "true",
        "fields": "id,type,risk,threats,feeds,usersubmissions,riskfactors,reference",
        "types": "ip,ipv6,domain,url",
        "risk": "unknown,none,low,medium,high,critical",
        "retired": "true",
        "seen": "all",
    }

    response = helper.send_http_request(url, "GET", parameters=parameters, verify=True, use_proxy=True)
    url = "https://pulsedive.com/premium/"

    for row in csv.DictReader(response.text.splitlines()):
        helper.log_info(row)
        json_data = json.dumps(row)
        event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=json_data)
        ew.write_event(event)
