# ----------------------------------------------------------------------------
# Copyright (c) 2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import q2_cutadapt

from qiime2.plugin import Plugin, Str
from q2_types.per_sample_sequences import SequencesWithQuality
from q2_types.sample_data import SampleData


plugin = Plugin(
    name='cutadapt',
    version=q2_cutadapt.__version__,
    website='https://github.com/qiime2/q2-cutadapt',
    package='q2_cutadapt',
    description='This QIIME 2 plugin supports removing adapters, primers, '
                'and other unwanted sequences from sequence data.',
    short_description='Plugin for removing unwanted sequences from sequence '
                      'data.',
)

plugin.methods.register_function(
    function=q2_cutadapt.remove_adapters_single,
    inputs={
        'sequences': SampleData[SequencesWithQuality],
    },
    parameters={
        'three_prime': Str,
        'five_prime': Str,
        'search_both': Str,
    },
    outputs=[('cleaned_sequences', SampleData[SequencesWithQuality])],
    input_descriptions={
        'sequences': 'The single-end sequences to remove adapters from.',
    },
    parameter_descriptions={
        'three_prime': 'The DNA to remove from the 3\' end of the sequences.',
        'five_prime': 'The DNA to remove from the 5\' end of the sequences.',
        'search_both': 'The DNA to remove from either the 3\' or 5\' end of '
                       'the sequences.',
    },
    output_descriptions={
        'cleaned_sequences': 'The single-end sequences with the specified '
                             'adapters removed.',
    },
    name='Remove unwanted sequences from single-end sequence data.',
    description='This method utilizes cutadapt to remove unwanted sequences '
                'from single-end sequence data. Please see the cutadapt '
                'project\'s documentation for more details.',
)
