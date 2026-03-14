from openai import OpenAI
from . import config

_client = OpenAI(api_key=config.API_KEY, base_url=config.BASE_URL)

_SYSTEM_PROMPT = (
    "你是一个搜索助手。根据提供的网页内容，综合多个来源回答用户问题，"
    "给出准确、简洁的答案，并在末尾列出参考来源链接。"
)


def summarize(question: str, pages: list[dict]) -> None:
    """Stream an LLM-generated answer grounded in the fetched pages."""
    context = "\n\n---\n\n".join(
        f"[Source {i}] {p['title']}\nURL: {p['url']}\n\n{p['content']}"
        for i, p in enumerate(pages, 1)
    )
    user_message = f"用户问题：{question}\n\n网页内容：\n{context}"

    stream = _client.chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.3,
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()
