"""One finding format for every review bot."""
from dataclasses import dataclass, field


@dataclass
class Finding:
    bot: str
    path: str
    start_line: int
    end_line: int
    body: str
    severity: str = "unknown"
    sources: list[str] = field(default_factory=list)


def from_review_comment(bot: str, c: dict) -> Finding:
    """Build a Finding from a GitHub pull request review comment (REST API shape)."""
    end = c.get("line") or c.get("original_line")
    start = c.get("start_line") or end
    return Finding(bot=bot, path=c["path"], start_line=start, end_line=end,
                   body=c["body"], sources=[c["html_url"]])


def overlaps(a: Finding, b: Finding, slack: int = 3) -> bool:
    """True when two findings point at the same file and nearby lines."""
    return a.path == b.path and a.start_line - slack <= b.end_line and b.start_line - slack <= a.end_line
