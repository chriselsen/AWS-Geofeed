[![build-aws-geoip](https://github.com/chriselsen/AWS-Geofeed/actions/workflows/build-aws-geoip.yml/badge.svg)](https://github.com/chriselsen/AWS-Geofeed/actions/workflows/build-aws-geoip.yml)
# AWS-Geofeed
[Geofeed for AWS (AS16509)](https://raw.githubusercontent.com/chriselsen/AWS-Geofeed/main/data/aws-geofeed.txt) as defined in datatracker.ietf.org/doc/html/rfc8805.

## What is a Geofeed?

A geofeed, sometimes also called geolocation feed, is a data format laid out in [RFC 8805](https://datatracker.ietf.org/doc/html/rfc8805). It is used by network operators to provide geolocation information for their IP prefixes. This enables IP address databases to be updated and improved with very little hassle on either end.

## Why a Geofeed for AWS (AS16509)?

While AWS [publishes information about it's IP address ranges](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html) in its [ip-ranges.json file](https://ip-ranges.amazonaws.com/ip-ranges.json), it uses a proprietary format to do so and also lacks detailed location information. 

This Geofeed generator ingests the data from the ip-ranges.json file and coverts it to an [RFC8805-compliant feed](https://raw.githubusercontent.com/chriselsen/AWS-Geofeed/main/data/aws-geofeed.txt). 

**If you enjoy this work, please consider sponsoring:**

[![Buy Me A Coffee](https://raw.githubusercontent.com/chriselsen/chriselsen/main/buymeacoffee.png)](https://www.buymeacoffee.com/chriselsen)
[![Support via PayPal](https://raw.githubusercontent.com/chriselsen/chriselsen/main/paypal-donate.png)](https://www.paypal.me/christianelsen)
[![Sponsor on Github](https://raw.githubusercontent.com/chriselsen/chriselsen/main/github-sponsor.png)](https://github.com/sponsors/chriselsen)

## Data source

This Geofeed generator uses the publicly available data from the AWS ip-ranges.json file to map an IP prefix to a location. While AWS only provides a location name such as ```us-east-1``` for a prefix, a custom location mapping converts this identified into an RFC8805-compliant identifier of ```US,US-VA,Ashburn,```.

### Location mappings

AWS includes detailed location information within the name of some AWS Regions, such as ```Europe (Frankfurt)``` for the ```eu-central-1``` Region. Here it is very trivial to convert such a location to the RFC8805-compliant identifier of ```DE,DE-HE,Frankfurt,```. In other cases, the AWS Region name only specifies a geographical region, such as Northern Virginia for ```US East (N. Virginia)``` as the name for the identifier ```us-east-1```. 
In these cases some additional research through openly available data is necessary to add a more accurate location. This openly available data can include [AWS blog posts](https://aws.amazon.com/blogs/aws/in-the-works-aws-canada-west-calgary-region/) or [AWS job postings](https://www.amazon.jobs/en/landing_pages/aws-data-centers?INTCMPID=HB_AJAW100046B).

## Updates

Updates are triggered via [Amazon SNS](https://aws.amazon.com/sns/), when AWS [makes changes](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html#subscribe-notifications) to the ip-ranges.json list.
