from datetime import datetime
def standard_ticket(support_channel_id, data, priority, steps_to_reproduce, links, user, info, version, goalkeeper, copied_at):

    message = {
            "channel": support_channel_id,
            "attachments": [
                {
                    "mrkdwn_in": ["text", "value"],
                    "color": "#36a64f",
                    "author_name": f"Ticket {data['author_name']['ticket_id']} - {priority}",
                    "title": "Click here to follow the ticket.",
                    "title_link": data["ticket_link"],
                    "fields": [
                        {
                            "title": ":label: Title:",
                            "value": data["fields"]["title"],
                            "short": False
                        },
                        {
                            "title": ":thread: Description:",
                            "value": data["fields"]["description"],
                            "short": False
                        },
                        {
                            "title": ":arrows_counterclockwise: How to reproduce:",
                            "value": steps_to_reproduce,
                            "short": False
                        },
                        {
                            "title": ":link: Links:",
                            "value": f"<{links['view_link']}|View Link> | " \
                                f"<{links['normal_link']}|Assignment Link> | " \
                                f"<https://app.logrocket.com{links['logrocket']}|LogRocket>",
                            "short": True
                        },
                        {
                            "title": ":bust_in_silhouette: User:",
                            "value": user,
                            "short": True
                        },
                        {
                            "title": ":information_source: Task Info:",
                            "value": info,
                            "short": False
                        },
                        {
                            "title": ":1234: Version:",
                            "value": version,
                            "short": False
                        },
                        {
                            "title": ":clock2: Copied At:",
                            "type": "mrkdwn",
                            "value": copied_at,
                            "short": False
                        },
                        {
                            "title": ":goal_net: Goalkeeper:",
                            "value": f"<@{goalkeeper}>",
                            "short": True
                        },
                    ],
                    "footer": "Technical Support Team",
                    "footer_icon": "https://images.crunchbase.com/image/upload/c_pad,f_auto,q_auto:eco,dpr_1/rbecxs664o38xrz8zkhq",
                    "ts": datetime.now().timestamp()
                }
            ]
    }
        # Attach Media files here
       # message['attachments'].append({
       #     "text": "Full Debug Information",
       #     "fallback": "If you could read this message, you'd be choosing something fun to do right now.",
       #     "color": "#3AA3E3",
       #     "attachment_type": "default",
       #     "callback_id": "dinfo_selection",
       #     "actions": [
       #         {
       #             "name": "dinfo",
       #             "text": "Debug Info",
       #             "type": "select",
       #             "options": [
       #                 {
       #                     "text": dinfo,
       #                     "value": "default"
       #                 },
       #             ]
       #         }
       #     ]
       # })

    return message

def non_dinfo_ticket(support_channel_id, data, priority, steps_to_reproduce, goalkeeper, media=False):
    return {
        "channel": support_channel_id,
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": "#36a64f",
                "author_name": f"Ticket {data['author_name']['ticket_id']} - {priority}",
                "title": "Click here to follow the ticket.",
                "title_link": data["ticket_link"],
                "fields": [
                    {
                        "title": ":label: Title:",
                        "value": data["fields"]["title"],
                        "short": False
                    },
                    {
                        "title": ":thread: Description:",
                        "value": data["fields"]["description"],
                        "short": False
                    },
                    {
                        "title": ":arrows_counterclockwise: How to reproduce:",
                        "value": steps_to_reproduce,
                        "short": False
                    },
                    {
                        "title": ":red_circle: Debug information is not available for this ticket :red_circle:",
                        "short": False
                    },
                    {
                        "title": ":goal_net: Goalkeeper:",
                        "value": f"<@{goalkeeper}>",
                        "short": True
                    },
                ],
                "footer": "Technical Support Team",
                "footer_icon": "https://images.crunchbase.com/image/upload/c_pad,f_auto,q_auto:eco,dpr_1/rbecxs664o38xrz8zkhq",
                "ts": datetime.now().timestamp()
            }
        ]
    }