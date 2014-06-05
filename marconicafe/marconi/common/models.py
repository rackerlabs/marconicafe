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

from cafe.engine.models.base import (AutoMarshallingModel,
                                     AutoMarshallingListModel)


class BaseMarconi(object):
    @classmethod
    def _json_to_obj(cls, serialized_str):
        data_dict = json.loads(serialized_str)
        return cls._dict_to_obj(data_dict)

    def _obj_to_json(self):
        return json.dumps(self._obj_to_dict())


class BaseMarconiModel(BaseMarconi, AutoMarshallingModel):
    pass


class BaseMarconiListModel(BaseMarconi, AutoMarshallingListModel):
    pass
