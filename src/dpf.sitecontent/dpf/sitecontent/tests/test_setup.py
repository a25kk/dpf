# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dpf.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dpf.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dpf.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dpf.sitecontent'))

    def test_uninstall(self):
        """Test if dpf.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['dpf.sitecontent'])
        self.assertFalse(self.installer.isProductInstalled('dpf.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDpfSitecontentLayer is registered."""
        from dpf.sitecontent.interfaces import IDpfSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IDpfSitecontentLayer in utils.registered_layers())
