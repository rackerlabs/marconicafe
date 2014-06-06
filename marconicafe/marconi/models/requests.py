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
from marconicafe.marconi.common.models import (
    BaseMarconiModel, BaseMarconiListModel)


class MessageModel(BaseMarconiModel):

    def __init__(
            self, ttl=None, body=None):
        super(MessageModel, self).__init__()
        self.ttl = ttl
        self.body = body

    def _obj_to_dict(self):
        return {"ttl": self.ttl, "body": self.body}


class MessageListModel(BaseMarconiListModel):
    def _obj_to_dict(self):
        ret_val = []
        for model in self:
            ret_val.append(model._obj_to_dict())
        return ret_val
