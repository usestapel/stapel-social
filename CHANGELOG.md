# Changelog

## [0.1.5] - 2026-08-02

Fix-up: 0.1.4's `publish.yml` test gate installed `pytest`/`pytest-django`
only, unlike `ci.yml` — it never picked up `stapel-tools`, so the new
`docs/llms.txt` drift/determinism tests in `tests/test_contract.py`
failed at the tag-triggered publish workflow (0.1.4 never reached
PyPI). `publish.yml` now installs `stapel-tools` the same way `ci.yml`
does. No other change.

## [0.1.4] - 2026-08-02

Packaging/docs catch-up, no behavior change:

- Canonical `ci.yml` with coverage + `codecov.yml`, Python 3.14
  classifier, badge canon.
- `docs/llms.txt` — the fifth contract artifact (badge-canon §3),
  rendered from the curated (hand-authored) `docs/capabilities.json` by
  `stapel_tools.llms_txt`; `capabilities.json`'s `version` field brought
  in sync with `pyproject.toml` (0.1.2 → 0.1.4), no other change to its
  hand-authored content.

## [0.1.2] - 2026-07-17

Fleet follow-up to stapel-core 0.12.0 (legacy shim sweep). Also re-pins
`stapel-profiles`'s ceiling — it had a breaking bump to 0.4.0 since
0.1.1, outside this composite's old `<0.4` ceiling. Suite green.

### Changed
- `stapel-core` ceiling `<0.12` → `<0.13`.
- `stapel-profiles` ceiling `<0.4` → `<0.5`.

## [0.1.1] - 2026-07-17

### Changed
- `stapel-core` ceiling raised `>=0.10,<0.11` → `>=0.10,<0.12` (core 0.11
  fleet re-pin). Member-module pins (chat, profiles, reviews) already
  satisfied by their own 0.11-fleet patch releases. Suite green as-is.

## [0.1.0] - 2026-07-16

### Added

- Initial composite (projections-and-composition §3): pyproject pins over
  the member modules, `preset` (INSTALLED_APPS/urls/STAPEL_* defaults),
  AppConfig app slot, minimal tests.

### Known gaps

- Likes/favourites wait for `stapel-engagement` (minor bump when it exists).
