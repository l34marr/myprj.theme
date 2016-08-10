# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from myprj.theme.testing import MYPRJ_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that myprj.theme is properly installed."""

    layer = MYPRJ_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if myprj.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'myprj.theme'))

    def test_browserlayer(self):
        """Test that IMyprjThemeLayer is registered."""
        from myprj.theme.interfaces import (
            IMyprjThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IMyprjThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MYPRJ_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['myprj.theme'])

    def test_product_uninstalled(self):
        """Test if myprj.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'myprj.theme'))

    def test_browserlayer_removed(self):
        """Test that IMyprjThemeLayer is removed."""
        from myprj.theme.interfaces import IMyprjThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMyprjThemeLayer, utils.registered_layers())
