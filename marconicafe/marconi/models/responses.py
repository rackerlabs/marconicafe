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
import re

from marconicafe.marconi.common.models import BaseMarconiModel


class Resources(BaseMarconiModel):
    @classmethod
    def _dict_to_obj(cls, data_dict):
        resources = cls()
        data_dict = data_dict.get('resources')
        for key, value in data_dict.items():
            name = re.sub("[^a-zA-Z]", "_", key)
            setattr(resources, name, Resource._dict_to_obj(value))
        return resources


class Resource(BaseMarconiModel):
    def __init__(self, href_template=None, href_vars=None, hints=None):
        self.href_template = href_template
        self.href_vars = href_vars
        self.hints = hints

    @classmethod
    def _dict_to_obj(cls, data_dict):
        return cls(
            href_template=data_dict.get("href-template"),
            href_vars=data_dict.get("href-vars"),
            hints=HintsModel._dict_to_obj(data_dict.get("hints")))


class HintsModel(BaseMarconiModel):
    def __init__(self, allow=None, formats=None):
        self.allow = allow
        self.formats = formats

    @classmethod
    def _dict_to_obj(cls, data_dict):
        return cls(
            allow=data_dict.get("allow"),
            formats=data_dict.get("formats"))
