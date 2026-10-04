"""材料寿命证据与可靠性承诺命令行冒烟入口。"""

import json
import sys
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from lifecycle_reliability import ReliabilityClaim


def main() -> None:
    item = ReliabilityClaim(**{'claim_code': 'claim-code-001', 'material_grade': 'material-grade-001', 'use_case': 'use-case-001', 'revision': 1})
    print(json.dumps({"item": asdict(item), "fingerprint": item.fingerprint()}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
