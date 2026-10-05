from settings import Settings


def test_settings_loaded_from_test_env():
    settings = Settings()  # type: ignore[call-arg]

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "test_app"
    assert settings.API_KEY == "fake_test_api_key"
