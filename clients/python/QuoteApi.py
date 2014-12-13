#!/usr/bin/env python
"""
WordAPI.py
Copyright 2014 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class QuoteApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def getBucketed(self, symbol, **kwargs):
        """Get previous quotes bucketed by seconds.

        Args:
            symbol, str: Instrument name. (required)

            startTime, datetime: Start date. Expects ISO formatted date strings. (optional)

            endTime, datetime: End Date. Expects ISO formatted date strings. (optional)

            count, float: Number of buckets to fetch. (optional)

            binSize, str: Time interval to bucket by. Available options: ['1m', '5m', '1h', '1d']. (optional)

            

        Returns: Array[Quote]
        """

        allParams = ['symbol', 'startTime', 'endTime', 'count', 'binSize']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBucketed" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/quote/bucketed'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('symbol' in params):
            queryParams['symbol'] = self.apiClient.toPathValue(params['symbol'])
        if ('binSize' in params):
            queryParams['binSize'] = self.apiClient.toPathValue(params['binSize'])
        if ('startTime' in params):
            queryParams['startTime'] = self.apiClient.toPathValue(params['startTime'])
        if ('endTime' in params):
            queryParams['endTime'] = self.apiClient.toPathValue(params['endTime'])
        if ('count' in params):
            queryParams['count'] = self.apiClient.toPathValue(params['count'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[Quote]')
        return responseObject
        

        

    




