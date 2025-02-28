import os
import unittest
import collections.abc

from threatexchange.api import ThreatExchangeAPI, ThreatPrivacyGroup

THREAT_EXCHANGE_INTEGRATION_TEST_TOKEN = os.getenv(
    "THREAT_EXCHANGE_INTEGRATION_TEST_TOKEN"
)


@unittest.skipUnless(
    THREAT_EXCHANGE_INTEGRATION_TEST_TOKEN,
    "Integration Test requires tokens. Use THREAT_EXCHANGE_INTEGRATION_TEST_TOKEN environment variable.",
)
class APIIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.api = ThreatExchangeAPI(THREAT_EXCHANGE_INTEGRATION_TEST_TOKEN)

    def test_get_threat_privacy_groups_member(self):
        """
        Assumes that the app (if token is provided) will have at least one
        privacy group.
        """
        response = self.api.get_threat_privacy_groups_member()
        self.assertTrue(
            isinstance(response, collections.abc.Sequence)
            and not isinstance(response, staticmethod),
            "API returned something that's not a list!",
        )

        self.assertTrue(isinstance(response[0], ThreatPrivacyGroup))
