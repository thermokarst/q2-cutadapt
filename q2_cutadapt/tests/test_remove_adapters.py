# ----------------------------------------------------------------------------
# Copyright (c) 2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin.testing import TestPluginBase

# from q2_cutadapt import remove_adapters_single


class TestRemoveAdaptersSingle(TestPluginBase):
    package = 'q2_cutadapt.tests'

    def test_remove_three_prime(self):
        pass
