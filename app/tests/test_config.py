import pytest
from core.config.test import TestSettings

def test_settings(settings):
  """ Test if the configuration is correct. """
  assert isinstance(settings, TestSettings)