#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import


class Attendee(object):

    """An event attendee.
    """

    def __init__(self,
                 value,
                 calendar_user_type='INDIVIDUAL',
                 group_or_list_membership=None,
                 participation_role=None,
                 participation_status='NEEDS-ACTION',
                 rsvp_expectation=False,
                 delegatess=None,
                 delegators=None,
                 sent_by=None,
                 common_name=None,
                 directory_entry_reference=None,
                 language=None):
        """Instantiates a new :class:`ics.attendee.Attendee`.

        Args:
            calendar_user_type (stirng) : rfc5545 CUTYPE property
            group_or_list_membership
            ... TODO
        """
        self.value = value
        self.calendar_user_type = calendar_user_type
        self.group_or_list_membership = group_or_list_membership
        self.participation_role = participation_role
        self.participation_status = participation_status
        self.rsvp_expectation = rsvp_expectation
        self.delegatess = delegatess
        self.delegators = delegators
        self.sent_by = sent_by
        self.common_name = common_name
        self.directory_entry_reference = directory_entry_reference
        self.language = language
