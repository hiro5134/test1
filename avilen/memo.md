# [My kicks](#mykicks)

## <a href="#index">Index</a><a id="index"></a>
* [Chapter 1](#cp1)
    * [Library](#lib)
    * [Higher API](#higherapi)
* [Chapter 2](#cp2)
    * [活性化関数](#mlp)
    * [万能近似定理 Universal Approximation Theorem](#uat)
    * [出力ユニットとタスク](#unit)
    * [損失関数](#loss)
* [Chapter 3](#cp3)


## <a id = "cp1">Chapter 1</a>
1. ## <a id="lib">Library</a>
    | Lib | Graph | Company | Year | memo |
    | - | - | - | - | - |
    | TensorFlow | Define and Run | Google | 2015 | 計算グラフを自分で定義 |
    | Chainer | Define by Run | Preferred Networks | 2015 | 2019年開発終了 |
    | PyTorch | Define by Run | Facebook | 2016 | 計算方法がnumpyに似てる |
    | TensorFlow 2 | Define by Run | Google | 2019 | シンプルな実装可能 |
    | Apache MXNet | Define and Run <br> Define by Run| AWS | 2017 | 静的・動的どちらも可能|
    | Caffe2 | Define and Run | Facebook | 2017 | 2018年PyTorchへ統合 |
    | Congnitive Toolkit (CNTK) | Define and Run | Microsoft | 2016 | 音声認識特化 |
    | theano | Define and Run | モントリオール大学 | 2007 | 2017年開発終了 |
1. ## <a id="higherapi">Higher API</a>
    | API | Company | Year | memo |
    | - | - | - | - |
    | Keras |  Google | 2015 | TF用のAPI(TF2から標準API) |
    | Gluon | AWS, Microsoft | 2017 | MXNet用のAPI |

## <a id = "cp2">Chapter 2</a>
1. ## <a id="activation">活性化関数</a>
    中間層の表現を非線形にするため．  
    表現力の向上
    - step関数  
        勾配が0になり最適化が難しい
    - sigmoid関数
        0~1  
        勾配消失が起こり，中間層の最適化に不向き
    - softmax関数  
        複数の入力を扱える  
        出力の合計が1
        勾配消失が起こり，中間層の最適化に不向き
    - tanh関数  
        -1~1
        勾配消失が起こり，中間層の最適化に不向き
    - ReLU関数  
        x>0で勾配が計算可能で勾配が消失しない  
        x<0での勾配を計算するために以下の派生が存在  
        - Leaky ReLU  
            x<0に緩やかな傾き
        - Randomized ReLU  
            x<0の傾きをランダムに変更(予測時は平均値に固定)
        - Parametric ReLU  
            x<0の傾きを学習
    - MAXOUT関数  
        ReLU関数の一般化  
        要素数kのグループから各グループの最大値を抽出  
        ReLU関数や二次関数などに近似可能
        ReLu関数よりも表現力が高く勾配が消えない   
        活性化関数自体を学習

1. ## <a id="uat">万能近似定理 Universal Approximation Theorem</a>
    3層モデルの中間層のノードを極限まで増やせばあらゆる関数を近似可能  
    →現実的でない  
    →活性化関数により，層を横に伸ばすことで表現力をあげられる（計算コストも少なく収まる）  
    →万能近似定理+活性化関数でDLが飛躍

1. ## <a id="unit">出力ユニットとタスク</a>
    | Task |  | Unit | Activation Func. | Loss Func. | Probability | memo |
    | - | - | - | - | - | - | - |
    | 回帰 |  | 線形ユニット | 恒等関数 | MSE | ガウス分布 | 連続値を予測<br>目的変数（連続値）の分布をガウス分布と仮定<br>出力値は目的変数の分布（条件付きガウス分布）の平均値を返そうとする|
    | 分類 | 二値分類 | シグモイドユニット | sigmoid関数 | Binary Cross Entropy | ベルヌーイ分布 | ラベルが1である確率を予測<br>目的変数の分布は二項分布<br>ベルヌーイ分布を出力|
    | | 多値分類 | softmaxユニット | softmax関数 | Cross Entropy | | ラベルごとに確率を予測 |

1. ## <a id="loss">損失関数</a>
    尤度の最大化　損失関数の最小化　となるように設計

## <a id = "cp3">Chapter 3</a>
1. ## <a id="batch">バッチ処理</a>
    オンライン学習 入力１つ
    バッチ処理　入力nこ　あらゆる場所がn次元になる
        sum撮るときはdim=1
        基本サンプルが行，説明変数が列なので列方向に足していくことでサンプルごとのsumが取れる

1. ## <a id="minibatch">ミニバッチ処理</a>
    バッチ処理　データ数が膨大であれば計算量も膨大にありパラメータの更新が遅い
    →データを分割してバッチ処理をする
    | Task | 勾配推定 | 収束速度 |
    | - | - | - |
    | バッチサイズ大 | 正確 | 遅い |
    | バッチサイズ小 | 誤差を高める | 早い |
    　　
1. ## <a id="adapt">最適化手法</a>
    1. ## <a id="">最急降下法</a>
        全体像はわからないが，その地点での最短経路方向に更新
        →求めた勾配方向とは逆向きに，その大きさ*η(学習率)を更新

        最急降下法ではlocal minimaに陥る可能性

        η小　時間がかかる　最適な場所を見つけられる可能性
        η大　早い　値がブレて最適な場所を見つけられない可能性
    1. ## <a id="">SGD 確率的勾配降下法</a>
        確率的な山の一地点で最短経路方向に更新
        ミニバッチ抽出にランダム性を持たせ，損失関数が確率的になる

        最急降下法の弱点を克服
        （これまで）学習率を確率的に変化
        →損失関数が複雑すぎてうまくいかない

        そこでSDGはデータを確率的に変える
        →データをシャッフルして，それぞれの損失関数の挙動を変える
        →あるミニバッチでは上がり，他方では下がる，などができ最適な場所を見つけられる

        一方で損失関数の形状が急峻な場合，振動してしまう

    1. ## <a id="">モメンタム</a>
        移動平均を導入（慣性項）
        精度を保ちつつ，収束速度を早くする

        SDG＋慣性の法則→モメンタム

    1. ## <a id="">ネステロフのモメンタム</a>
        慣性項なしで更新した場合に慣性項をたしあわせ
        →ブレーキの役割

    1. ## <a id="">AdaGrad</a>
        過去の購買の二乗和を記憶して学習率を調整

        今までの勾配が大きい　学習率小さく更新
        今までの勾配が小さい　学習率大きく更新

        問題点
        学習率が0になる可能性
        →局所解

    1. ## <a id="">RMSProp</a>
        古い情報を忘れ，新しい情報を反映しやすくした

    1. ## <a id="">Adam</a>
        現在のスダンダード

        イテレーション数でバイアス補正
        →初期段階の不安定さを解消

        
