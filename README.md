# stapel-social

Composite: social surface — chat + profiles + reviews.

> Likes/favourites are NOT included yet: `stapel-engagement` does not
> exist. They arrive as a MINOR bump of this composite once it does.

## Assemble (one line)

```bash
pip install stapel-tools
stapel-assemble mysocial --libs social
cd mysocial && make test
```

That expands `social` through the STAPEL_LIBS `requires`
closure and wires every member module into INSTALLED_APPS,
requirements.txt, urls.py and CONFIG.MD, then runs the verify gates.

## Manual wiring (no scaffold)

```python
# settings.py
from stapel_social import preset

INSTALLED_APPS = [
    # ... django/stapel-core baseline (incl. stapel_core.django.projections)
    "stapel_chat",
    "stapel_profiles",
    "stapel_reviews",
    "stapel_social",
]
for _k, _v in preset.SETTINGS_DEFAULTS.items():
    globals().setdefault(_k, _v)

# urls.py
from django.urls import include, path

urlpatterns = [
    path("chat/", include("stapel_chat.urls")),
    path("profiles/api/", include("stapel_profiles.urls")),
    path("reviews/", include("stapel_reviews.urls")),
]
```

## Config checklist (fill these, in the generated project's CONFIG.MD too)

| Key | Note |
|-----|------|
| `STAPEL_REVIEWS["TARGET_TYPES"]` | prefilled by `stapel_social.preset.SETTINGS_DEFAULTS` (targets `profile`) |
| `STAPEL_CHAT[...]` | see stapel-chat CONFIG.MD |
| `STAPEL_PROFILES[...]` | see stapel-profiles CONFIG.MD |
