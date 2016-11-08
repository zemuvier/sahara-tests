#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from os import path
from os import remove
import re

from sahara_tempest_plugin.tests.cli import base


class SaharaPluginCLITest(base.ClientTestBase):

    def openstack_plugin_list(self):
        self.assertTableStruct(self.listing_result('plugin list'), [
            'Name',
            'Versions'
        ])

    def openstack_plugin_show(self):
        list_plugin = self.listing_result('plugin list')
        name = [p['Name'] for p in list_plugin]
        if len(name) == 0:
            raise self.skipException('No plugins to show')
        self.assertTableStruct(
            self.listing_result(''.join(['plugin show ', name[0]])), [
                'Field',
                'Value'
            ])

    def openstack_plugin_configs_get(self):
        list_plugin = self.listing_result('plugin list')
        name = [p['Name'] for p in list_plugin]
        version = [p['Versions'] for p in list_plugin]
        if len(name) == 0:
            raise self.skipException('No plugin to get configs')
        plugin_name = name[0]
        outmsg = self.openstack('dataprocessing plugin configs get',
                                params=''.join([plugin_name, ' ',
                                               version[0]]))
        outfile_match = re.search('configs was saved in "(.+)"', outmsg)
        if outfile_match:
            configs_file = outfile_match.group(1)
        else:
            configs_file = '%s_%s' % (plugin_name, version[0])

        result = path.exists(configs_file)
        self.assertTrue(result)
        remove(configs_file)
