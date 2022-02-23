<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [['$', '$'] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });

</script>

# [My kicks](#mykicks)

## <a href="#index">Index</a><a id="index"></a>
* [Chapter 1](#cp1)
    * [Library](#lib)

## <a id = "cp1">20220101</a>
1. ## <a id="">UCB1アルゴリズム</a>
    1. UCB1アルゴリズム
        最初にとりうる行動を一通り行う．
        信頼区間の上限値を加味した最良のケースでの報酬期待値から最適な行動を決めて実行．
    1. 貪欲法
        ある一定の確率で探索と活用をそれぞれ行い続ける．
    1. $\epsilon$-greedy
        最初にまとめて探索を行う．
        最大の報酬が得られた行動を固定し，以後活用のみ行う．
    1. トンプソンサンプリング
        ベイズ戦略の一種．
        事後確率に従って行動をランダムに選択．

1. ## <a id="">擬似逆行列</a>
    線形回帰やPCAのようなMLで用いられる線形モデルの多くは行列$\bm{X}\bm{X}^{\textrm{T}}$に依存．
    一方，この行列が特異である場合，擬似逆行列を用いて解くことができる．
    $$
      \bm{X}^{+} = \lim_{\alpha\rightarrow\infty}\left(
        \bm{X}\bm{X}^{\textrm{T}} + \alpha\bm{I}
        \right)^{-1}\bm{X}^{\textrm{T}}
    $$

1. ##<a id =""></a>
