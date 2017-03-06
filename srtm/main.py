# -*- coding: utf-8 -*-

# Copyright 2013 Tomo Krajina
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json     as mod_json
import os       as mod_os
import os.path  as mod_path

from . import data      as mod_data

def get_data(file_handler=None):
    """
    Get the utility object for querying elevation data.

    If you need to change the way the files are saved locally (for example if
    you need to save them locally) -- change the file_handler. See
    srtm.main.FileHandler.
    """
    if not file_handler:
        file_handler = FileHandler()

    return mod_data.GeoElevationData(file_handler=file_handler)

class FileHandler:
    """
    The default file handler. It can be changed if you need to save/read SRTM
    files in a database or Amazon S3.
    """

    def get_srtm_dir(self):
        """ The default path to store files. """
        return "/data/srtm1"

    def exists(self, file_name):
        return mod_path.exists('%s/%s' % (self.get_srtm_dir(), file_name))

    def write(self, file_name, contents):
        with open('%s/%s' % (self.get_srtm_dir(), file_name), 'wb') as f:
            f.write(contents)

    def read(self, file_name):
        with open('%s/%s' % (self.get_srtm_dir(), file_name), 'rb') as f:
            return f.read()
