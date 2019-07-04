## series_Image_GPについて

1. ### やりたいこと  
    拡散強調像からリンパ節とされる明点を抽出したい  

1. ### 背景  
    1. 各画像によって拡散強調像の見え方や明度が異なるため，画一的なフィルタの組み合わせ方や各フィルタのパラメータ設定が困難  
    1. フィルタの組み合わせ方とパラメータの配置の最適化問題と捉えることが可能
1. ### 進化計算での検討  
      入力：拡散強調像  
      ターゲット：手動で生成した二値化画像  
      遺伝子：各種画像処理フィルタ  
      遺伝子表現型：木構造

1. ### 入力・ターゲット例  
    表示は拡散強調像（←），リンパ部分二値化画像（→）  
    1. 例1  
        <img width="400" alt="00000010 DWI" src="https://drive.google.com/uc?export=view&id=1BtS4-V599sWbgElqdGz8XCXxO_LiLHUu"><img width="400" alt="00000010 ANN" src="https://drive.google.com/uc?export=view&id=14ZCkmkib-6CdMsmSFpw2i-pDwzrirDjk">
    1. 例2  
        <img width="400" alt="00000001 DWI" src="https://drive.google.com/uc?export=view&id=1y7cbOemRy6J0OWfg_KoUqB0weOsl-5kU"><img width="400" alt="00000001 ANN" src="https://drive.google.com/uc?export=view&id=1xYchgKiMT15nIDcfWbriCk63wQK7zYlq">
