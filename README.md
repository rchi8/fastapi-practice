# fastapi-practice

##　[feature/docker] Docker環境の構築
https://chat.openai.com/share/e46744c7-6b69-4ebe-88f6-184b947c7a35

## [feature/hello-world] Hello Worldまで
https://chat.openai.com/share/e46744c7-6b69-4ebe-88f6-184b947c7a35

## [feature/routers] ルータの作成
https://chat.openai.com/share/e46744c7-6b69-4ebe-88f6-184b947c7a35

## [feature/schemas] レスポンス作成








## REST API の解説
REST API（Representational State Transfer Application Programming Interface）とは、ウェブサービスなどのAPIを設計するためのアーキテクチャスタイルの一つです。APIとは、異なるソフトウェア同士がやりとりをするための「橋」のようなものですが、RESTはそのやりとりがどのように行われるかの「ルール」を提供します。🌉

### REST APIの特徴

1. **ステートレス性**: 各リクエストは独立していて、それぞれのリクエストで必要な情報は全て含まれています。
2. **無障壁**: REST APIはHTTPという普遍的なプロトコルを使うので、環境や言語に依存しない。
3. **クライアント-サーバー構造**: サーバーはデータと機能を提供し、クライアントはそれを利用する、という役割分担が明確です。

### 基本のHTTPメソッド

- **GET**: データを取得する。
- **POST**: 新しいデータを作成する。
- **PUT**: 既存のデータを更新する。
- **DELETE**: データを削除する。

例えば、書籍の情報を管理するAPIがあったとしましょう。

- 書籍の一覧を取得: `GET /books`
- 新しい書籍を追加: `POST /books`
- 特定の書籍の情報を更新: `PUT /books/1`
- 特定の書籍を削除: `DELETE /books/1`

REST APIはこのように、ウェブ上のリソース（この場合は「書籍」）に対して、綺麗に操作を行うことができます。AIやデータサイエンスのコンテキストでは、データの入出力やモデルの操作にREST APIが使われることも多いですよ。📚✨