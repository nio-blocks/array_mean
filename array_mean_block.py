import numpy as np
from nio import Block
from nio.block.mixins import EnrichSignals
from nio.properties import Property, StringProperty, VersionProperty


class ArrayMean(EnrichSignals, Block):

    incoming_array = Property(
        title='Incoming Array',
        order=0)
    outgoing_attribute = StringProperty(
        title='Outgoing Signal Attribute',
        default='mean',
        order=1)
    version = VersionProperty('0.1.0')

    def process_signal(self, signal):
        array = self.incoming_array(signal)
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        dimensions = len(array.shape)
        self.logger.debug('Reducing {}D matrix'.format(dimensions))
        for r in range(dimensions - 1) or range(1):
            array = array.mean(axis=0)
        attr = self.outgoing_attribute(signal)
        return self.get_output_signal({attr: array}, signal)
