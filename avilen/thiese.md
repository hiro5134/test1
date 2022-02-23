# [My kicks](#mykicks)

## <a href="#index">Index</a><a id="index"></a>
* [Chapter 1](#cp1)

## <a id = "cp1">EfficientNet</a>
1. ## <a id="lib">GPipe</a>
    EfficientNetのベース
    モデルのスケールアップをすることの有用性論文内で主張
    特に解像度のスケールアップ(480 * 480画像使用)でSOTA性能

1. ## <a id="lib">EfficientNet</a>
    - 新たなスケーリング手法を提案
        本手法に基づくベースラインモデル EfficientNetを提案
        (従来のモデルスケーリング手法の有効性を評価)
    - モデルのスケールアップは有効(like GPipe)
    - 既存手法に比べ8.4倍小さく，6.1倍高速でSOTA性能を発揮

    1. モデルのスケーリング
        既存のスケーリング手法を組み合わせた
        下記3スケーリング手法を組み合わせた，Compound Scalingを提案
        - 層の幅
        - 層の深さ
        - 解像度

    1. Compound Scaling Method
        以下の手順でモデルをスケールアップ
        1. 初期値$\phi = 1$
        1. メモリ，FLOPS，下式の制約下で$\alpha, \beta, \gamma$をグリッドサーチ
        1. 制約を満たす範囲で$\phi$をスケールアップ
        $$\begin{align}
          \textrm{depth : }&d = \alpha^{\phi}\\
          \textrm{width : }&w = \beta^{\phi}\\
          \textrm{resolution : }&r = \gamma^{\phi}\\
          \textrm{s.t.}\,&\alpha\cdot\beta^2\cdot\gamma^2\approx2\\
          &\alpha\geq1,\beta\geq1,\gamma\geq1
        \end{align}$$
        幅のスケールの影響を他のスケールよりも大きく見積もる
        →グリッドサーチの結果最も良かったモデルを「EfficientNet-B0」とし，$\phi$の増加に伴いB1〜7まで存在
        →MBConvという機構を用いている

    1. MBConv
        Depthwise ConvとSqueeze-and-Excitation(SE)とスキップ接続の併用
        - Depthwise Conv
            チャネル毎の畳み込み
        - Squeeze-and-Excitation(SE)
            特徴マップ$U$を変換$F_{sq}$で低次元に圧縮
            非線形変換$F_{ex}$で特徴生成($F_{scale}$)
            元の特徴$U$に重みづけ($F_{scale}$)して出力$\bar{X}$を得る


## <a id = "cp2">WideResNet</a>
1. ## <a id="lib">WideResNet</a>
    層を深くする代わりに，層幅を広げたResNet
    →発表当時は，層の深化が主流であった
    層幅を広げた方が，効率・精度の面でも優れていることを主張

1. ## <a id="lib">アーキテクチャ</a>
    - Group
        - Block * k
            k = 1が一般的なResNet
            Kを増やすことで層幅を増加

    block type = B(3,3)
    - conv1 (out = 32 * 32)
    $$
      [3\times 3, 16]
    $$
    - conv2 (out = 32 * 32)
    $$
      \begin{align}\left[\begin{split}
        3\times 3, 16\times k\\
        3\times 3, 16\times k
      \end{split}\right] * N\end{align}
    $$
    - conv3 (out = 16 * 16)
    $$
      \begin{align}\left[\begin{split}
        3\times 3, 16\times k\\
        3\times 3, 16\times k
      \end{split}\right] * N\end{align}
    $$
    - conv4 (out = 8 * 8)
    $$
      \begin{align}\left[\begin{split}
        3\times 3, 16\times k\\
        3\times 3, 16\times k
      \end{split}\right] * N\end{align}
    $$
    - avg-pool (out = 1 * 1)
    $$
      [8\times 8]
    $$

1. ## <a id="lib">結果</a>
    k = 10の28層WideresNetが1000層近い通常ResNetに勝る結果に


## <a id = "cp3">Mask R-CNN</a>
1. ## <a id="lib">物体検出</a>
    画像中オブジェクトの位置とクラスを推定するタスク
    bounding boxの座標回帰問題とクラス分類問題を解く

1. ## <a id="lib">YOLO</a>
    検出と識別を同時に行う one-stage法の提案
    →従来は検出と識別を順次行う two-stage法

    高速な推論が可能
    v1〜4が提案

    - bounding boxの確信度を定義
        IOU : 真のboxと予測のboxのIOU
        $\textrm{Pr(Object)}\times IOU$
    - 確信度とクラス予測確率の積の最大化で検出と分類を同時に実現
        $\textrm{Pr(Class}_i\textrm{|Object)}\times\textrm{Pr(Object)}\times IOU = \textrm{Pr(Class}_i)\times IOU$
    - 損失
        以下の真値との誤差を最小にするように学習
        確信度とクラス確率は真値が1のため，実質指標の最大化
        1. bounding boxの座標
        1. bounding boxの確信度
        1. クラス予測確率
        $L_{YOLO} = \textrm{3つの誤差の和}$

1. ## <a id="lib">SSD</a>
    予め複数のbounding boxを用意(default box)
    box毎に推論
    各層の特徴マップから特徴抽出を行い，様々なスケールの物体に対応
    →YOLOは最後のマップのみから推論(入力数:1)
    →SSDは各層のマップを入力とし，推論(入力数:マップ数)

1. ## <a id="lib">Faster R-CNN</a>
    候補領域の提案，物体の分類をend2endで行う物体検出手法

    - CNNで抽出した特徴マップ上の各点(Anchor)
    - Anchor毎に9個の形状の異なるbox(Anchor box)を算出
    - Anchor box毎に物体の誤認識とboxのズレが小さくなるように学習

1. ## <a id="lib">Mask R-CNN</a>
    オブジェクトの位置とクラスに加え，オブジェクトのマスクを出力する
    →Faster R-CNNの拡張(出力層分岐し，マスクの出力されるイメージ)

    物体検出だけでなく，領域分割(ピクセル単位の識別)や姿勢推定も可能に

    - RoIAlign
        双線形補間によって特徴マップ上の座標を決定
        →細かい単位での分割が可能に

        関心領域(RoI)をの特徴を抽出する一般的な手法RoIPool
        →RoIの座標を整数値に丸めいていた
        →RoIと特徴マップにずれが生じる(座標にずれ，ビンによる分割から抜け出せない)

    1. 結果
        - Instance Segmentation
            物体を検出し，物体ごとに領域を分割するタスク
            →従来よりも自然で高精度なsegmentationが可能に
        - 姿勢推定
            人体のキーポイント(関節など)の位置を推定するタスク
            →姿勢推定が可能に


## <a id = "cp3">FCOS</a>
    物体検出
1. ## <a id="lib">FPN</a>
    領域検出手法(ピクセル単位での分類)
    畳み込み各層で推論を行うことで，マルチスケールな推論が可能に

    - 畳み込み以前
        様々な大きさの特徴マップから推論を個別に行っていた
    - 畳み込み
        畳み込んだ結果の出力層のみから推論
    - FPN
        上記2つを合わせたもの

1. ## <a id="lib">RetinaNet</a>
    FPNをベースに，物体分類・bounding box回帰を行う

    - 論文での指摘
        Anchor boxを用いるとポジテイブ/ネガティブ不均衡が発生
        →検出したいオブジェクト(ポジティブ)に対して，背景(ネガティブ)が圧倒的に多いため
        →Focal Lossを導入し解消

1. ## <a id="lib">FCOS</a>
    Fully Convolutional One-Stage Object Detection
    RetinaNetにオブジェクトの中心位置推定を加えたもの(anchor boxを用いないanchor free)
    物体中心自体を予測し，真のbounding box中全ての点を利用してbounding boxを予測

    - 既存手法はAnchor boxを用いることがベース
        SSD, YOLO(v2以降)など
        (YOLOv1はanchor boxを用いず，物体中心近くの点でboundng boxを予測)
        以下の問題点があった
        →事前の適切な設定が必要
        →ポジティブ/ネガティブ不均衡が発生

    1. アーキテクチャ
        RetinaNet同様，物体分類，bbox回帰を行う
        加えて，conter-ness予測も行う

        (RetinaNetではC5をp6,7から作るが，FCOSではF5から作り，性能向上)

    1. center-ness予測
        中心からの重みづけ(centerness)で，質の悪いbboxを排除

        分類スコアにcenternessを乗じたものをテスト時に検出されたbboxのスコアとし，質の悪いbboxを排除
        $$
          \textrm{centerness}^* = \sqrt{\frac{\min(l^*,r*)}{\max(l^*,r^*)}\times\frac{\min(t^*,b*)}{\max(t^*,b^*)}}
        $$
        中心位置からの左右上下の離れ具合を($l^*,r^*,t^*,b^*)$)
        真の中心位置と同じであれば，centernessは1．
        離れると値が小さくなる

    1. 結果
        COCOデータセットで物体検出の性能比較
        →COCO：自然画像からの物体検出のベンチマーク
        →nms：non-maximum suppression(bboxの重なりを取り除く手法)

        Average precision(AP)とaverage recall(AR)でRetinaNetを上回った


## <a id = "cp3">BERT</a>
1. ## <a id="lib">BERT</a>
    Pre-training of Deep Bidirectional Transfomers for Language Understanding

    BERT : Bidirectional Encoder Representations from Transformers

    Googleが開発した汎用言語モデル
    NLPにおける，ImageNetのPre-trainedモデル(VGG, ResNet)的存在
    →(当時NAACLに採択されていないにもかかわらず)ArXiv登場時に，A new era of NLPと騒がれていた

    1. 特徴
        - マルチタスク学習により，汎用的な分散表現を計算する事前学習モデル
            下記タスクを解き，損失関数が最小になるように学習
            - Masked LM
                マスクされた入力は何か
            - Next Sentence Prediction
                2文入力，それらは連続した文章か
        - 大きなTransformer
            - Model : (Encoder, Head)
            - Original Transformer : (6, 8)
            - BERT BASE : (12, 12)
            - BERT LARGE : (24, 16)
        - 単文・複文どちらも入力可能
            →複文タスク(QA, 要約など)にも応用させるため
        - Masked LNの提案
            双方向でも，予測時に未来の情報を利用する問題(カンニング)を上手く回避
    1. 利用方法
        基本的には，BERTモデルに小さなレイヤを追加するのみで他タスクに利用可能
        - Classification Tasks
            事前学習のタスク同様，[CLS]tokenに対して分類
        - Named Entity Recognition
            各tokenがIOB tagを出力するように学習
        - Question and Answer
            Paragraphに対して，AnswerとなるStart/End Spanを出力するように学習


## <a id = "cp3">GPT-3</a>
1. ## <a id="lib">前提とバージョン</a>
    - few / one / zero-shot learning
        一般に大量のデータが必要なDNNにて
        - few-shot
            少量のデータで行う学習
            - one / zero-shot
                1個 / 0個のデータで行う学習
    - 学習の背景
        各タスクへの適用は，事前学習後にfine-tuningすることが一般的
        一方でこの時，大量のデータが必要になる
    - GPT-3
        事前学習：より大規模なモデル＋より多くのデータで事前学習
        各タスクへの適用：few-shotでのfine-tuningで推論の性能向上

    1. GPT
        Transformerのデコーダからなるアーキテクチャ
        自己回帰型の事前学習→各タスクのfine-tuning

        自己回帰型言語モデル：ある位置の文字の確率を，それ以前の文字たちの確率で表現する言語モデル
    1. GPT-2
        GPTを大規模化→大きなデータセットで学習
        事前学習で，マルチタスク学習を実施
    1. GPT-3
        さらなるぢ大規模化で，few-shotでさらに性能向上
        - In-context Learning
            GPT-2同様に事前学習でマルチタスク学習
            →特に，タスクごとの学習をIn-contxet Learningと呼ぶ

1. ## <a id="lib">GPT-3におけるfew-shotの意味とタスク</a>
    推論時に提示される例の数で，zero/one/few-shotを区別
    タスク自体を自然言語で表現
    プロンプト後のテキストを生成させる

1. ## <a id="lib">生成結果</a>
    - 作って欲しいサイトの要望を言葉で書いて，要望通りのサイトを作る
        e.g.)Googleのサイトを作った
    - 自然な文章を生成
    - 思考実験を行った

1. ## <a id="lib">課題</a>
    - 同じ意味の内容を繰り返す
    - 文章全体としての一貫性がない
    - 矛盾した文章を生成
    - 非合理的な文章を生成
    - 物理法則を直感的/常識的に理解できない

1. ## <a id="lib">発見</a>
    - Scaling Law
        モデルの性能は，モデルサイズに対して対数スケールで向上していくことを発見
        $\textrm{Validation Loss} = \log(\textrm{Prams})$


## <a id = "cp3">VQ-VAE</a>
    Neural Discrete Representation Learning
1. ## <a id="lib">前提</a>
    - VAE
        - 潜在変数を確率変数とする自己符号型深層生成モデル
        - 入力xをエンコーダで潜在変数zに符号化し，デコーダで複合x'
        - 潜在変数が従う分布として，多変量正規分布を仮定

    - Posterior Collapse
        デコーダが入力xをむしし，潜在変数zの事後分布が事前分布とほぼ変わらなくなること
        in case : 入力xが複雑，ネットワークの表現力が高い時

1. ## <a id="lib">VQ-VAE</a>
    - 潜在変数を量子化(離散化)したVAE
    - Posterior Collapseを解決
    - 後続モデル VQ-VAE2は，綺麗な画像を生成することで注目を集めた

    1. ベクトル量子化
        - 離散的な埋め込み空間を用意
        - encoderの出力$z_e(x)$を，最近傍の離散埋め込みベクトル$e_k$に対応させる
        - 対応する埋め込みベクトル$z_q(x)=e_k$をdecoderへ出力
    1. 損失関数
        $L = \log p(x|z_q(x)) + ||\textrm{sg}[z_e(x)] - e||_2^2 + \beta||z_e(x) - \textrm{sg}[e]||_2^2$
        上式を最小化．(sg : stop gradient)
        各項の意味は以下
        - 再構成損失
            入力と出力から，再現できるかを測る
        - VQ損失(Vector Quantization)
            埋め込み空間をencoderの出力に近づける
        - コミットメント損失
            encoderの出力を埋め込み空間に近づける


## <a id = "cp3">A3C</a>
    Asynchronous Methods for Deep Reainforcement Learning
1. ## <a id="lib">前提</a>
    強化学習のアルゴリズム

    - 強化学習
        エージェントは状態sに基づき，方策$\pi$を用いて行動aを選択する
        行動aが働きかけられた環境pは，今の状態sと行動aから次の状態s'と報酬を返す
        これを受けて，エージェントはパラメータ$\theta$を変えながら，より良い行動をとるよう方策を変えていく

    - より良い方策とは
        累積期待報酬$J(\theta)$が大きい方策
        強化学習は，累積期待報酬の最大化で実現できる，と仮定されている(ハウ州仮説)
        (多くの)強化学習は，累積期待報酬が最大化する方策の学習を目指す
        $\theta^* = \textrm{argmax}_{\theta}\mathbb{E}_p(\tau|\theta)\left[\sum_t r(s_t,a_t)\right] (= \textrm{argmax}_{\theta} J(\theta))$

    - どのように累積期待報酬を最大化するのか
        方策勾配法で最大化する
        - 方策勾配法
            勾配法で，累積期待報酬の最大化を目指す手法
            $\theta_{t+1}\leftarrow \theta_t + \alpha\nabla_{\theta}J(\theta)$
        - 方策勾配定理から，累積期待報酬の勾配は以下
            $\nabla_{\theta}J(\theta) \propto \mathbb{E}_{\pi}\left[\nabla\log\pi(a|\theta)Q_{\pi}(s,a)\right]$
            ここで$Q_{\pi}(s,a)$は行動価値関数で，$\gamma$は割引率
            $Q_{\pi}(s,a) = \mathbb{E}_{p(\tau|\theta)}[r_{t+1}+\gamma r_{t+2}+\gamma^2r_{t+3}+\dots|s_t,a_t]$

    - REINFORCE
        方策勾配法の代表的な価値関数
        累積期待報酬をモンテカルロ近似
        ベースラインを引くことで，バリアンスの低減(Advantage)
        →ベースライン：値を差し引き，その値を基準にすること

    - Actor-Critic
        方策Actorに加え，方策評価Criticも学習
        二つに分かれていることで，方策モデルに適用可能なモデルの自由度が向上

    - 強化学習での問題点
        自己相関の問題
        ・連続する経験の系列は，互いの相関が強い
        ・経験間の相関が，学習に非効率化/不安定化をもたらす
        非効率化
        →相関が強い
        →同じような振る舞いをするデータが多数いるような状況
        →情報が少ないという意味で非効率的
        不安定化
        →同じパターンを多く見るので局所解に陥りやすく，学習が不安定になる

1. ## <a id="lib">A3C</a>
    Asynchronos Advantage Actor-Critic
    - Asynchronous : 非同期処理
    - Advantage : アドバンテージの使用
    - Actor-Critic

    Acor-Critic方策勾配法に属する強化学習アルゴリズム
    分散非同期処理により，経験の自己相関に対応

    $$d\theta = \nabla_{\theta^{\prime}}\log\pi(a_t|s_t;\theta^{\prime})\left[\sum_{i=0}^{k-1}\gamma^ir_{t+i}+\gamma^k V(s_{t+k};\phi)-V(s_t;\phi)\right] - \beta\nabla_{\theta^{\prime}}\mathbb{E}_{\pi}\left[\log\pi(a_t|s_t;\theta^{\prime})\right]$$

    - 実装
        - Critic $V(s_t;\phi)$をベースラインにしたAdvantageを使用
        - 方策パラメータ$\theta$と，Criticパラメータ$\phi$を一部共有
            →Actorにsoftmax出力のCNN，Criticに線形出力のCNNを用い，出力以外共有
        - エントロピー項を追加し，局所界への収束を避ける

    - 非同期分散処理
        - 分散型強化学習
            複数のエージェントを並列に動作させ，結果を集約し方策を更新する
        - 非同期分散処理
            パラメータ同期を同時ではなく，時間差を設けて行う
            →tー1, t, t＋1を一つに集約するイメージ
            →経験の系列にばらつきが生まれ，自己相関が低減する


## <a id = "cp3">XAI</a>
    Explainable AI
1. ## <a id="lib">前提</a>
    - Deep NNでは高精度な予測が可能
    - 一方で，その判断根拠は人間にはわからない
    - 応用上，判断根拠の説明は必要
        ビジネスの意思決定など
    - XAI(Explainable AI)にて説明可能なAIを目指す

1. ## <a id="lib">LIME</a>
    モデルを決定境界近傍のデータ周りで線型近似することで，予測に重要なデータを説明する手法

    - 元データ $x\in\mathbb{R}^d$に対して，解釈可能な表現 $x^{\prime}\in{0,1}^{d^{\prime}}$
    - それぞれのサンプルを，$z\in\mathbb{r}^d,\,z^{\prime}\in{0,1}^{d^{\prime}}$
    - モデルを線形近似
    $f(z)\approx g(z^{\prime})=w_g\cdot z^{\prime}$
    - $f(z)$と$g(z^{\prime})$が近くなるように損失を最小化
    $\mathcal{L}(f,g,\pi_x) = \sum_{z,z^{\prime}\in\mathcal{Z}}\pi_x(z)(f(z-g(z^{\prime})))^2$
    ここで，$\pi_x(z)=\exp(-D(x,z)^2/\sigma^2)$で
    $D$は距離を測る関数，$\sigma$は幅
    xとzの距離が近ければ値が大きくなり，損失関数$\mathcal{L}$内で重要視される

1. ## <a id="lib">SHAP</a>
    協力ゲーム理論において，各プレイヤーの貢献度を表すShapley値を用い，各特徴量の予測への貢献度を定量化する手法

    - ゲーム理論
        複数のプレイヤーが各々の戦略に基づいて行動する時の状況を議論する理論


    |  | B協力 | B裏切り |
    | - | - | - | - | - |
    | A協力 | A=2, B=2 | A=0, B=3 |
    | A裏切り | A=3, B=0 | A=0, B=0 |

    - Additive feature attribution methods
        既存手法の多くは，以下のように定式化がきる($\phi$は重み→後のShapley値参照)
        - 解釈可能な特徴の各要素$z^{\prime}_i$に関する線形和(LIMEと同様)
        - $M$は解釈可能な特徴ベクトル次元

    $$
      g(z^{\prime})=\phi_0+\sum_{i=1}^M \phi_i z^{\prime}_i
    $$

    - Shapley値
        複数のプレイヤーが貢献した際，得られた利得を貢献度に応じて配分する値
        プレイヤーの登場順を含めて前通り考える
        →その平均値：Shapley値
    $$
      \phi_i(f,x)=\sum_{z^{\prime}\subseteq x^{\prime}} \frac{|z^{\prime}|!\,(M-|z^{\prime}|-1)!}{M!}\left[f_x(z^{\prime})-f_x(z^{\prime}\backslash i)\right]
    $$
    $|z^{\prime}|$は$z^{\prime}$の非0のの要素（実質的に考慮すべきもの）
    この式の解をSHAP値と定義し，Additive feature attribution methodの重みに用いる
    - 第一項：特徴量の組の出やすさ
    - 第二項：特徴量が追加された影響
        - $f$：モデルの出力
        - $z^{\prime}$：解釈可能な表現
        - $z^{\prime}\backslash i$：iを除いた解釈可能な表現


## <a id = "cp3">Metric Learnig</a>
    距離学習とも
1. ## <a id="lib">Metric Learning</a>
    - ある混在したデータに対して，類似データは近くに，そうでないものは遠くになるような埋め込みを学習する手法
    - クラス数が多いが，各クラスデータが少ない際に有効

1. ## <a id="lib">Siamese Network</a>
    - 入力：$X_1, X_2$
    - ニューラルネット$G_W$で埋め込み：$G_W(X_1), G_W(X_2)$
    - 埋め込み近さ$W_W$：$||G_W(X_1) - G_W(X_2)||$

    類似したもの(正例)は近づけ，そうでないもの(負例)は遠ざけるように学習

    - Contrastive Loss
        埋め込みの距離から定義された損失関数
        - $Y$はラベル．同じクラスで1，異なるクラスで0をとる
            前者では$L_I$，後者では$L_G$
        - $L_I$は$E_W$の増加で大きく，$L_G$は$E_W$の増加で小さくなるよう設計
    $$
      E_W(X_1, X_2) = ||G_W(X_1) - G_W(X_2)||\\
      L(W, Y, X_1, X_2) = (1-Y)L_G(E_W) + YL_I(X_2)
    $$

    - 改善点
        類似度の判断に文脈を考慮できなかった
        AとBを比較した際，似ていると判断されたものの
        別のA'とBを比較した際，似てない場合を考慮できなかった
        →何を類似の根拠とするのか，その明示が必要であった
        →そもそも，2つのみの入力から判断しているため，当然でもある

1. ## <a id="lib">Triplet Network</a>
    Siamese Networkから3入力にしたもの
    データ類似度の判断に文脈が必要であったSiamese Networkの弱点を克服

    - 入力：$x$，それらの正例$x^+$と負例$x^-$
    - ニューラルネット$Net$で埋め込み
    - 正例・負例ごとの距離を計算：$||Net(x) - Net(x^+)||_2$, $||Net(x) - Net(x^-)||_2$
    - Triplet Loss：正例の距離に対して，負例の距離が相対的に遠くなるよう調整
        スケールをとることで，絶対的な値の比較でなく，相対的な比較ができる
        相対的な比較に持ち込むことで，文脈の定義が不要
    $$
      Loss(d_+, d_-) = ||(d_+, d_- - 1)||_2^2 = const.\cdot d_+^2
    $$

    $$
      d_+ = \frac{\exp(||Net(x) - Net(x^+)||_2)}{\exp(||Net(x) - Net(x^+)||_2) + \exp(||Net(x) - Net(x^-)||_2)}
    $$

    $$
      d_- = \frac{\exp(||Net(x) - Net(x^-)||_2)}{\exp(||Net(x) - Net(x^+)||_2) + \exp(||Net(x) - Net(x^-)||_2)}
    $$

    (距離の右下添え字はノルム．2であればL2ノルム)
    (絶対値記号1つは，ただの絶対値．2つはノルム．ノルムは簡単にはベクトルの大きさ．ユーグリット距離とも似ているようで異なる．)
    https://qiita.com/muripo_life/items/f122526a38bb75ba02f2


## <a id = "cp3">MAML</a>
    Model-Agnostic Meta-Learning for Fast Adoptation of Deep Network
    メタ学習の手法
1. ## <a id="lib">メタ学習</a>
    学習に必要なもの(ハイパーパラメータや学習アルゴリズム，損失関数など)についても学習を行う，階層的な学習

    [メタパラメータ] →メタ学習→ [学習率，学習アルゴリズム，損失関数] →通常の学習→ [NNのパラーメータ]

1. ## <a id="lib">MAML (Model-Agnostic Meta-Learning)</a>
    Few-shotで未知タスクに適応できるような初期値，を学習するメタ学習アルゴリズム

    [メタパラメータ] →メタ学習→ [(学習率，学習アルゴリズム，損失関数)→初期値] →通常の学習(タスク$i$)→ [NNの最適パラーメータ$\theta_i^*$]

    - 勾配法の二重ループで最適化(多くの場合)
        1. 各タスク$i$に対する勾配法による学習(普通のNN学習)
            - $\mathcal{L_{T_i}}$：iの損失
            - $f_{\theta}$：モデル出力
            - $\alpha$：学習率
            - Few-shotで行われる
        $$
          \theta_i^{\prime} = \theta - \alpha\nabla_{\theta}\mathcal{L_{T_i}}(f_{\theta})
        $$
        1. 全体の最適化
            - $\beta$：学習率
            - $p(\mathcal{T})$：タスクの分布
            - 各タスクにFew-shotで適応できるように最適化
            各タスクで更新された$\theta_i^{\prime}$で計算(few-shotで損失が小さくなった点)
            更新後の$\theta$で各タスクの総和に対して勾配法をとり，最小化させる
        $$
          \theta \leftarrow \theta - \beta\nabla_{\theta}\sum_{\mathcal{T_i}\sim p(\mathcal{T})}\mathcal{L_{T_i}}(f_{\theta_i^{\prime}})
        $$

    - 学習ができる根拠
        - 1段階目の勾配法で，タスクごとの損失が減るようにパラメータを更新
        - これを学習を通じてfew-shotで行われている
        - 最終的にたどり着く解も，「そこから勾配法をすれば，few-shotで各タスクの損失が小さくなる」ような解になっている


## <a id = "cp3">Grad-CAM</a>
    Visual Explanations from Deep Networks via Gradient-based Localization
1. ## <a id="lib">Grad-CAM</a>
    - 画像に対する判断根拠を可視化する手法
        →予測値の勾配が大きいピクセルを重要なピクセルとする

    1. CAM
        - 特徴
            - Dense層の重みで特徴マップを重みづけ，クラスに対する出力を計算
            - GAP後の特徴マップは，クラス判断の根拠となった特徴が残っているはず
            - 重みは，その特徴の重要度を反映
            - 出力＝ヒートマップとして可視化
        - 問題点
            - 使えるアーキテクチャに制限
                Convした後です，とかGAP使いますとか
    1. Grad-CAM
        CAMの問題点を改善
        - 特徴
            - CAMを正規化したもの(CAMの一般化)
            - CAMでのDense層の重みを用いていた部分を，出力に関する特徴マップの微分で重みづけ
                アーキテクチャ依存がなくなった(汎用性が高くなった)
                勾配法で楽手できる
            - ReLUにより，正のみ採用
        - 問題点
            - 全体的にここが重要だ，というぼんやりとした情報しかわからない
                具体的にここのピクセルがどう重要か，がわからない
    1. Guided Grad-CAM
        より精密な推論根拠の可視化
        既存のGuided BackpropとGrad-CAMの組み合わせ

        - Guided Backprop
            判断根拠可視化の手法
            ピクセルを動かし，出力がどう変わるか学習していく手法
            ピクセルレベルでの重要度がわかる
            一方，この手法だけでは可視化が不十分であった
            Grad-CAMと組み合わせ，正確になった


## <a id = "cp3">Speech Processing</a>
    音声処理分野
1. ## <a id="lib">前提</a>
    - フーリエ変換
        時間領域を周波数領域へ変換
        時間領域の無限個の重ね合わせで表現
        $-\infty$から$+\infty$まで連続的に積分
        - STFT 短時間フーリエ変換
            窓関数で区切られた範囲を積分
        - DFT 離散フーリエ変換
            標本点(N個)で離散的に変換
        - FFT 拘束フーリエ変換
            DFTを高速に行う
            $O(N^2)\rightarrow O(N\log N)$へ
            うまいこと周期性を利用して，要素をまとめ計算コストを下げて高速化
            (オイラーの公式の周期性)
    - メル周波数ケプストラム係数(MFCC)
        音声処理で用いられる，古典的な特徴量
        - 信号に対してフーリエ変換
        - 得られた周波数のパワースペクトラム$f$をメル尺度へ変換
        $m = 2595\log_{10} \left(1+ \frac{f}{700}\right)$
        - メル周波数ごとにケプストラムを求める
            フーリエ変換の対数を逆フーリエ変換
        - 離散コサイン変換から得られた振幅＝MFCC
        $C_n = \sqrt{\frac{2}{k}}\sum_{k=1}^K (\log S_k)\cos[n(k-0.5)\pi/ k]$
        $n=1,2,\cdots,N$


## <a id = "cp3">CTC</a>
    Connectionist Temporal Classfication:
    Labelling Unsegmented Sequence Data with Recurrent Neural Networks
1. ## <a id="lib">CTC Connectionist Temporal Classfication</a>
    - 古典的なend2endなneural音声認識モデル
    - ネットワークにはBi-directional LSTMを使用
    - 入力・出力の系列長の違いを吸収し，音声データに対応
        発音における空白のタイミングや，同じ音節にい続ける点を「パス」を導入し表現
        →空白文字の削除
        →連続する文字の削除


## <a id = "cp3">GCN</a>
    GCN (Spectral-based)
1. ## <a id="lib">前提</a>
    - グラフ畳み込み
        - 画像と同じようにグラフ上での畳み込みがモチベーション
        - グラフ：辺と頂点lあらなる図形

    - Spextral GCN
        信号$x$と，フーリエ空間上での$g_{\theta}=diag(\theta)$との要素石としてグラフ畳み込みを定義
        ($\theta$：フーリエ係数のベクトル)
        - 畳み込み定理：畳み込みのグラフフーリエ変換がグラフフーリエ変換の要素積
        - 直感的には，周波数成分から信号の滑らかさを見るイメージ
        $$g_{\theta}\star x = Ug_{\theta}U^{\top}x$$
        $U^{\top}$がグラフフーリエ変換
        - 問題点
            - 空間的な局所性が保証されない
            - フィルターのパラメータ計算で$O(N)$
            - 固有ベクトルの計算で$O(N^2)$
    - ChebNet
        Spectral GCNの問題点を解決
        - フィルター$g_{\theta}(\Lambda)$を$K$次チェビシェフ多項式で近似
             $K$を変化させて局所性を調整
             フィルタの計算量が$O(N)\rightarrow O(K)$に
             再帰的な計算が可能になり，計算量が$O(N^2)\rightarrow O(KE)$
             →$E$：グラフのエッジ数


## <a id = "cp3">Self-supervised Learning</a>
1. ## <a id="lib">Self-supervised Learning</a>
    自己教師あり学習
    - ラベルなしデータからラベルを作り，教師あり学習を行う

1. ## <a id="lib">SimCLR</a>
    - 同じデータ$x$に対して，異なるデータ拡張を行う$\tilde{x}$
        $f(\tilde{x})\rightarrow h,\,g(h)\rightarrow z$
    - 正例のペアに対しては出力$z$が類似するように，負例のペアには$z$が類似しないように，Contrastive Lossを最小化
    - 結果
        教師あり学習には劣るが，モデルを大きくすることで精度向上
        →教師ありにも匹敵する精度

1. ## <a id="lib">BYOL</a>
    - 負例を必要としない自己教師あり学習
    - オンラインの予測とターゲットが小さくなるように，オンラインを学習
        ターゲットはオンラインの指数移動平均
    - 結果
        自己教師ありのSOTAであったSimCLRを上回る結果


## <a id = "cp3">Wasserstein GAN</a>
1. ## <a id="lib">前提</a>
    - GAN
        生成期$G$は識別器$D$を騙すデータを生成するように学習する
        $$
        \underset{G}{\min}\,\underset{D}{\max}\,V(D,G) = \mathbb{E}_{x\sim p_{data}(x)}[\log D(x)] + \mathbb{E}_{z\sim p_z(z)}[\log (1-D(x))]
        $$
    - Jensen-Shannon (JS) ダイバージェンス
        - ある$G$に最適な$D$である$D_G^*$は，真と偽の分布に対する割合と同価
        $$
        D_G^*(x) = \frac{p_{data}(x)}{p_{data}(x)+p_g(x)}
        $$
        - $p_{data}$と$p_g$のJSダイバージェンス$D_{JS}(p_{data}||p_g)$は以下のように変形される
            $\frac{p_{data}+p_g}{2}$は二つの中間的な位置
        $$
        D_{JS}(p_{data}||p_g) = \frac{1}{2}D_{KL}\left(p_{data}||\frac{p_{data}+p_g}{2}\right) + D_{KL}\left(p_g||\frac{p_{data}+p_g}{2}\right)
        $$
        $$
        = \frac{1}{2}\left(\log 2 + \int p_{data}\log\frac{p_{data}}{p_{data}+p_g}dx\right) + \frac{1}{2}\left(\log 2 + \int p_g\log\frac{p_g}{p_{data}+p_g}dx\right)
        $$
        $$
        = \frac{1}{2}\left(\log 4 + L_{GAN}(D^*,G)\right)
        $$
        - 上式より，GANはJSダイバージェンスの最小化
    - ダイバージェンスとGANの学習不安定さ
        - KLダイバージェンスは2つの分布の比で距離を測る
        $$
        KL(\mathbb{P}_r||\mathbb{P}_g)=\int\log\left(\frac{P_r(x)}{P_g(x)}\right)P_r(x)d\mu(x)
        $$
        $$
        JS(\mathbb{P}_r,\mathbb{P}_g)=KL(\mathbb{P}_r||\mathbb{P}_m) + KL(\mathbb{P}_g||\mathbb{P}_m)
        $$
        - $P_r=0$や$P_g=0$では分布の離れ具合を適切に測れない
            →データが低次元にある時など
        - GANの学習の不安定さは，ダイバージェンスを最小化しているため
    - Earth-Mover(EM)距離 / Wasserstein-1距離
        ある砂山から，別の砂山へ砂を移動する最適な輸送計画の費用
        - EM距離は2つの分布の差で距離を測る
        $$
        W(\mathbb{P}_r,\mathbb{P}_g)=\underset{\gamma\in\Pi(\mathbb{P}_r,\mathbb{P}_g)}{\inf} \mathbb{E}_{(x,y)\sim\gamma}[||x-y||]
        $$

1. ## <a id="lib">Wasserstein GAN</a>
    - Earth-Mover距離を最小化するGAN
    - Kantorovich-Rubinstein双対性から，Wasserstein距離は以下
    $$
    W(\mathbb{P}_r,\mathbb{P}_g) = \underset{||f||\leq 1}{\sup}\mathbb{E}_{x\sim \mathbb{P}_r}[f(x)] - \mathbb{E}_{x\sim \mathbb{P}_{\theta}}[f(x)]
    $$
    - $f$が1-Lipschitz関数であれば，下式を解けば良い(GANと類似)
    $$
    \underset{w\in W}{\max}\,\mathbb{E}_{x\sim \mathbb{P}_r}[f_w(x)] - \mathbb{E}_{z\sim p(z)}[f_w(g_{\theta}(z))]
    $$
    - 1-Lipschitz性を保つために重みをクリッピング
        固定した定数$c$の間に収める
    $$
    w\rightarrow \textrm{clip} (w,-c,c)
    $$


## <a id = "cp3">Continual Learning</a>
    Continual Learning with Deep Generative Replay
1. ## <a id="lib">前提</a>
    - 一般に機械学習ではタスクが学習中に変化しない
    - 一方，人間は変化する環境の中で新しいタスクを次々にこなす
    - 機械学習でもその流れを汲みたい：継続学習 Continual Learning
        次々に新しいデータが現れる中で継続的に学習
    - 継続学習の問題点：破滅的忘却 Catastrophic Forgetting
        勾配法で学習されたニューラルネットワークは，新しいタスクの学習ですぐに昔のタスクを忘れてしまう

    - 破滅的忘却を人間の記憶方法を模して解決を試みる
        記憶を司る相補的なモジュールと，昔の経験を再度繰り返し(忘却が遅くなりそう)が必要そう
        - Complementary Learning System(CLS)
            人間の脳では，海馬(短期的な記憶)と新皮質(長期的な記憶)とが相補的な役割を担う：Complementary Learning System(CLS)
        - 記憶の定着
            人間の脳では，過去の経験を脳内で繰り返し定着されると考えられている

1. ## <a id="lib">Deep Generative Replay</a>
    - CLSに倣い，タスクを解くネットワークとそれを補う生成モデルを使用
    - GANで昔のデータを擬似的に生成し，過去のタスクの忘却を防ぐ
    - 新しい生成モデルは実際のデータと生成されたデータ両方で学習


## <a id = "cp3">World Models</a>
    外界を表現する強化学習
1. ## <a id="lib">前提</a>
    - 人間の脳内は絶えず脳内に作った外界のモデルを使って予測をしていると言える

1. ## <a id="lib">World Models</a>
    - 外界の表象を生成：Vision Model(V)
        VAEで外界の縮約表現を作る
    - 外界のダイナミクスを予測：Memory RNN(R)
        RNNの出力を混合ガウス分布でモデリング
    - Rに基づき行動を生成：Controller(C)
        線形モデルを用いる
        Cの最適化に共分散行列適応進化戦略(CMA-ES)を使用

1. ## <a id="lib">結果</a>
    - ベンチマークタスクを学習可能
    - 実環境ではなく，World Modelsの中でのみ学習を行い，学習された方策を実環境に適用
    - World Modelsの中だけでも一定程度の性能獲得


## <a id = "cp3">Individual Treatment Effect</a>
    Ewstimated individual treatment effect: generalization bounds and algorithms
1. ## <a id="lib">前提</a>
    - Causal Inference
        - 一般的な統計的機械学習では相関しか学習できない
        - 因果を知りたい場面では，相関が必ずしも意味をなすとは限らない

    - 因果と介入
        ある介入を行うか否かで結果が変わる時に因果関係を認める
        - 定式化
            Individual Treatment Effect (ITE)
            $$
              \tau(x) = \mathbb{E}[Y_1 - Y_0 | x] = m_1(x) - m_0(x)
            $$
            特徴量$x$から$y$が引き起こされる
            介入の有無$t=\{0,1\}$で2つの潜在的な結果$y=Y_0, t=0$と$y=Y_1, t=1$
            $m_1(x)=\mathbb{E}[Y_1 |x], m_0=\mathbb{E}[Y_0 |x]$

1. ## <a id="lib">Counterfactual Regression</a>
      - 目的関数
          介入の有無で条件づけられた特徴ごとに損失を最小化
      - Integral Probability Metric (IPM)
          統制群と治療群の間の距離を測る
          IPMをペナルティ項として加えることで，介入の有無による不均衡と予測精度のトレードオフを考慮
          - 背景
              ITEを知りたい，ITEを精度良く推定したい
              真のITEと予測のITEのさの平均であるPEHE loss(the expected precision in estimation of heterogeneous effect loss)を小さくしたい
              PEHEは，一定の条件下でIPMを含む項以下の値となる
