#!/usr/bin/env python3
# coding=utf-8

# notion api 后台：https://www.notion.so/my-integrations
NOTION_ACCESS_TOKEN = ""

NOTION_URI = "https://api.notion.com"
NOTION_VERSION = "2022-02-22"
NOTION_HEADERS = {
    "Authorization": "Bearer " + NOTION_ACCESS_TOKEN,
    "Notion-Version": NOTION_VERSION
}

