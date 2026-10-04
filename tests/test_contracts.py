"""材料寿命证据与可靠性承诺基础契约测试。"""

import unittest

from lifecycle_reliability import ReliabilityClaim, unique_by_identity


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.values = {'claim_code': 'claim-code-001', 'material_grade': 'material-grade-001', 'use_case': 'use-case-001', 'revision': 1}

    def test_fingerprint_is_stable(self) -> None:
        left = ReliabilityClaim(**self.values)
        right = ReliabilityClaim(**dict(reversed(list(self.values.items()))))
        self.assertEqual(left.fingerprint(), right.fingerprint())

    def test_evolve_keeps_original(self) -> None:
        original = ReliabilityClaim(**self.values)
        change_key = next(key for key, value in self.values.items() if isinstance(value, str))
        changed = original.evolve(**{change_key: "revised-value"})
        self.assertNotEqual(original.fingerprint(), changed.fingerprint())
        self.assertEqual(getattr(original, change_key), self.values[change_key])

    def test_conflicting_identity_is_rejected(self) -> None:
        first = ReliabilityClaim(**self.values)
        changed_values = dict(self.values)
        change_key = next(key for key in self.values if key != "claim_code")
        changed_values[change_key] = 2 if isinstance(changed_values[change_key], int) else "conflict"
        second = ReliabilityClaim(**changed_values)
        with self.assertRaises(ValueError):
            unique_by_identity([first, second])


if __name__ == "__main__":
    unittest.main()
