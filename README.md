# youtube-trends-mcp

[![YouTube Trends](https://img.shields.io/badge/YouTube%20Trends-FF0000?style=flat-square)](https://trendsmcp.ai/youtube-trends)
[![MCP](https://img.shields.io/badge/MCP-compatible-blue?style=flat-square)](https://modelcontextprotocol.io)
[![Works with Claude](https://img.shields.io/badge/Claude-supported-orange?style=flat-square)](https://trendsmcp.ai/mcp-server-for-claude)
[![Works with Cursor](https://img.shields.io/badge/Cursor-supported-purple?style=flat-square)](https://trendsmcp.ai/mcp-server-for-cursor)

> **YouTube trend data for AI assistants**
> Find out what people are searching for on YouTube. Rising topics, growing video keywords, and historical search demand - all queryable by your AI in plain language.

**Full docs and live demo:** [https://trendsmcp.ai/youtube-trends](https://trendsmcp.ai/youtube-trends)

Part of **[Trends MCP](https://trendsmcp.ai)** - the MCP server for live trend data across 12+ sources.
See the main repo: [https://github.com/trendsmcp/trends-mcp](https://github.com/trendsmcp/trends-mcp)

---

## Get started in 2 steps

**Step 1:** Get your free API key at **[trendsmcp.ai](https://trendsmcp.ai)**
100 requests/day, no credit card required.

**Step 2:** Add to your AI client (replace `YOUR_API_KEY`):

[**+ Add to Cursor (one click)**](cursor://anysphere.cursor-deeplink/mcp/install?name=trends-mcp&config=eyJ1cmwiOiAiaHR0cHM6Ly9hcGkudHJlbmRzbWNwLmFpL21jcCIsICJ0cmFuc3BvcnQiOiAiaHR0cCJ9)

**Cursor / Windsurf / Cline** &nbsp; (`~/.cursor/mcp.json` or equivalent)
```json
{
  "mcpServers": {
    "trends-mcp": {
      "url": "https://api.trendsmcp.ai/mcp",
      "transport": "http",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**VS Code / GitHub Copilot** &nbsp; (`.vscode/mcp.json`)
```json
{
  "servers": {
    "trends-mcp": {
      "type": "http",
      "url": "https://api.trendsmcp.ai/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

**Claude Desktop** &nbsp; (`claude_desktop_config.json`)
User → Settings → Developer → Edit Config — add inside mcpServers
```json
{
  "mcpServers": {
    "trends-mcp": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://api.trendsmcp.ai/mcp",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

**Claude.ai** (browser) &nbsp; Settings -> Connectors -> Add custom connector:
```
https://api.trendsmcp.ai/mcp
```

---

## Example query

After connecting, ask your AI:
```
get_trends(keyword='morning routine', source='youtube', data_mode='weekly')
```

---

## Available tools

| Tool | What it does |
|------|-------------|
| `get_trends` | Time-series for a keyword on this source |
| `get_growth` | Growth % over 1W, 1M, 3M, 6M, 1Y periods |
| `get_top_trends` | What is trending right now on this source |
| `get_ranked_trends` | Top topics ranked by volume |

---

## FAQ

### What YouTube data does Trends MCP provide?

YouTube video search volume trends - normalized interest over time, growth metrics, and historical series. This reflects demand for video content on specific topics, not view counts on individual videos.

### How is YouTube search data different from Google Search data?

YouTube reflects video-specific intent. A keyword like 'how to do a handstand' may have high YouTube demand but lower Google Search volume. Comparing both reveals content format preferences.

### Can I use this to find trending YouTube content ideas?

Yes. Query a set of topic keywords, rank by growth rate over the last 30 days, and your AI will surface which video topics are gaining search momentum right now.

### Does it cover YouTube Shorts search demand?

The signal reflects overall YouTube search volume including Shorts discovery. YouTube does not separate Shorts search data, so results reflect total platform search interest.

---

## All data sources

Trends MCP covers 12+ sources in one connection:
Google Search, YouTube, TikTok, Reddit, Amazon, Wikipedia,
News Sentiment, Web Traffic, App Downloads, Steam, npm, and more.

Browse all: [https://trendsmcp.ai/data-sources](https://trendsmcp.ai/data-sources)


---

## Also works as a Python client

Same API key works directly in Python - no MCP host needed.

```bash
pip install youtube-trends-mcp
```

```python
import os
from youtube_trends_mcp import TrendsMcpClient, SOURCE

client = TrendsMcpClient(api_key=os.environ["TRENDSMCP_API_KEY"])

series  = client.get_trends(source=SOURCE, keyword="your keyword")
growth  = client.get_growth(source=SOURCE, keyword="your keyword", percent_growth=["1M", "3M", "12M"])
top     = client.get_top_trends(type="Youtube", limit=10)
```

Full Python docs: [trendsmcp.ai/docs](https://trendsmcp.ai/docs)
---

## License

MIT &copy; [Trends MCP](https://trendsmcp.ai)
