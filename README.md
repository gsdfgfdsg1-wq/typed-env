# typed-env

A dependency-free typed environment validator with safe diagnostics for sensitive configuration.

## Quick start

```bash
python typed_env.py schema.json values.json --environment production
```

Schemas declare required settings, primitive types, defaults, sensitivity, and allowed environments. Diagnostics return `set` for sensitive values rather than the supplied value.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
