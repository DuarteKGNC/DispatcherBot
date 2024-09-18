from datetime import datetime
def standard_ticket(support_channel_id, data, priority, steps_to_reproduce, links, user, info, version, goalkeeper, debug_info):
    message = {
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
    message['attachments'].append({
        "title":"Upload her",
        "text":"<https://images.crunchbase.com/image/upload/c_pad,f_auto,q_auto:eco,dpr_1/rbecxs664o38xrz8zkhq|Download FIle>"
    })
    return message

def non_dinfo_ticket(support_channel_id, data, priority, steps_to_reproduce, goalkeeper):
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