"""Synthetic checklist contracts, not natural-language agent or hardware evaluation."""
import copy
import unittest

from wiiready.__main__ import journey


class AgentCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.answers = dict(model='original', menu='4.3U', computer='linux',
                            homebrew='no', sd='yes', storage='sd', gamecube='no')
        self.saved = journey(self.answers)
        # Synthetic prerequisite attestations; no actual storage is inspected.
        for checkpoint in ['review', 'storage-review']:
            self.saved = journey(self.answers, self.saved, checkpoint, 'user-confirmed')
        self.prerequisites = copy.deepcopy(self.saved['state']['completed'])

    def test_repeated_reads_without_attestation_never_advance(self):
        before = copy.deepcopy(self.saved)
        for _ in range(3):
            result = journey(self.answers, self.saved)
            self.assertEqual(result['state'], before['state'])
            self.assertEqual(result['next_checkpoint'], before['next_checkpoint'])
            self.assertEqual(result['status'], 'awaiting-user')
            self.assertFalse(result['write_authorized'])
        self.assertEqual(self.saved, before)

    def test_homebrew_requires_console_test_attestation_not_copy_status(self):
        self.assertEqual(self.saved['next_checkpoint']['id'], 'homebrew')
        before = copy.deepcopy(self.saved)
        for level in [None, 'user-confirmed', 'copied', 'probably', '']:
            with self.subTest(level=level), self.assertRaises(ValueError):
                journey(self.answers, self.saved, 'homebrew', level)
        self.assertEqual(self.saved, before)

    def test_cannot_skip_a_pending_console_checkpoint(self):
        for checkpoint in ['backup', 'recovery', 'loader', 'wii-test']:
            with self.subTest(checkpoint=checkpoint), self.assertRaises(ValueError):
                journey(self.answers, self.saved, checkpoint, 'console-tested')
        self.assertEqual(self.saved['state']['completed'], self.prerequisites)

    def test_hardware_change_requires_review_even_without_advancing(self):
        for changes in [dict(model='vwii'), dict(menu='4.3E'), dict(storage='usb-hdd')]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                journey(dict(self.answers, **changes), self.saved)
        self.assertEqual(self.saved['state']['completed'], self.prerequisites)

    def test_explicit_attestation_advances_only_one_checkpoint(self):
        # Invented attestation demonstrates the API contract, not actual observation.
        result = journey(dict(self.answers, homebrew='yes'), self.saved,
                         'homebrew', 'console-tested')
        self.assertEqual(result['state']['completed'],
                         self.prerequisites + [{'id': 'homebrew', 'evidence': 'console-tested'}])
        self.assertEqual(result['next_checkpoint']['id'], 'backup')
        self.assertFalse(result['write_authorized'])
        self.assertFalse(result['installation_supported'])
        self.assertEqual(self.saved['state']['completed'], self.prerequisites)
