import connexion
import six

from swagger_server.models.host import Host  # noqa: E501
from swagger_server.models.payload import Payload  # noqa: E501
from swagger_server import util


def delete_metric(metric_id, hostname):  # noqa: E501
    """Delete complex metric

     # noqa: E501

    :param metric_id: Metric identyfier
    :type metric_id: str
    :param hostname: Target host (domain name)
    :type hostname: str

    :rtype: object
    """
    return 'do some magic!'


def get_hosts(q=None):  # noqa: E501
    """Get list of hosts

     # noqa: E501

    :param q: Filters out used metrics and hosts according to provided keys. String needs to match the following schema: &#x60;KEY1:VAL1,KEY2:VAL2;KEY3:VAL4...&#x60;. Comma is used to indicate &#x60;AND&#x60; operation while semicolon relates to &#x60;OR&#x60;. When &#x60;VAL&#x60; paramater is wrapped into slashes then regex mode is activated. For example when we query for &#x60;metric_id:cpu,os:/.*nix.*/;metric_id:cpu,os:/.*win.*/&#x60; we should receive cpu metric measurements for hosts containing either nix or win as substring in &#x60;os&#x60; metadata. Note that &#x60;AND&#x60; operation has higher priority than &#x60;OR&#x60;. Allowed keys: &#x60;metric_id&#x60;, &#x60;description&#x60;, &#x60;complex&#x60; (metric parameters) and all available host metadata fields.
    :type q: str

    :rtype: List[Host]
    """
    return 'do some magic!'


def post_metric(metric_id, hostname, payload):  # noqa: E501
    """Add complex metric

     # noqa: E501

    :param metric_id: Metric identyfier
    :type metric_id: str
    :param hostname: Target host (domain name)
    :type hostname: str
    :param payload: Complex mertic payload
    :type payload: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        payload = Payload.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'