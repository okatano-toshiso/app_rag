# app_rag - Retrieval-Augmented Generation (RAG) 対応チャットボット

`app_rag` は、RAG（Retrieval-Augmented Generation）技術を活用したチャットボットアプリケーションです。  
ユーザーの質問に対して、外部知識ベースから関連情報を検索し、生成AI（ChatGPTなど）と組み合わせて高精度な応答を生成します。

---

## 📘 概要

このプロジェクトは、ホテル予約や観光案内などの自然言語対話を通じて、ユーザーの意図を理解し、最適な回答を提供することを目的としています。  
`utils/rag.py` により、RAG（検索＋生成）アプローチを実装しています。

---

## 🧩 主な機能

- 🔍 **RAG（Retrieval-Augmented Generation）** による高精度応答生成  
- 🏨 **ホテル予約・観光案内** などのドメイン特化型対話  
- 🧠 **ChatGPT API** を利用した自然言語生成  
- 🎙️ **音声入力・文字起こし** 機能（`line_audio_save.py`, `transcriber.py`）  
- 🧾 **ユーザー入力検証**（`validation.py`）  
- 🗂️ **プロンプト管理**（`prompts/` ディレクトリ）  

---

## 🏗️ ディレクトリ構成

```
app_rag/
├── chatgpt_api.py              # ChatGPT APIとの通信処理
├── generate.py                 # 応答生成ロジック
├── main.py                     # アプリケーションエントリーポイント
├── menu_items.py               # メニュー定義
├── messages.py                 # メッセージ管理
├── reservation_handler*.py     # 各種予約処理（ホテル・観光・飲食など）
├── prompts/                    # 対話プロンプト定義
├── utils/                      # ユーティリティ群（RAG, 音声処理, 検証など）
│   ├── rag.py                  # RAG実装（検索＋生成）
│   ├── transcriber.py          # 音声→テキスト変換
│   ├── vocabulary_filter_utils.py # 語彙フィルタリング
│   └── ...
└── README.md
```

---

## ⚙️ セットアップ手順

### 1. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定
`.env` ファイルを作成し、APIキーなどを設定します。
```bash
OPENAI_API_KEY=your_api_key_here
```

### 3. アプリケーションの起動
```bash
python main.py
```

---

## 🧠 RAG（Retrieval-Augmented Generation）とは？

RAG は、**検索（Retrieval）** と **生成（Generation）** を組み合わせたAIアプローチです。  
このプロジェクトでは、`utils/rag.py` にて以下の流れを実装しています：

1. ユーザーの質問を受け取る  
2. 内部知識ベース（FAQや観光情報など）から関連情報を検索  
3. 検索結果をもとに ChatGPT API で自然言語応答を生成  
4. 最終的な回答をユーザーに返す  

この仕組みにより、単なる生成AIよりも正確で文脈に沿った回答が可能になります。

---

## 🧪 使用例

### ホテル予約の問い合わせ
```
ユーザー: 明日2名で宿泊予約をしたいです。
AI: ご希望の宿泊日と部屋タイプを教えてください。
```

### 観光案内
```
ユーザー: 東京でおすすめの観光地は？
AI: 浅草寺、東京スカイツリー、上野公園などがおすすめです。
```

---

## 🧰 開発者向け情報

### プロンプトの追加
`prompts/` ディレクトリに新しい `.py` ファイルを追加することで、  
新しい対話シナリオを簡単に拡張できます。

### RAGのカスタマイズ
`utils/rag.py` 内で検索アルゴリズムやスコアリングロジックを調整可能です。

---

## 📚 参考資料

- [Retrieval-Augmented Generation (RAG) Explained - Hugging Face](https://huggingface.co/blog/rag)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [LangChain Documentation](https://python.langchain.com/)
- [GitHub README 書き方ガイド](https://docs.github.com/ja/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

---

## 🧑‍💻 ライセンス

このプロジェクトはオープンソースであり、自由に利用・改変できます。  
詳細は `LICENSE` ファイルをご確認ください。

---

## 💬 貢献方法

1. Issue を作成して改善提案を行う  
2. Fork してブランチを作成  
3. 修正後、Pull Request を送信  

---

## 🏁 作者

開発者: [Your Name]  
連絡先: [your.email@example.com]
cd