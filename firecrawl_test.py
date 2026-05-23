"""
Firecrawl 测试脚本 - 抓取网页并提取 Markdown 内容
"""
import os
from firecrawl import Firecrawl

API_KEY = os.environ.get("FIRECRAWL_API_KEY", "fc-fb979a96cf004bc0a10a02d18c483a2b")

app = Firecrawl(api_key=API_KEY)

# 抓取单个网页
result = app.scrape_url("https://firecrawl.dev")
print("标题:", result.metadata.title)
print("描述:", result.metadata.description)
print("语言:", result.metadata.language)
print("--- Markdown 内容预览 ---")
print(result.markdown[:500])
