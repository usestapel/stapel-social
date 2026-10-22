"""Preset for the "social" scenario — plain data, importable without
Django settings (projections-and-composition §3).

Scenario: a social surface around any entity: chat/messaging + user profiles + reviews.

A generated project (stapel-assemble … --libs social) gets the
same wiring from the STAPEL_LIBS registry; this module is the single source
a hand-written settings.py/urls.py copies from instead.
"""

# Dotted app paths, in mount order. L1 libraries (stapel-attributes) are pip
# dependencies, NOT Django apps — deliberately absent here.
#
# stapel_realtime is chat's WebSocket substrate: stapel_chat.E010 refuses to
# boot without it. The host still supplies CHANNEL_LAYERS, the "channels"
# signal transport and an ASGI router (stapel_realtime.asgi
# build_websocket_application); see stapel-realtime's README.
INSTALLED_APPS = [
    "stapel_profiles",
    "stapel_realtime",
    "stapel_chat",
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
                # A profile's target_key is its user id, so the profile IS its
                # owner: that user may reply to reviews of it and may not
                # review it (stapel-reviews allow_self_review defaults off).
                "owner_key_for": "reviews.owner_is_target",
                # Host policy callbacks (comm Functions) are None by default:
                # any authenticated user may review, nobody may hide. Name
                # your own "can_review"/"can_moderate"/"can_respond"
                # Functions to restrict or widen.
            },
        },
    },
}
