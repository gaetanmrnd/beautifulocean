
#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ea",
    "dataset": "era5",
    "date": "2017-12-25",
    "domain": "g",
    "expver": "1",
    "param": "229.140",
    "step": "0/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18",
    "stream": "wave",
    "time": "18:00:00",
    "type": "fc",
    "target": "output",
})