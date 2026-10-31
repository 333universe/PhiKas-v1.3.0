import unittest
import json
from phikas.orchestrator import UnifiedFinOpsOrchestrator
from phikas.exceptions import AuthenticationError

class TestPhiKasEngine(unittest.TestCase):
    def setUp(self):
        self.orchestrator = UnifiedFinOpsOrchestrator(resource_threshold_pct=5.0)

    def test_deduplication_integrity(self):
        raw_lines = [
            "2026-10-30 | US-EAST4-B | STORAGE | Bucket 'user-assets-temp-backup': 450 TB, 0 access requests over 90 days.",
            "2026-10-30 | US-EAST4-B | STORAGE | Bucket 'user-assets-temp-backup': 450 TB, 0 access requests over 90 days."
        ]
        elements = [self.orchestrator.process_stream_element(line) for line in raw_lines]
        self.assertFalse(elements[0]["duplicate"])
        self.assertTrue(elements[1]["duplicate"])

    def test_invalid_hmac_exception(self):
        with self.assertRaises(AuthenticationError):
            self.orchestrator.verify_ingress_auth(b"dummy_payload", "invalid_signature_string")

if __name__ == "__main__":
    unittest.main()
