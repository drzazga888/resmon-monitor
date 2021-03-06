# coding: utf-8

from __future__ import absolute_import

from typing import List, Dict  # noqa: F401

from rest_api.swagger_server.models.base_model_ import Model
from rest_api.swagger_server.models.metadata import Metadata  # noqa: F401,E501
from rest_api.swagger_server.models.metric import Metric  # noqa: F401,E501
from rest_api.swagger_server import util


class Host(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, hostname: str=None, metrics: List[Metric]=None, metadata: List[Metadata]=None):  # noqa: E501
        """Host - a model defined in Swagger

        :param hostname: The hostname of this Host.  # noqa: E501
        :type hostname: str
        :param metrics: The metrics of this Host.  # noqa: E501
        :type metrics: List[Metric]
        :param metadata: The metadata of this Host.  # noqa: E501
        :type metadata: List[Metadata]
        """
        self.swagger_types = {
            'hostname': str,
            'metrics': List[Metric],
            'metadata': List[Metadata]
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'metrics': 'metrics',
            'metadata': 'metadata'
        }

        self._hostname = hostname
        self._metrics = metrics
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'Host':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Host of this Host.  # noqa: E501
        :rtype: Host
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hostname(self) -> str:
        """Gets the hostname of this Host.

        Domain name for host  # noqa: E501

        :return: The hostname of this Host.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname: str):
        """Sets the hostname of this Host.

        Domain name for host  # noqa: E501

        :param hostname: The hostname of this Host.
        :type hostname: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def metrics(self) -> List[Metric]:
        """Gets the metrics of this Host.

        Array of metrics (both complex and basic)  # noqa: E501

        :return: The metrics of this Host.
        :rtype: List[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List[Metric]):
        """Sets the metrics of this Host.

        Array of metrics (both complex and basic)  # noqa: E501

        :param metrics: The metrics of this Host.
        :type metrics: List[Metric]
        """
        if metrics is None:
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def metadata(self) -> List[Metadata]:
        """Gets the metadata of this Host.

        Various host properties eg. os, unit specification  # noqa: E501

        :return: The metadata of this Host.
        :rtype: List[Metadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: List[Metadata]):
        """Sets the metadata of this Host.

        Various host properties eg. os, unit specification  # noqa: E501

        :param metadata: The metadata of this Host.
        :type metadata: List[Metadata]
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
