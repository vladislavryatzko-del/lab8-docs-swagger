"""Проверка openapi.yaml: структура OpenAPI 3.x + базовая согласованность.

Запуск:  python scripts/validate_spec.py
Нужно:   pip install openapi-spec-validator pyyaml
"""
import sys
from pathlib import Path

import yaml
from openapi_spec_validator import validate

spec_path = Path(__file__).resolve().parent.parent / "openapi.yaml"
spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))

validate(spec)  # бросит исключение при нарушении структуры OpenAPI

methods = {"get", "post", "put", "patch", "delete"}
ops = [(m.upper(), p, op) for p, item in spec["paths"].items() for m, op in item.items() if m in methods]
ids = [op["operationId"] for _, _, op in ops]
assert len(ids) == len(set(ids)), "operationId должны быть уникальны"
assert len(ops) >= 4, "нужно минимум 4 операции"

print(f"OK: OpenAPI {spec['openapi']}, операций: {len(ops)}, схем: {len(spec['components']['schemas'])}")
for m, p, op in ops:
    print(f"  {m:6} {p:38} {op['operationId']}")
sys.exit(0)
