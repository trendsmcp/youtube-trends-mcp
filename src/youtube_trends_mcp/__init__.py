"""
youtube-trends-mcp -- YouTube search interest as an MCP tool. Plug into Claude, Cursor, or any MCP-compatible AI host. Weekly series, growth percentages, and live YouTube trending searches.

Get your free API key at https://trendsmcp.ai
Full docs at https://trendsmcp.ai/docs
"""

from trendsmcp import TrendsMcpClient, AsyncTrendsMcpClient, TrendsMcpError
from trendsmcp.types import (
    TrendsSource,
    TrendsDataPoint,
    GetTrendsParams,
    GetTrendsResponse,
    GrowthPreset,
    CustomGrowthPeriod,
    GetGrowthParams,
    GrowthResult,
    GrowthMetadata,
    GetGrowthResponse,
    TopTrendsFeed,
    GetTopTrendsParams,
    GetTopTrendsResponse,
)

# Default source for this package. Pass to 'source' in any request.
SOURCE: TrendsSource = "youtube"

__version__ = "1.0.0"
__all__ = [
    "TrendsMcpClient",
    "AsyncTrendsMcpClient",
    "TrendsMcpError",
    "SOURCE",
    "TrendsSource",
    "TrendsDataPoint",
    "GetTrendsParams",
    "GetTrendsResponse",
    "GrowthPreset",
    "CustomGrowthPeriod",
    "GetGrowthParams",
    "GrowthResult",
    "GrowthMetadata",
    "GetGrowthResponse",
    "TopTrendsFeed",
    "GetTopTrendsParams",
    "GetTopTrendsResponse",
]
