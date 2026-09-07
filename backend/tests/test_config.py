from app.config import Settings


def test_blank_openai_model_uses_the_application_default() -> None:
    settings = Settings(postgres_url="postgresql://example", openai_model="")

    assert settings.openai_model == "gpt-5.4-mini"
