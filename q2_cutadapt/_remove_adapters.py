# ----------------------------------------------------------------------------
# Copyright (c) 2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.per_sample_sequences import (
    SingleLanePerSampleSingleEndFastqDirFmt)


def remove_adapters_single(sequences: SingleLanePerSampleSingleEndFastqDirFmt,
                           three_prime: str=None, five_prime: str=None,
                           search_both: str=None) -> \
                                   SingleLanePerSampleSingleEndFastqDirFmt:
    pass
