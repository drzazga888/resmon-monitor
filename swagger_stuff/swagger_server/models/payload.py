# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Payload(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, unit: str=None, moving_window_duration: int=None, interval: int=None):  # noqa: E501
        """Payload - a model defined in Swagger

        :param description: The description of this Payload.  # noqa: E501
        :type description: str
        :param unit: The unit of this Payload.  # noqa: E501
        :type unit: str
        :param moving_window_duration: The moving_window_duration of this Payload.  # noqa: E501
        :type moving_window_duration: int
        :param interval: The interval of this Payload.  # noqa: E501
        :type interval: int
        """
        self.swagger_types = {
            'description': str,
            'unit': str,
            'moving_window_duration': int,
            'interval': int
        }

        self.attribute_map = {
            'description': 'description',
            'unit': 'unit',
            'moving_window_duration': 'moving_window_duration',
            'interval': 'interval'
        }

        self._description = description
        self._unit = unit
        self._moving_window_duration = moving_window_duration
        self._interval = interval

    @classmethod
    def from_dict(cls, dikt) -> 'Payload':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The payload of this Payload.  # noqa: E501
        :rtype: Payload
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this Payload.

        Detailed informations about metric  # noqa: E501

        :return: The description of this Payload.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Payload.

        Detailed informations about metric  # noqa: E501

        :param description: The description of this Payload.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def unit(self) -> str:
        """Gets the unit of this Payload.

        String that should be appended to chart tooltip / legend eq. `%` or `Mb`  # noqa: E501

        :return: The unit of this Payload.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this Payload.

        String that should be appended to chart tooltip / legend eq. `%` or `Mb`  # noqa: E501

        :param unit: The unit of this Payload.
        :type unit: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def moving_window_duration(self) -> int:
        """Gets the moving_window_duration of this Payload.

        Duration of moving window in seconds  # noqa: E501

        :return: The moving_window_duration of this Payload.
        :rtype: int
        """
        return self._moving_window_duration

    @moving_window_duration.setter
    def moving_window_duration(self, moving_window_duration: int):
        """Sets the moving_window_duration of this Payload.

        Duration of moving window in seconds  # noqa: E501

        :param moving_window_duration: The moving_window_duration of this Payload.
        :type moving_window_duration: int
        """
        if moving_window_duration is None:
            raise ValueError("Invalid value for `moving_window_duration`, must not be `None`")  # noqa: E501

        self._moving_window_duration = moving_window_duration

    @property
    def interval(self) -> int:
        """Gets the interval of this Payload.

        Number of seconds between each new point in produced series  # noqa: E501

        :return: The interval of this Payload.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval: int):
        """Sets the interval of this Payload.

        Number of seconds between each new point in produced series  # noqa: E501

        :param interval: The interval of this Payload.
        :type interval: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval
