# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from wavefront_api_client.models.azure_base_credentials import AzureBaseCredentials  # noqa: F401,E501


class AzureConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base_credentials': 'AzureBaseCredentials',
        'metric_filter_regex': 'str',
        'category_filter': 'list[str]',
        'resource_group_filter': 'list[str]'
    }

    attribute_map = {
        'base_credentials': 'baseCredentials',
        'metric_filter_regex': 'metricFilterRegex',
        'category_filter': 'categoryFilter',
        'resource_group_filter': 'resourceGroupFilter'
    }

    def __init__(self, base_credentials=None, metric_filter_regex=None, category_filter=None, resource_group_filter=None):  # noqa: E501
        """AzureConfiguration - a model defined in Swagger"""  # noqa: E501

        self._base_credentials = None
        self._metric_filter_regex = None
        self._category_filter = None
        self._resource_group_filter = None
        self.discriminator = None

        if base_credentials is not None:
            self.base_credentials = base_credentials
        if metric_filter_regex is not None:
            self.metric_filter_regex = metric_filter_regex
        if category_filter is not None:
            self.category_filter = category_filter
        if resource_group_filter is not None:
            self.resource_group_filter = resource_group_filter

    @property
    def base_credentials(self):
        """Gets the base_credentials of this AzureConfiguration.  # noqa: E501


        :return: The base_credentials of this AzureConfiguration.  # noqa: E501
        :rtype: AzureBaseCredentials
        """
        return self._base_credentials

    @base_credentials.setter
    def base_credentials(self, base_credentials):
        """Sets the base_credentials of this AzureConfiguration.


        :param base_credentials: The base_credentials of this AzureConfiguration.  # noqa: E501
        :type: AzureBaseCredentials
        """

        self._base_credentials = base_credentials

    @property
    def metric_filter_regex(self):
        """Gets the metric_filter_regex of this AzureConfiguration.  # noqa: E501

        A regular expression that a metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :return: The metric_filter_regex of this AzureConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._metric_filter_regex

    @metric_filter_regex.setter
    def metric_filter_regex(self, metric_filter_regex):
        """Sets the metric_filter_regex of this AzureConfiguration.

        A regular expression that a metric name must match (case-insensitively) in order to be ingested  # noqa: E501

        :param metric_filter_regex: The metric_filter_regex of this AzureConfiguration.  # noqa: E501
        :type: str
        """

        self._metric_filter_regex = metric_filter_regex

    @property
    def category_filter(self):
        """Gets the category_filter of this AzureConfiguration.  # noqa: E501

        A list of Azure services (such as Microsoft.Compute/virtualMachines, Microsoft.Cache/redis etc) from which to pull metrics.  # noqa: E501

        :return: The category_filter of this AzureConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_filter

    @category_filter.setter
    def category_filter(self, category_filter):
        """Sets the category_filter of this AzureConfiguration.

        A list of Azure services (such as Microsoft.Compute/virtualMachines, Microsoft.Cache/redis etc) from which to pull metrics.  # noqa: E501

        :param category_filter: The category_filter of this AzureConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._category_filter = category_filter

    @property
    def resource_group_filter(self):
        """Gets the resource_group_filter of this AzureConfiguration.  # noqa: E501

        A list of Azure resource groups from which to pull metrics.  # noqa: E501

        :return: The resource_group_filter of this AzureConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_group_filter

    @resource_group_filter.setter
    def resource_group_filter(self, resource_group_filter):
        """Sets the resource_group_filter of this AzureConfiguration.

        A list of Azure resource groups from which to pull metrics.  # noqa: E501

        :param resource_group_filter: The resource_group_filter of this AzureConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._resource_group_filter = resource_group_filter

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AzureConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other