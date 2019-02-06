from influxdb import InfluxDBClient
import Util
import time

if __name__ == "__main__":
    client = InfluxDBClient('influx', 8086, 'root', 'root', 'example')
    client.create_database('example')

    now_time = Util.get_time()
    now_date = Util.get_date()
 
    message =  [{ 
            "measurement":"matlab",\
            "tags": {
                "type":"regular_info"
            },\
            "time": now_date+"T"+now_time+"Z",\
            "fields": {                 \
                    "total": 10000,   \
                    "use": 116,       \
                    # "metadata": {"MATLAB": "v40", "vendor": "MLM", "expiry": "30-jul-2019\r\n", "vendor_string": "vi=0:at=200:ae=1:lu=200:lo=TH:ei=5150696:lr=1:ep=15:\r\n"}     \
            }
        }]
    client.write_points(message)

    result = client.query('select use from matlab;')

    print("Result: {0}".format(result))

