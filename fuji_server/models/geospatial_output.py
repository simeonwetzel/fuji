# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from datetime import date, datetime  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model


class GeospatialOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):
        """GeospatialOutput - a model defined in Swagger"""
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "GeospatialOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RelatedResource_output of this GeospatialOutput.  # noqa: E501
        :rtype: GeospatialOutput
        """
        return util.deserialize_model(dikt, cls)
