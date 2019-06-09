#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import asyncio
import asyncovh
import datetime
from tabulate import tabulate

# Services type desired to mine. To speed up the script, delete service type you don't use!
service_types 	= [ 
	'allDom',
	'cdn/dedicated',
	'cdn/website',
	'cdn/webstorage',
	'cloud/project',
	'cluster/hadoop',
	'dedicated/housing',
	'dedicated/nas',
	'dedicated/nasha',
	'dedicated/server',
	'dedicatedCloud',
	'domain/zone',
	'email/domain',
	'email/exchange',
	'freefax',
	'hosting/privateDatabase',
	'hosting/web',
	'hpcspot',
	'license/cloudLinux',
	'license/cpanel',
	'license/directadmin',
	'license/office',
	'license/plesk',
	'license/sqlserver',
	'license/virtuozzo',
	'license/windows',
	'license/worklight',
	'overTheBox',
	'pack/xdsl',
	'router',
	'sms',
	'telephony',
	'telephony/spare',
	'veeamCloudConnect',
	'vps',
	'xdsl',
	'xdsl/spare'
]

# Delay before expiration in days
delay = 60

async def get_expired_services(client, service_type, delay_date):
	service_list = await client.get("/{0}".format(service_type))

	# If we found you have this one or more of this product, we get these information
	tasks = []
	for service in service_list:
		tasks.append(client.get("/{0}/{1}/serviceInfos".format(service_type, service)))

	results = await asyncio.gather(*tasks)

	rows = []
	for service_infos in results:
		service_expiration_date = datetime.datetime.strptime(service_infos['expiration'], '%Y-%m-%d')
		print("{0} VS {1}".format(service_expiration_date, delay_date))
		if service_expiration_date >= delay_date:
			continue

		rows.append( [ service_type, service, service_infos['status'], service_infos['expiration'] ] )

	return rows

async def main():
	# Compute now + delay
	delay_date = datetime.datetime.now() + datetime.timedelta(days=delay)

	# Create a client using ovh.conf
	client = asyncovh.Client()
	await client.init()

	services_will_expired = []

	# Check all OVH product (service type)
	async with client._session:
		tasks = []
		for service_type in service_types:
			tasks.append(get_expired_services(client, service_type, delay_date))
		
		results = await asyncio.gather(*tasks)
		for rows in results:
			services_will_expired.extend(rows)

	# At the end, we show service expirated or that will expirated (in a table with tabulate)
	print(tabulate(services_will_expired, headers=['Type', 'ID', 'status', 'expiration date']))

if __name__ == "__main__":
    import sys
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    asyncio.run(main())