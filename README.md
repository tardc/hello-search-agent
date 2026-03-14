# Search Agent

流程：用户问题 → 搜索网页 → 抓取内容 → AI 流式总结

## 快速开始

```bash
pip install -r requirements.txt
cp .env.example .env   # 填入你的配置
python main.py "你的问题"
```

## 配置（.env）

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `OPENAI_API_KEY` | API Key（必填） | - |
| `OPENAI_BASE_URL` | API Base URL | `https://api.openai.com/v1` |
| `OPENAI_MODEL` | 模型名称 | `gpt-4o-mini` |
| `NUM_RESULTS` | 搜索结果数量 | `5` |
| `MAX_PAGE_CHARS` | 每页最大字符数 | `4000` |

## 兼容示例

```env
# DeepSeek
OPENAI_BASE_URL=https://api.deepseek.com/v1
OPENAI_MODEL=deepseek-chat

# Ollama（本地）
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_API_KEY=ollama
OPENAI_MODEL=llama3
```
