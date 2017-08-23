# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Crawler implementation. """


# TODO: The next editor must remove this disable and correct issues.
# pylint: disable=missing-type-doc,missing-return-type-doc,missing-return-doc
# pylint: disable=missing-param-doc


class Storage(object):

    def open(self, handle=None):
        raise NotImplementedError()

    def write(self, resource):
        raise NotImplementedError()

    def read(self, resource_key):
        raise NotImplementedError()

    def error(self, message):
        raise NotImplementedError()

    def warning(self, message):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def commit(self):
        raise NotImplementedError()

    def rollback(self):
        raise NotImplementedError()


class Memory(Storage):
    HANDLE = 0

    def __init__(self):
        super(Memory, self).__init__()
        self.mem = {}

    def open(self, handle=None):
        handle = self.HANDLE if handle is None else handle
        self.HANDLE += 1
        return handle

    def write(self, resource):
        self.mem[resource.key()] = resource

    def read(self, resource_key):
        return self.mem[resource_key]

    def error(self, message):
        pass

    def warning(self, message):
        pass

    def close(self):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type_p, value, tb):
        self.close()

    def commit(self):
        pass

    def rollback(self):
        pass