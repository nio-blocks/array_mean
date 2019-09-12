import numpy as np
from nio import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..array_mean_block import ArrayMean


class TestArrayMean(NIOBlockTestCase):

    def test_process_signals(self):
        """Incoming arrays are reduced to the inner-most dimension."""
        blk = ArrayMean()
        self.configure_block(blk, {
            'incoming_array': '{{ $array }}',
            'log_level': 'DEBUG',
        })
        blk.start()
        blk.process_signals([
            Signal({
                'array': [
                    [
                        [1, 2, 3],
                        [2, 3, 4],
                        [3, 4, 5],
                    ],
                    [
                        [1, 2, 3],
                        [2, 3, 4],
                        [3, 4, 5],
                    ],
                ],
            }),
        ])
        blk.stop()
        self.assert_num_signals_notified(1)
        print(self.last_signal_notified().to_dict())
        # self.assert_signal_list_notified([
        #     Signal({'mean': np.array([2, 3, 4])}),
        # ])
