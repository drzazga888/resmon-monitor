from rest_api.swagger_server.models.metric import Metric  # noqa: E501
from rest_api.swagger_server import util
from common.database.mongoAccess import dbApi

from flask_jwt_extended import jwt_required


@jwt_required
def get_metrics():  # noqa: E501
    """List of metrics

     # noqa: E501


    :rtype: List[Metric]
    """

    api = dbApi.dbApi()
    metrics = api.getAllMetrics()
    response = []

    for metric in metrics.keys():
        interval = None
        moving_window = None
        parent_id = None
        hosts = api.getHostnameByMetric(metric)

        print("getCpxDefinitions, metric: ", metric)

        cpxDef = api.getCpxDefinitions({api.METRIC_ID_KEY: metric})

        if cpxDef:
            print("cpxDef not none")
            hosts.append(cpxDef[api.HOSTNAME_KEY])
            interval = cpxDef[api.INTERVAL_KEY]
            moving_window = cpxDef[api.MOVING_WINDOW_KEY]
            parent_id = cpxDef[api.PARENT_ID_KEY]
            print(parent_id)

        metric_object = Metric(
            id=metric,
            interval=interval,
            moving_window_duration=moving_window,
            description=metrics[metric][0],
            unit=metrics[metric][1],
            hosts=hosts,
            parent_id=parent_id,
        )
        response.append(metric_object.to_dict())

    return response
