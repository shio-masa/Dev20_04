slackでもあった内容でLINE MessagingAPIを利用する課題に取り組みました。
LINE公式アカウント上で動作する 自動応答bot作成しました（が上手く動作せず調整中です）

手順：
Line Developersでプロバイダーを作成
Line Developers-MessagingAPIからチャネルアクセストークンを発行
バックエンドシステムはAWSを利用して構築し、サービスはAmazon API GatewayとAmazon lambdaを利用した
LambdaでPython用ソースファイルとLineBotライブラリをアップロード
API gatewayから作成したlambda 関数を指定し、URLを発行（この時点でerror404が返されており、lambda関数とgatewayの接続がうまくいってない？と捜索中）
URLをLINE公式アカウント webhookに埋め込み、既存の自動応答をoff 

LINE公式アカウント:URL https://lin.ee/oHUp24A