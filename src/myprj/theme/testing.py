# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import myprj.theme


class MyprjThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=myprj.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'myprj.theme:default')


MYPRJ_THEME_FIXTURE = MyprjThemeLayer()


MYPRJ_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MYPRJ_THEME_FIXTURE,),
    name='MyprjThemeLayer:IntegrationTesting'
)


MYPRJ_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MYPRJ_THEME_FIXTURE,),
    name='MyprjThemeLayer:FunctionalTesting'
)


MYPRJ_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MYPRJ_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MyprjThemeLayer:AcceptanceTesting'
)
