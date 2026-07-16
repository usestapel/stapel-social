# CONFIG.MD — stapel-social

Config registry ({static-scaffold-and-config.md} §2). This composite reads
NO configuration keys of its own — every key belongs to a member module
(chat, profiles, reviews); see each member's CONFIG.MD (the scaffold aggregates them all
into the generated project's CONFIG.MD automatically).

Scenario defaults live in `stapel_social.preset.SETTINGS_DEFAULTS` — they are
settings-dict PRESETS for member keys, not new keys.

## stapel-social

| Key | Source | Purpose | Required | Default |
|-----|--------|---------|----------|---------|
