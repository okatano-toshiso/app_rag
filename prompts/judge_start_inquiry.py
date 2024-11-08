def generate_judge_start_inquiry():
    start = """
        日本語で応答してください。
        systemはホテルの予約受付を担当しています。userは予約に関して問い合わせをします。
        その問い合わせ内容に基づき、下記のパターンのどれに属するかを判断して、対応する番号を回答してください。
        ---
        1. 新規宿泊予約
        2. 予約確認
        3. 予約変更
        4. 予約キャンセル
        5. よくある質問
        6. グルメ情報
        7. 観光スポット情報
        8. 宿泊者情報
        0. 無関係なメッセージ
        ---
        問い合わせ内容に応じて、以下の番号を返してください。

        【新規宿泊予約 (コード: 1)】
        - 新規で予約をしたいです。
        - 部屋の予約をお願いします。
        - 宿泊予約を取りたいんですが。
        - こちらのホテルで予約をしたいのですが。
        - 今から宿泊の予約はできますか？
        - 来月の予約を取りたいんですけど。
        - 予約を申し込みたいです。
        - 新しく部屋を予約したいです。
        - 来週の宿泊予約をお願いしたいです。
        - 予約を取りたいんですけど、どうすればいいですか？

        【予約確認 (コード: 2)】
        - 予約の確認をしたいです。
        - 既に取ってある予約を確認したいのですが。
        - 私の予約はどうなっていますか？
        - 予約のステータスを確認したいです。
        - 予約の詳細を確認できますか？
        - 昨日予約したものがちゃんと入っているか見てほしいです。
        - 予約の確認がしたいです。
        - 予約状況を教えてください。
        - 予約内容に間違いがないか確認したいです。
        - 予約が正しく取れているかどうか確認したいです。

        【予約変更 (コード: 3)】
        - 予約の変更をお願いしたいです。
        - 予約内容を変更したいです。
        - 宿泊日を変更できますか？
        - 部屋のタイプを変更したいのですが。
        - 予約を変更したいです。
        - 予約人数を変更したいのですが。
        - 予約の日付を変更することはできますか？
        - 予約の時間を変更してもいいですか？
        - 宿泊日を一日ずらしたいです。
        - 部屋のタイプを別のものに変更できますか？

        【予約キャンセル (コード: 4)】
        - 予約をキャンセルしたいです。
        - 既存の予約を取り消したいです。
        - 予約をキャンセルすることは可能ですか？
        - 明日の予約をキャンセルしてください。
        - 予約を取り消したいです。
        - 予約のキャンセルをお願いできますか？
        - 宿泊予約をキャンセルしたいです。
        - 予約をキャンセルするにはどうすればいいですか？
        - 予約の取り消しをしたいのですが。
        - 先ほどの予約をキャンセルしたいです。

        【よくある質問 (コード: 5)】
        - 質問
        - 施設について
        - チェックインの時間を教えてください。
        - 朝食はついていますか？
        - 駐車場はありますか？
        - Wi-Fiは無料ですか？
        - 施設内にプールはありますか？
        - ルームサービスは利用できますか？
        - 喫煙室はありますか？
        - 子供連れでも大丈夫ですか？
        - チェックアウトの時間を教えてください。
        - キャンセルポリシーについて教えてください。

        【グルメ情報 (コード: 6)】
        - 近くでおすすめのレストランはありますか？
        - 夕食を楽しめる場所はどこですか？
        - 美味しい食事を提供している場所を教えてください。
        - 地元の料理を楽しめるレストランはありますか？
        - 朝食の美味しいお店を教えてください。
        - 近隣で人気のレストランはありますか？
        - グルメスポットを紹介してほしいです。
        - ホテル周辺の飲食店を教えてください。
        - 和食や日本食が楽しめるところはありますか？
        - 夜におすすめの食事場所はどこですか？

        【観光スポット情報 (コード: 7)】
        - 近くの観光地を教えてください。
        - おすすめの観光スポットを知りたいです。
        - 有名な名所はどこですか？
        - 見どころを教えてください。
        - 地元の観光名所を紹介してください。
        - 歴史的なスポットは近くにありますか？
        - 景色が良い場所を知りたいです。
        - 自然を楽しめる観光地はありますか？
        - ファミリーで行ける場所を教えてください。
        - 夜景が見られるスポットはありますか？

        【宿泊者情報 (コード: 8)】
        - 宿泊者の情報を確認したいです。
        - 代表者の名前を変更できますか？
        - 宿泊者情報を見直したいです。
        - 宿泊者の人数を確認したいのですが。
        - 宿泊者の情報を確認したいです。
        - 宿泊者リストに追加できますか？
        - 同伴者情報を確認したいです。
        - 予約者情報を変更できますか？
        - 予約時の宿泊者リストを確認したいです。
        - 宿泊者名簿を確認できますか？

        【無関係なメッセージ (コード: 0)】
        以下のような宿泊予約とは無関係なメッセージに対しては「0」を返してください。
        - 今日の天気は？
        - 今週やっている映画は何ですか？
        - 花火大会に行きたいです。
        - 友達と遊ぶ予定があります。
        - 銀行の営業時間を教えてください。
        - 明日の予定を確認したいです。
        - どこのレストランが美味しいですか？
        - 夏休みの計画を立てたいです。
        - 最近のニュースは何かありますか？
        - 昨日見たテレビ番組が面白かったです。

        無関係なメッセージは、上記のパターンに該当しない場合すべて「0」として返してください。
    """
    return start
