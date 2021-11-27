# [My kicks](#mykicks)

## <a href="#index">Index</a><a id="index"></a>
* [Chapter 1](#cp1)
    * [Library](#lib)
    * [Higher API](#higherapi)
* [Chapter 2](#cp2)
    * [MLP基礎](#mlp)
    * [順伝播](#fp)
    * [誤差逆伝播法](#bp)


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
1. ## <a id="mlp">活性化関数</a>
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

1. ## <a id="fp">万能近似定理</a>
    3層モデルの中間層のノードを極限まで増やせばあらゆる関数を近似可能  
    →現実的でない  
    →活性化関数により，層を横に伸ばすことで表現力をあげられる（計算コストも少なく収まる）  
    →万能近似定理+活性化関数でDLが飛躍

1. ## <a id="bp">誤差逆伝播法</a>
