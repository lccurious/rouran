# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse201(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, samples: List[str]=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger

        :param name: The name of this InlineResponse201.  # noqa: E501
        :type name: str
        :param samples: The samples of this InlineResponse201.  # noqa: E501
        :type samples: List[str]
        """
        self.swagger_types = {
            'name': str,
            'samples': List[str]
        }

        self.attribute_map = {
            'name': 'name',
            'samples': 'samples'
        }
        self._name = name
        self._samples = samples

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse201':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201 of this InlineResponse201.  # noqa: E501
        :rtype: InlineResponse201
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse201.


        :return: The name of this InlineResponse201.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse201.


        :param name: The name of this InlineResponse201.
        :type name: str
        """

        self._name = name

    @property
    def samples(self) -> List[str]:
        """Gets the samples of this InlineResponse201.


        :return: The samples of this InlineResponse201.
        :rtype: List[str]
        """
        return self._samples

    @samples.setter
    def samples(self, samples: List[str]):
        """Sets the samples of this InlineResponse201.


        :param samples: The samples of this InlineResponse201.
        :type samples: List[str]
        """

        self._samples = samples
