"""
Firecrawl 测试脚本
使用前请到 https://firecrawl.dev 注册获取免费 API Key
然后设置环境变量: export FIRECRAWL_API_KEY="fc-YOUR_API_KEY"
"""
import os
from firecrawl import Firecrawl

api_key = os.environ.get("FIRECRAWL_API_KEY")
if not api_key:
    print("请先设置 API Key:")
    print("  1. 访问 https://firecrawl.dev 注册")
    print("  2. 运行: export FIRECRAWL_API_KEY='fc-YOUR_API_KEY'")
    exit(1)

app = Firecrawl(api_key=api_key)

# 抓取单个网页
result = app.scrape_url("https://firecrawl.dev")
print("网页内容 (Markdown):")
print(result.get("markdown", "")[:500])
