#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from apiplayground import APIPlayground


class VoipCallBilledAPIPlayground(APIPlayground):
    """
    To test CDR api in broswer

        ``URL`` : http://127.0.0.1:8000/api-explorer/voip-call-billed/
    """

    schema = {
        "title": "Voip call billed API Playground",
        "base_url": "http://localhost/api/v1/",
        "resources": [
            {
                "name": "/voip_call_billed/",
                "description": "This resource allows you to bill voip call.",
                "endpoints": [
                    {
                        "method": "POST",
                        "url": "/api/v1/voip_call_billed/",
                        "description": "Creates new billed voip call",
                        "parameters": [{
                                           "name": "recipient_phone_no",
                                           "type": "string",
                                           "is_required": True,
                                           "default": "34657077888"
                                       },
                                       {
                                           "name": "sender_phone_no",
                                           "type": "string",
                                           "default": "48092924"
                                       },
                                       {
                                           "name": "disposition",
                                           "type": "string",
                                           "default": "1"
                                       },
                                       {
                                           "name": "call_date",
                                           "type": "string",
                                           "default": "2013-01-11 11:11:22"
                                       },
                                       ]
                    },
                    ]
            },
            ]
    }
