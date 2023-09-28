# -*- coding: utf-8 -*-

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model


class StandardisedProtocolDataOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, standard_data_protocol: str = None):  # noqa: E501
        """StandardisedProtocolDataOutput - a model defined in Swagger

        :param standard_data_protocol: The standard_data_protocol of this StandardisedProtocolDataOutput.  # noqa: E501
        :type standard_data_protocol: str
        """
        self.swagger_types = {"standard_data_protocol": str}

        self.attribute_map = {"standard_data_protocol": "standard_data_protocol"}
        self._standard_data_protocol = standard_data_protocol

    @classmethod
    def from_dict(cls, dikt) -> "StandardisedProtocolDataOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StandardisedProtocolData_output of this StandardisedProtocolDataOutput.  # noqa: E501
        :rtype: StandardisedProtocolDataOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def standard_data_protocol(self) -> str:
        """Gets the standard_data_protocol of this StandardisedProtocolDataOutput.


        :return: The standard_data_protocol of this StandardisedProtocolDataOutput.
        :rtype: str
        """
        return self._standard_data_protocol

    @standard_data_protocol.setter
    def standard_data_protocol(self, standard_data_protocol: str):
        """Sets the standard_data_protocol of this StandardisedProtocolDataOutput.


        :param standard_data_protocol: The standard_data_protocol of this StandardisedProtocolDataOutput.
        :type standard_data_protocol: str
        """

        self._standard_data_protocol = standard_data_protocol
