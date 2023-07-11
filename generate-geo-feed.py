#!/usr/bin/env python3

# Generate geofeed as defined in datatracker.ietf.org/doc/html/rfc8805 from AWS ip-ranges.json file
# Does not include locations from ip-ranges.json marked as 'GLOBAL'
#
# Author: Christian Elsen - https://github.com/chriselsen/

import json
import datetime
from urllib.request import urlopen

# AWS ip-ranges.json URL
url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

# Load and open JSON file
response = urlopen(url)
ipranges = json.loads(response.read())

# Open local Location Mapping file
loc_map = {}
with open('./data/loc-mapping.txt') as lf:
    for line in lf:
        if not line.startswith('#'):
            k, v = [i.strip() for i in line.split(' ', 1)]
            loc_map.update({k: v})
lf.close()

# Location mapping function
def loc_lookup(loc):
    try:
        return loc_map[loc]
    except:
        raise SystemExit('Unknown location encountered: ' + loc)

# Convert ip-ranges to GeoFeed
output = {}
for i in ipranges['prefixes']:
    if i['network_border_group'] != "GLOBAL":
        output.update({i['ip_prefix']: loc_lookup(i['network_border_group'])})

# Write output file
df=open('./data/aws-geofeed.txt','w')
df.write('# AWS (AS16509) Geofeed, lastupdated (rfc3339): ' + datetime.datetime.now(datetime.timezone.utc).isoformat('T','seconds') + '\n')
df.write('# Self-published geofeed as defined in datatracker.ietf.org/doc/html/rfc8805\n')
df.write('# Data derived from https://ip-ranges.amazonaws.com/ip-ranges.json\n')
df.write('# Does not include locations from ip-ranges.json marked as \'GLOBAL\'\n')
for key in sorted(output):
    df.write(key + ',' + output[key] + '\n')
df.close()
