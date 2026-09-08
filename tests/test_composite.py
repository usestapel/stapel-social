"""Minimal composite checks: the package imports, the preset is coherent,
the Django app mounts.
"""
from stapel_social import preset


def test_preset_is_coherent():
    # The composite's own app slot is present (glue must live in
    # INSTALLED_APPS — STAPEL_LIBS grabli 5.8) and prefixes are unique.
    assert "stapel_social" in preset.INSTALLED_APPS
    prefixes = [p for p, _ in preset.URL_INCLUDES]
    assert len(prefixes) == len(set(prefixes))
    # The composite mounts no urls of its own (http=False — glue only).
    assert not any(m.startswith("stapel_social") for _, m in preset.URL_INCLUDES)


def test_app_config_mounts():
    from django.apps import apps

    cfg = apps.get_app_config("social")
    assert cfg.name == "stapel_social"


def test_refusal_envelope_is_wired_in_this_harness():
    """The suite's own settings reach core's DRF exception handler.

    stapel-social is a composite preset: it mounts no urls of its own, so
    there is no protected endpoint here to fire an unauthenticated request
    at. The seam is asserted directly instead — core's system check reads
    ``rest_framework.settings.api_settings``, i.e. what DRF will actually
    call, so an absent ``EXCEPTION_HANDLER`` key reads here as DRF's own
    handler and the check reports it. Before this harness carried the key,
    this failed with stapel_core.error_envelope.W001.
    """
    from stapel_core.django.exception_handler_checks import (
        W001_HANDLER_BYPASSED,
        check_exception_handler_wired,
        effective_handler,
        reaches_core_handler,
    )

    assert [m.id for m in check_exception_handler_wired()] == []
    assert W001_HANDLER_BYPASSED  # the id this guards against
    assert reaches_core_handler(effective_handler())
