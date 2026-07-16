"""Preset for the "social" scenario — plain data, importable without
Django settings (projections-and-composition §3).

Scenario: a social surface around any entity: chat/messaging + user profiles + reviews.

A generated project (stapel-assemble … --libs social) gets the
same wiring from the STAPEL_LIBS registry; this module is the single source
a hand-written settings.py/urls.py copies from instead.
"""

# Dotted app paths, in mount order. L1 libraries (stapel-attributes) are pip
# dependencies, NOT Django apps — deliberately absent here.
INSTALLED_APPS = [
    "stapel_chat",
    "stapel_profiles",
    "stapel_reviews",
    "stapel_social",
]

# (url_prefix, urlconf_module) — mount each one with
#   path(prefix, include(module))
# The composite itself mounts NO urls (http=False): it only carries glue.
URL_INCLUDES = [
    ("chat/", "stapel_chat.urls"),
    ("profiles/api/", "stapel_profiles.urls"),
    ("reviews/", "stapel_reviews.urls"),
]

# Scenario defaults for STAPEL_<MOD> settings dicts. Merge them into the
# project's settings, e.g.:
#   from stapel_social import preset
#   STAPEL_REVIEWS = {**preset.SETTINGS_DEFAULTS.get("STAPEL_REVIEWS", {})}
SETTINGS_DEFAULTS = {
    "STAPEL_REVIEWS": {
        # reviews is target-generic and ships an EMPTY TARGET_TYPES registry;
        # the composite is the place that knows both sides, so the scenario
        # default targets user profiles out of the box.
        "TARGET_TYPES": {
            "profile": {
                "moderation": "post",
                "one_per_author": True,
                "allow_response": True,
                # Host policy callbacks (comm Functions) are None by default:
                # any authenticated user may review. Register and name your
                # own "can_review"/"can_moderate" Functions to restrict.
            },
        },
    },
}
