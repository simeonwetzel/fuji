# -*- coding: utf-8 -*-

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model


class DataProvenanceOutputInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, is_available: bool = True, provenance_metadata: List[Dict[str, str]] = None):  # noqa: E501
        """DataProvenanceOutputInner - a model defined in Swagger

        :param is_available: The is_available of this DataProvenanceOutputInner.  # noqa: E501
        :type is_available: bool
        :param provenance_metadata: The provenance_metadata of this DataProvenanceOutputInner.  # noqa: E501
        :type provenance_metadata: List[Dict[str, str]]
        """
        self.swagger_types = {"is_available": bool, "provenance_metadata": List[Dict[str, str]]}

        self.attribute_map = {"is_available": "is_available", "provenance_metadata": "provenance_metadata"}
        self._is_available = is_available
        self._provenance_metadata = provenance_metadata

    @classmethod
    def from_dict(cls, dikt) -> "DataProvenanceOutputInner":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataProvenance_output_inner of this DataProvenanceOutputInner.  # noqa: E501
        :rtype: DataProvenanceOutputInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_available(self) -> bool:
        """Gets the is_available of this DataProvenanceOutputInner.


        :return: The is_available of this DataProvenanceOutputInner.
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available: bool):
        """Sets the is_available of this DataProvenanceOutputInner.


        :param is_available: The is_available of this DataProvenanceOutputInner.
        :type is_available: bool
        """

        self._is_available = is_available

    @property
    def provenance_metadata(self) -> List[Dict[str, str]]:
        """Gets the provenance_metadata of this DataProvenanceOutputInner.


        :return: The provenance_metadata of this DataProvenanceOutputInner.
        :rtype: List[Dict[str, str]]
        """
        return self._provenance_metadata

    @provenance_metadata.setter
    def provenance_metadata(self, provenance_metadata: List[Dict[str, str]]):
        """Sets the provenance_metadata of this DataProvenanceOutputInner.


        :param provenance_metadata: The provenance_metadata of this DataProvenanceOutputInner.
        :type provenance_metadata: List[Dict[str, str]]
        """

        self._provenance_metadata = provenance_metadata
