#!/usr/bin/env python3
# coding=utf-8

import requests
from settings_notion import NOTION_URI, NOTION_HEADERS


def page_update(page_id, lark_event_id):
    """
    更新 notion 的 飞书日程id：https://developers.notion.com/reference/patch-page
    """
    url = f"{NOTION_URI}/v1/pages/{page_id}"
    data = {
        "properties": {
            "lark_event_id": {
                "type": "rich_text",
                "rich_text": [{"text": {
                    "content": lark_event_id,
                },
                    'annotations': {'bold': False,
                                    'italic': False, 'strikethrough': False,
                                    'underline': False,
                                    'code': False,
                                    'color': 'default'},
                    'href': None,
                    "plain_text": lark_event_id, }]

            }}
    }
    resp = requests.patch(url, headers=NOTION_HEADERS, json=data)
    print("更新 notion lark_event_id：")
    print(resp.text)
    return resp.json()


def database_query(database_id, next_cursor=None, all=False):
    """
    获取 notion database：https://developers.notion.com/reference/post-database-query
    """
    url = f"{NOTION_URI}/v1/databases/{database_id}/query"
    if all:
        data = {}
    else:
        data = {
            "filter": {
                "timestamp": "last_edited_time",
                "last_edited_time": {
                    "past_week": {}
                }
            },
            "page_size": 100
        }
    if next_cursor:
        data["start_cursor"] = next_cursor

    resp = requests.post(url, headers=NOTION_HEADERS, json=data)
    print(resp.text)
    return resp.json()
