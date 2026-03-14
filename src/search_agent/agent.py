from .search import web_search, fetch_page
from .summarize import summarize


def run(question: str) -> None:
    """Execute the full search-agent pipeline."""
    print(f"\n🔍 搜索中: {question}\n")

    results = web_search(question)
    if not results:
        print("未找到相关结果。")
        return

    print(f"找到 {len(results)} 个结果，正在抓取页面...\n")
    pages = []
    for r in results:
        print(f"  ↳ {r['title'][:60]}...")
        pages.append({**r, "content": fetch_page(r["url"])})

    print("\n🤖 AI 总结中...\n" + "=" * 60)
    summarize(question, pages)
    print("=" * 60)
