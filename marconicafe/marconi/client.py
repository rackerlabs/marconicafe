"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import json

from marconicafe.marconi.common.client import BaseMarconiClient
from marconicafe.marconi.models import requests, responses


class MarconiClient(BaseMarconiClient):
    def get_home_document(self, requestslib_kwargs=None):
        return self.get(
            self.url, response_entity_type=responses.Resources,
            requestslib_kwargs=requestslib_kwargs)

    def get_queue_list(
            self, marker=None, limit=None, detailed=None,
            requestslib_kwargs=None):
        url = '{0}/queues'.format(self.url)
        params = {"marker": marker, "limit": limit, "detailed": detailed}
        return self.get(
            url, params=params, requestslib_kwargs=requestslib_kwargs)

    def create_queue(self, queue_name=None, requestslib_kwargs=None):
        url = '{0}/queues/{1}'.format(self.url, queue_name)
        return self.put(url, requestslib_kwargs=requestslib_kwargs)

    def delete_queue(self, queue_name=None, requestslib_kwargs=None):
        url = '{0}/queues/{1}'.format(self.url, queue_name)
        return self.delete(url, requestslib_kwargs=requestslib_kwargs)

    def check_queue_exists(self, queue_name=None, requestslib_kwargs=None):
        url = '{0}/queues/{1}'.format(self.url, queue_name)
        return self.get(url, requestslib_kwargs=requestslib_kwargs)

    def set_queue_metadata(
            self, queue_name=None, metadata=None, requestslib_kwargs=None):
        url = '{0}/queues/{1}/metadata'.format(self.url, queue_name)
        data = "" if metadata == None else json.dumps(metadata)
        return self.put(url, data=data, requestslib_kwargs=requestslib_kwargs)

    def get_metadata(self, queue_name=None, requestslib_kwargs=None):
        url = '{0}/queues/{1}/metadata'.format(self.url, queue_name)
        return self.get(url, requestslib_kwargs=requestslib_kwargs)

    def get_queue_stats(self, queue_name=None, requestslib_kwargs=None):
        url = '{0}/queues/{1}/stats'.format(self.url, queue_name)
        return self.get(url, #response_entity_type=responses.TenantList,
            requestslib_kwargs=requestslib_kwargs)

    def post_message(self, queue_name, model, requestslib_kwargs=None):
        url = '{0}/queues/{1}/messages'.format(self.url, queue_name)
        headers = {"Client-ID": "4d15e12d-51b9-4590-a8c1-a697a5e55383"}
        return self.post(
            url, request_entity=model, headers=headers,
            requestslib_kwargs=requestslib_kwargs)
"""
POST /v1/queues/{queue_name}/messages Posts the message or messages for a specified queue.
GET /v1/queues/{queue_name}/messages{?
marker,limit,echo,include_claimed}
Gets the message or messages in a specified queue.
GET /v1/queues/{queue_name}/messages{?
ids}
Gets the specified set of messages from the specified
queue.
DELETE /v1/queues/{queue_name}/messages{?
ids}
Bulk-deletes for messages.
GET /v1/queues/{queue_name}/messages/
{messageId}
Shows details for the specified message from the specified
queue.
DELETE /v1/queues/{queue_name}/messages/
{messageId}{?claim_id}
Deletes the specified message from the specified queue.
Claims
POST /v1/queues/{queue_name}/claims{?
limit}
Claims a set of messages from a specified queue.
GET /v1/queues/{queue_name}/claims/
{claimId}
Queries the specified claim for a specified queue.
PATCH /v1/queues/{queue_name}/claims/
{claimId}
Updates the specified claim for a specified queue.
DELETE /v1/queues/{queue_name}/claims/
{claimId}
Releases the specified claim for the specified q"""