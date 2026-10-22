"""The preset's profile review type works end to end: the profile's user can
reply, a stranger cannot, and nobody reviews their own profile (SO-2)."""
import pytest

from stapel_social import preset


@pytest.fixture
def profile_type(settings):
    settings.STAPEL_REVIEWS = dict(preset.SETTINGS_DEFAULTS["STAPEL_REVIEWS"])


def _user(name):
    from django.contrib.auth import get_user_model

    return get_user_model().objects.create_user(
        username=name, email=f"{name}@example.com", password="x"
    )


@pytest.mark.django_db
def test_the_profile_user_replies(profile_type):
    from stapel_reviews import services

    author, subject = _user("author"), _user("subject")
    review = services.create_review(
        target_type="profile", target_key=str(subject.pk), author=author, rating=5
    )
    response = services.respond(review, author=subject, body="thank you")
    assert response.author_id == subject.pk


@pytest.mark.django_db
def test_a_stranger_cannot_reply(profile_type):
    from stapel_reviews import services

    author, subject, stranger = _user("author"), _user("subject"), _user("stranger")
    review = services.create_review(
        target_type="profile", target_key=str(subject.pk), author=author, rating=5
    )
    with pytest.raises(services.NotAllowedToModerate):
        services.respond(review, author=stranger, body="me")


@pytest.mark.django_db
def test_nobody_reviews_their_own_profile(profile_type):
    from stapel_reviews import services

    me = _user("me")
    with pytest.raises(services.SelfReview):
        services.create_review(
            target_type="profile", target_key=str(me.pk), author=me, rating=5
        )
