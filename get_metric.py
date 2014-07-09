#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk import UcloudApiClient
import config
from pprint import pprint
import sys


def get_metric(region, resource_type, resource_id, metric_name,
               timerange=1 * 60 * 60):
    """Get UCloud monitor data
    Region: "cn-east-01"|"cn-north-01"|"cn-south-01"|"hk-01"|"cn-north-02"
            East China   Bejing bgpa   South China  Hong Kong   Beijing bgpb
    ResourceType: 'uhost'|'udb'|'umem'|'ulb'
    MetricName:
        uhost:
            'NetworkIn'
            'NetworkOut'
            'CPUUtilization'
            'IORead'
            'IOWrite'
            'DiskReadOps'
            'DiskWriteOps'
            'NICIn'
            'NICOut'
            'MemUsage'
            'DataSpaceUsage'
            'RootSpaceUsage'
            'ReadonlyDiskCount'
            'RunnableProcessCount'
            'BlockProcessCount'
        udb:
            'CPUUtilization'
            'MemUsage'
            'QPS'
            'ExpensiveQuery'

        ulb:
            'NetworkOut'
            'CurrentConnections'

        umem:
            'Usage'
            'QPS'
            'InstanceCount'

    """
    api_client = UcloudApiClient(config.base_url, config.public_key,
                                 config.private_key)

    response = api_client.get("/", Action="GetMetric",
                              Region=region,
                              ResourceType=resource_type,
                              ResourceID=resource_id,
                              MetricName=metric_name,
                              TimeRange=timerange)
    pprint(response)


if __name__ == '__main__':
    # get_metric('cn-east-01', 'uhost', 'uhost-ezsffw', 'NetworkOut')
    usage = "%s Region ResourceType ResourceID MetricName [TimeRange]\n" % (sys.argv[0])
    argc = len(sys.argv)
    if argc < 5:
        sys.stderr.write(usage)
        sys.exit(1)
    region = sys.argv[1]
    resource_type = sys.argv[2]
    resource_id = sys.argv[3]
    metric_name = sys.argv[4]
    if argc == 6:
        get_metric(region, resource_type, resource_id, metric_name, int(sys.argv[5]))
    else:
        get_metric(region, resource_type, resource_id, metric_name)
