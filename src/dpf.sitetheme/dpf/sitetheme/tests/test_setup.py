# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dpf.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dpf.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dpf.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dpf.buildout'))

    def test_uninstall(self):
        """Test if dpf.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['dpf.buildout'])
        self.assertFalse(self.installer.isProductInstalled('dpf.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDpfBuildoutLayer is registered."""
        from dpf.buildout.interfaces import IDpfBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IDpfBuildoutLayer in utils.registered_layers())
