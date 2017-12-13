# ----------------------------------------------------------------------------
# Copyright (c) 2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime2.plugin.model as model


class CutadaptStatsFmt(model.TextFileFormat):
    def sniff(self):
        return self.path.stat().st_size > 0


CutadaptStatsDirFmt = model.SingleFileDirectoryFormat(
    'CutadaptStatsDirFmt', 'stats.tsv', CutadaptStatsFmt)
