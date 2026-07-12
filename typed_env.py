#!/usr/bin/env python3
"""Validate typed environment settings without exposing sensitive values."""
import argparse
import json
from pathlib import Path


def validate(schema, values, environment):
    errors, diagnostics = [], {}
    for name, spec in schema.items():
        value = values.get(name, spec.get("default"))
        if environment not in spec.get("environments", [environment]): errors.append(f"not-applicable:{name}"); continue
        if spec.get("required") and value is None: errors.append(f"missing:{name}"); continue
        if value is not None and spec.get("type") == "integer":
            try: int(value)
            except (ValueError, TypeError): errors.append(f"type:{name}")
        if value is not None and spec.get("type") == "boolean" and str(value).lower() not in {"true", "false", "0", "1"}: errors.append(f"type:{name}")
        diagnostics[name] = "set" if spec.get("sensitive") and value is not None else value
    return {"valid": not errors, "errors": errors, "diagnostics": diagnostics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schema"); parser.add_argument("values"); parser.add_argument("--environment", required=True)
    args = parser.parse_args()
    print(json.dumps(validate(json.loads(Path(args.schema).read_text()), json.loads(Path(args.values).read_text()), args.environment), indent=2))


if __name__ == "__main__": main()
