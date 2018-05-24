# -*- coding: utf-8 -*-
"""Module providing embedable cards"""
from Acquisition import aq_inner
from Products.Five.browser import BrowserView


class NewsItemCardView(BrowserView):
    """ Embeddable preview card for news items """

    def has_image(self):
        context = aq_inner(self.context)
        try:
            lead_img = context.image
        except AttributeError:
            lead_img = None
        if lead_img is not None:
            return True
        return False


class NewsItemCardPreview(BrowserView):
    """Preview embeddable news item preview cards"""

    def __call__(self):
        return self.render()

    def render(self):
        return self.index()

    def rendered_card(self):
        context = aq_inner(self.context)
        template = context.restrictedTraverse('@@card-news-item')()
        return template
