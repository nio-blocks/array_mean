from nio import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..array_mean_block import ArrayMean


class TestArrayMean(NIOBlockTestCase):

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = ArrayMean()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({'hello': 'nio'})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assert_last_signal_notified(Signal({'hello': 'nio'}))
