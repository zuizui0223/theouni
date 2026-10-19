# 52リポ「普遍性」再精査 V2 — 最新コミット・結果台帳・データ共有関係・投稿設計

**監査日:** 2026-10-19 JST  
**母集団:** \`zuizui0223\` の53リポからWebサイトを除いた52研究/開発リポ。各リポの直近3コミットと最新コミットのchanged filesをGitHub経由で確認。主要結果のsource-locked JSON/原稿/検証スクリプトも個別照合。  
**全52最新コミット指標:** [PORTFOLIO_52_LAST_COMMIT_INDEX_20261019.json](PORTFOLIO_52_LAST_COMMIT_INDEX_20261019.json)。ここには12桁SHA prefixを保存。最新とは監査時点の観測値であり将来のHEADを約束しない。  
**限界:** 全52の全コミット・全ブランチを時系列再構成したわけではない。全学術論文のprior art系統的レビュー、全生データの独立再実行、全GitHub Actionsアーカイブ再集計も実施していない。「支持済み」はsource-locked研究台帳の確認であって独立再現試験の新規PASSではない。

## I. 最も大切な修正：README最新版だけでは科学状況が見えない

1. **FCP** 最終の実画像ROIは **4,475植物種 / 447,500実測画像 / 227,107四値判定画像**。旧199,700実測/447,500 pendingは期限付きの履歴。全域組成をシャッフルする50km比較では **1,761種、平均差0.0176149、p=0.005**。対照的に5km同月年内ラベルシャッフルは194種 p=0.300 / 高ペア数14種 p=0.275、**追加のfine-local偏りは不支持**。異年同月・4観察者で1km圏内異色再記録の候補8種も複色花・花齢・ROI残差を除外できず、遺伝的多型維持ではない。根拠：[source-specific月帰無](https://github.com/zuizui0223/fcp/blob/main/docs/FCP_LOCAL_POLYMORPHISM_MAINTENANCE_VS_SPECIATION_20261018.md)、[再発候補](https://github.com/zuizui0223/fcp/blob/main/docs/FCP_RECURRENT_LOCAL_PHOTO_MORPH_QA_AND_MAINTENANCE_IDENTIFIABILITY_20261018.md)、[JSON](https://github.com/zuizui0223/fcp/blob/main/results/fcp_local_photo_coexistence_month_null_verified_20261018.json)。
2. **TURNOVER** 元の「時間×空間・形質×相互作用」の合同系列は適格ゲートHOLDだが、独立に設計された植物の時間的形質記憶系列は **201科×形質系、45科、12形質**で実データ終結。科反復性0.150 [0.020,0.286]、形質0.043 [0,0.134]、系固有/残差0.806。leave-one-family-outで形質名からの持越し増分 −0.024 p=.091（prune-only −0.032 p=.193）。**形質の記憶の存在と、強度の系統間転用の未確認を区別する**。科>形質の分散比有意差は事前の精度ゲートHOLD。根拠：[biology/result](https://github.com/zuizui0223/turnover/blob/main/docs/TRAIT_MEMORY_CONTEXT_SYNTHESIS_V0_1.md)、[paper boundary](https://github.com/zuizui0223/turnover/blob/main/docs/PUBLICATION_BOUNDARY_V0_1.md)、[source-gate JSON](https://github.com/zuizui0223/turnover/blob/main/data/trait_memory_route_v0_1.json)。
3. **MOIS** READMEの309,439写真は現行収集の最終数ではない。10月19日最新HEADは **350,399 actual-photo source cohortの季節/分類群4項分解ワークフロー**とテストを追加した。外部Action/releaseの最新数値をこの監査で独立取得できていないため、350,399という原画像数を「350,399の色分類または温暖化効果確認」とは書かない。既存の30万件超の実測側での雨量/蒸気圧の全球正関連は厳密地理セル内ではCIが0を含み、写真比率に限定される。[latest commit](https://github.com/zuizui0223/mois/commit/badaa7816d42)、[historical source model](https://github.com/zuizui0223/mois/blob/main/README.md)。
4. **EGWE** 既存EGC機構をピン留めした新4条件×256軌跡の「形質不在・遺伝的資源あり」を実行。各初期(q,p)における第1世代再出現/第12世代存在：(.2,.04)=63/256・7/256、(.2,.40)=233・74、(.8,.04)=86・4、(.8,.40)=250・78。**発現可能性≠短期反復≠12世代の存在≠自然界適応度**。高q初期状態は固定せず後に下がる。源コード内モデルに限った結果。[実行結果](https://github.com/zuizui0223/egwe/blob/main/artifacts/egc_trait_reappearance/establishment_window_4cell_256seed_20261019_summary.json)。
5. **ANTO** 新v9は過去史の予測力が「不完全に測られた現在の遺伝/発生資源」を代理し得ることを条件付きのexact Brier riskで例証。可視白花のみ0.0475、歴史付0.045、機能資源完全測定0.030、資源+歴史0.030。自然の祖先喪失/再発現は未実証。[v9](https://github.com/zuizui0223/anto/blob/main/docs/HISTORY_MEDIATION_AND_HIDDEN_STATE_SUFFICIENCY_V9.md)。
6. **AZA3** 公開C. japonicum転写配列26のうち旧5候補DFR/ANS似配列で、7酵素参照+ANR/FLS近縁酵素対照+参照省略に頑健なのは **2/5**。配列類似は白花の発現可能性でも歴史的色素再獲得でもない。[v4](https://github.com/zuizui0223/aza3/blob/main/docs/ANTO_CIRSIUM_PARALOG_SPECIFICITY_AND_HEAD_CHEMISTRY_V4.md)。
7. **SCH / BALANCE** SCHでは実験操作下のGymnadenia開花開始の選択傾斜 +0.094 → −0.066（差−0.160）。任意共分散の最悪SE上界0.059、単一比較の保守的正規近似p上界約.0067。ただし20探索比較族全体のBonferroni上界約.134で、純機能最適値の直接実験同定ではない。BALANCEのU1 47花種記録/U2 22記録の機能ペア別レビューで **Mimulus aurantiacus と Ipomopsis aggregata**は同一種でも調べた機能ペアが異なると「検出された対立」の結論が違う。U1/U2は非同質な抽出枠、0/47対8/22は頻度比較不可。[SCH定量境界](https://github.com/zuizui0223/sch/blob/main/docs/SCH_GYMNADENIA_COVARIANCE_ROBUST_GRADIENT_CONTRAST_V1.md)、[BALANCE原出典分担](https://github.com/zuizui0223/balance/blob/main/docs/BALANCE_PLANT_CROSS_FRAME_FUNCTION_PAIR_SPECIFICITY_V1.md)。
8. **ESDM** 同一8分類群のカメラ出現データで28組中15比較可能、5組は季節ベースの夜昼相対順序が逆、leave-one-siteに頑健2組。年×月の細かい条件では12比較可能、3組逆転、頑健1組。観測源/地理/分類群別検出率の混同は残り、実際の活動時間・競争の転換とは言えない。[機械結果](https://github.com/zuizui0223/esdm/blob/main/docs/replication/E4_EIGHT_TAXON_SITE_TIME_RESULT_RECEIPT.json)。
9. **SDMR** 2026-10-19のM5主軸はknown-truth 71/80 positive process recovery。一方real-plant 50分類群では2 learner共通sharp =16/300しかなく、事前0.80基準を不支持。方法上の成功を植物環境ドライバーの同定と混同しない。[empirical boundary](https://github.com/zuizui0223/sdmr/blob/main/manuscript/PROCESS_INFORMATION_EMPIRICAL_SCOPE_LEDGER.md)。
10. **THEOUNI C2 / REC** 実狐・アナグマ/カワウソの記録を使う後付け観測デザイン試験では、上流真値情報が安価ならその取得が有利で、価格比3:1では逆転。カワウソpilot診断のMAE0.119/0.125は最良固定AB10の0.117に勝てない。**適応観測の存在定理やMRODの合成ベンチは、実生物で常に適応選択が勝つことを意味しない**。[source-linked C2](https://github.com/zuizui0223/theouni/blob/main/research/C2_EMPIRICAL_INTERVENTION_REPLAY_2026-10-19.md)。
11. **EOG 11島** latest headはHelgeland公表コロニー直接陽性における初回再検出時の島コードの食い違いと、11島保全/農場群の感度。これは検出地点分類の差であり独立な移入/繁殖/SDM優越の証拠ではない。[gate](https://github.com/zuizui0223/eog/blob/main/docs/eog_helgeland_11island_habitat_paired_v1.md)。
12. **CREST SeedClim** 原SeedClim資料の12site/69block/412plot/356turfを見たメタデータ整合ゲート。17blockが命名揺れを修正必要だったが、種子銀行とその後の植生のrow-level正規joinは **HOLD**。状態資源の独立自然実証にはまだ使えない。[source gate](https://github.com/zuizui0223/crest/blob/main/docs/crest_seedclim_multisite_carrier_gate_2026-10-19.md)。

## II. 「普遍性」を3種類に分ける

**(A) 反復性 / recurrence**: 同じパターンが異なる対象で何度も観測される（符号や境界の共有）。  
**(B) 転移可能性 / portability**: 一部で学習した効果量・条件付き構造が、未使用の科/種/場所にも予測情報を与える。  
**(C) 機構の共通性 / mechanistic invariance**: 異なる生物群で同じ因果操作が同じ生態過程を生み、交絡・観測方式を越えて説明する。

「複数のリポが同じ言葉を使う」=AでもBでもCでもない。数学的共通定理は一般的な条件付き主張であり、自然界のB/Cではない。

### 証拠階層（独立単位と推定対象を同時に記録）

| レベル | 証拠の基準 | 現在の実例 | 上限 |
|---|---|---|---|
| U0 条件付き数理一般性 | 宣言した全有限問題族への定理/反例 | ANTO、SLK、adaptive-gain、CCOC、MLTR、MRM、CREST | 野外で頻度・効果が成立とは言えない |
| U1 系内反復 | 1種内の別個体/地点/年に再現 | Louisクイナ10個体、Tampa71 transects、hotarubukuro34地点 | 1系以上の分類学的普遍性はまだない |
| U2 分類群・地域内反復 | 種/科/地域を変えた同一プロトコル | TURNOVER 45科、FCP 4475種、ISLAND 4地域、CHOCHO 239蝶種、Batter4種 | 同じ情報源/推定法の共通偏りが残る |
| U3 外部資料で同一主張再試験 | 独立の計測・別分類群で同じ推定対象・帰無を再測定 | BITA2生物ネットワークは限定的、MINA Signy地点/種の前向き再現、FCP4種disjointは資料源が同じ | 異なる研究目的・異なる反応変数は同一効果のreplicationでない |
| U4 外部機構一般性 | 複数独立生物系で同じ識別済み因果操作・反証に合格 | **今回の52リポ横断ではまだ確認できない** | 最高誌の主張をこの水準と取り違えない |

## III. 「同じリポ群」であることと独立な科学データであることを区別する

| 横断関係 | 資料/依存関係 | 厳密な位置づけ |
|---|---|---|
| **fcp ↔ mois** | 元のiNaturalist写真・photo ID/ROI資産の一部を共有 | 種内と種間で別推定対象だが **独立データ複製ではない** |
| **fcp ↔ chun ↔ turnover** | 写真種内空間、色状態系統時間、BIEN連続形質系統時間。少なくとも解析フレーム/アウトカムは異なる。種の重なりは網羅監査なし | 概念的三角測量。「花色と一般形質で同一の記憶係数」ではない |
| **azami ↔ EAzami ↔ aza3 ↔ anto** | 同じCirsium系統群への連鎖、画像・系統・実験計画・数理それぞれ異なる | 四つの独立進化実証ではない。AZA3に同一植物由来の分子・遺伝・適応度ブリッジを集約 |
| **island ↔ izu-core ↔ shimahotarubukuro** | 全球島嶼パターン、有限ABM、伊豆の125植物個体 | 3章のdistinct estimand、モデルによるパターン因果証明なし |
| **egc ↔ egwe** | source-pinned同じEGC closure・設計拡張 | 実データによる独立再現ゼロ |
| **egc/egwe ↔ egwee** | 有限機構 vs 5独立野外研究クラスター | 外部質的一致の比較。EGWEEはSerapias除外で全体推論が変化 |
| **sch ↔ balance ↔ slk ↔ payoff** | 同一モデルオブジェクトL/R/K/Phiと文献選択枠の一部が接続 | 4つの独立実証ではなく「競合機構識別→利益→アクセス→実現」の段階 |
| **bita ↔ sch** | 両方花の生物間相互作用だが前者は採餌経路、後者は生殖適応度最適値 | 行動のルート変化だけで花形選択葛藤が証明されるわけではない |
| **rec ↔ theouni C2** | 881件fox/badger、706pass-camera otterを共用 | C2は再解析であり独立外部生物学的証拠ではない |
| **v3 ↔ rec ↔ tnoa ↔ boundary ↔ mrod** | 入口選択→記録の保持→観測同値→次観測を共有する方法論 | 別の失敗点の診断。1つの実物センサー系で全段を実証したとは言えない |
| **mrod ↔ adaptive-gain ↔ ced** | 候補観測の価値・費用・報告基準。合成問題に共通の出発点あり | 数学最適性と実測での得失を区別。C2の実データは固定armの有利な例 |
| **eog ↔ azores / louis / Tampa** | EOGベンチから同じ種/資料を起点に生物課題を分離 | 起源が同じだからEOG方法の独立な複製にはならない。独立な生物系で各別の結果 |
| **odsp ↔ batter** | ODSPでのTadarida vertical shape起源、BATTERはその後5比較パネル | 初期Tadaridaを新たな独立再現として数えない |
| **frogcs ↔ mina ↔ batter** | 原データ出所・分類群・観測法が異なる | 結果は独立だが推定対象は違う。「総量以上の組織化」の新しい共通nullが必要 |
| **chocho ↔ eog ↔ acsp** | 幼虫食草資源機会、到達可能性、調査可能域 | 全て「適地」ではない。実占有/分散を証明した組合せではない |
| **esdm ↔ rec** | カメラ測定のバイアスを扱うがMICAは基準通過イベント真値がない | 感度に関する共通疑念。ESDMの夜昼比を真の活動比と認定しない |
| **ccoc ↔ mltr ↔ mrm ↔ crest/theouni** | 未知の未来文法・受け継ぐ過去史・介入応答機構を状態の必要区別へ組み込み | 数理上の構成要素／総合設計、独立な4本の生態測定ではない |

## IV. 生物学的に非自明な「普遍性候補」を優先順位で整理

### 1位候補: 生物の組織化は総量・平均・在不在に還元できない

**根拠が実データにある複数の独立現象**:
- **FROGCS**: 雨後の鳴声量を条件づけても分類群内の多地点集中が予想以上（2,916厳格事前使用対応、null超過0.2969, p=.000999）。事象量の固定だけでは場所配置を説明しきれない。
- **MINA**: Palmer/Signyペンギン5個体群で繁殖コンポーネントの有効数が19〜83%減少、量減少時の比例縮小・有限観測誤差だけより集約が進む。
- **BATTER**: 4コウモリ分類群6追跡パネル中5比較パネルで、水平使用/中央値標高を条件付けても個体特有の垂直利用分布形が保持される。
- **LOUIS**: King Rail10個体で水深使用変化が局所可用性より小さい、プール使用対可用性傾き0.162対null1.001。移動により状態が緩衝される機構自体は未実証。
- **TAMPA**: 同じThalassia海草の出現記録が残っても量/丈/密度は変わり得る。予測警報はtransect固定効果で弱まる。

**非自明な部分**は「豊かなデータは情報が増す」という一般論でなく、各生物の真の観測単位を保存した *同じマージナルに対する条件付き再配分／持続的個体差が有意か* である。三本の既存Frog/Mina/Batterはそれぞれ既に別の条件付きnullを持つが、この3解析を集めるだけでは新しい一つの定量普遍性試験にはならない。

**新横断主仮説（未検証）:** 粗い在/総量/平均が同じでも、状態配置の条件付き残差が将来の生殖・利用・反応の予測情報を持つ。最初は分類群独立の3系を共通のnull-calibrated statisticで表し、4系目を完全未使用外部ソースから事前凍結して検定する。新原稿でこれを「普遍的に選択が維持」とは言わない。

### 2位候補: 進化的記憶の「符号の反復」と「係数の転移」は違う

- **CHUN**: fine flower-color記憶は32clades中23で分岐に対し減少方向、単一特権的な色解像度は成立しない。
- **TURNOVER**: 201 family×trait系で時系統的記憶の勾配が異質、特定の形質名で他科の強度を正しく予測する基準を満たさない。科に跨るtrait labelとは別に科の反復性が0.150。
- **EAzami**: 3頭花形質で歴史的反復回数と変化深さが違い、現生BIO15/BIO1条件は特定の歴史的起源の類似性を示さない。
- **FCP**: 50km内の空間的色彩類似は多種反復するが、fine same-month nullでは支持されない。これは時間的進化記憶の直接証明ではなく尺度を跨ぐ反例。

**最小で堅い主張:** 「ある形質で記憶がある」から「その形質の記憶量は別系統でも同じ」とは推論できない。これは自明な『文脈依存』以上に、**他科holdoutでtrait labelの予測情報を直接試した**ことが新規性の核。Ackerly (2009)等の進化率のclade差は先行知見として正確に位置づける。外部独立原データ/異なるtrait codingでの転移性能が次のゲート。

### 3位候補: 利用機会・機能葛藤の符号は、相手とアクセス経路で変わる

- **BITA**: 花に対するaccess mismatchは盗蜜比率と正関連でも、正当な採餌の落ち込みが主因となり得る。エクアドル259植物種とアフリカ57植物種の2ネットワーク。同じ効果族としての独立集団数は2に留まる。
- **SCH**: Gymnadeniaの送粉環境操作で開花開始選択傾斜の符号が変わる。ただしpure-function optimumや全探索20比較のfamilywise claimは未同定。
- **BALANCE**: 同じMimulus/Ipomopsis種についても herbivore–pollinator 対立と雄雌干渉の機能ペアが違えば、調査が同じ『flower conflict』という答えを出すとは限らない。異なる出典/異なる操作。
- **CHOCHO**: butterfly幼虫寄主の導入により239蝶種中206で資源機会が拡大、総potential region被覆+54.9%、食草専門化度相関rho .008。変化は消費者の食性幅の新進化がなくても説明できる。
- **IWE**: direct strict相利4効果のみで、反対タイプやmixedとの効果異質性の一般則は検証できていない。

**未検証主仮説:** 同一形質の効果を固定符号の「利益/コスト」でまとめると、生態相手の再分配・アクセス経路の選択・機能ペア別の方向転換を失う。標準の3因子（物理的access、相手guild、測定機能/適応度）と交差操作が必要。現在は一つの因果機構の普遍的複製とは呼べない。

### 4位候補: 表現型が失われても、未来の到達可能性まで失われたとは限らない

- **ANTO** exact marginal/pairwise but hidden triple-resource co-retention0–25%、v9歴史予測力は機能資源測定で媒介され得る。
- **EGWE** 形質0からの再発現と12世代目存在をモデル内で明瞭に分離。joint trait/allele zero は変異・移入ゼロの吸収状態。
- **IZU-CORE** 有限遅延自殖モデルでA先行はI減少の必要条件でなく、I座の資源支持喪失は将来経路を制限。384パス保有者差の2主指標はzero包含。
- **CHUN** 見える花色の過去の反復は機能的遺伝資源や古い白化順序の直接証拠ではない。
- **AZA3** 実Cirsiumで機能候補の酵素family類似2 stable、same-individual floral genotype＋floret RNA/代謝物＋introgression ancestry＋子孫適応度は未取得。
- **CREST SeedClim** soil seed bankと後の植生を結ぶ自然候補のsite metadataは12ヶ所分検証したがraw row joinはHOLD。

これは**数理・モデルとして強いが、自然界の進化的再獲得が支持されているわけではない**。その意味で「Nature Ecology & Evolutionを今提出できる最有力成果」とはしない。強い独立証拠には少なくとも2つ以上の独立植物系統での潜在分子状態＋既知の時間順序＋発現＋fitnessが必要。

### 5位候補: 分布/観測における「可能性」の地図と「実現」の地図は異なる

- **ISLAND** 自己和合性の4地域正関連と、花形・色の異なる地域反応、GloPL独立花粉制限の正勾配。歴史的原因未同定。
- **CHOCHO** 幼虫寄主資源の新たな地理的機会は実蝶生存/占有拡大でない。
- **EOG** 世界集合の予測利得はAzores/Louisiana正Tampa負、generic SDM üstün性なし。
- **STRUCTURAL** A-Islandsの強参照条件後はlog-loss加算+0.0034852（悪化）。
- **SDMR / ESDM** 本当に新分類群/地域/観測条件で得点を確認すると、より複雑な環境/活動モデルはしばしば不確定または不利。
- **REC / MOIS** 生態的構成を示す分母が写真機会/カメラ記録によって作り替えられる。人為的組成変化と生物学的真値を分ける。

「potential≠realized」は自明な理論文だけなら投稿に弱い。新規性は**いつ・どこで・どの方向に両者が離れるか**を独立holdoutで識別すること。

## V. 投稿ポートフォリオ：単独本論 vs 将来の真の新統合

| 研究稿 | 所有権・使用する実際の根拠 | 現時点の評価 | 投稿方針 |
|---|---|---|---|
| **TURNOVER-Temporal** | 201系、45植物科、12形質の真の記憶勾配＋cross-family holdout | 今回最も大きい普遍性の更新。ただし独立ソース確認未了 | GEB/進化系比較誌候補。**単独原稿先行**。CHUNを数値複製と呼ばない |
| **FCP-Within species** | 447500実測画像、1761種50km、fine-month-negative | 多種反復性強いが遺伝的局所多型の機構は不明 | New Phytologist中心、50km構造とfine-local未確定を共に書く。MOIS別 |
| **CHOCHO host resource** | 239蝶種、原寄主植物の再分布固定、206拡大、+54.9% | 広い蝶専門化スペクトルでの独立資源地理原理 | GEB本論独立、実占有は新研究 |
| **ISLAND Ch1** | 4地域SC共通＋traitwise regional response＋GloPL/H4 | 同じ島群パターンの機能的照合は支持、進化因果不明 | GEB現行ルート維持。多重性/起源未判定83.65%を開示 |
| **BITA** | EcuadorとAfrotropicalの2ネットワークでroute mismatch | 生態学的逆説の実証は魅力、独立ネットワークk=2 | Ecology Letters Letter、SCH/PAYOFF理論の合併はしない |
| **FROGCS** | NAAMP雨期干期 matched空間pulse | 複数分類群の条件付き空間組織結果 | JAE単独。MINAと新しい共同帰無を開発するなら別研究 |
| **MINA Paper1** | Palmer＋Signy2種のprospective breeding-site concentration | 外部地点/種の真正複製が比較的良好 | Ecology Report単独。Antarctic Atlasは生物成績を開けるまで別 |
| **BATTER** | 4bat taxa・6panelの中央値除去vertical profile個体反復 | 垂直方向の個体固有形という十分に具体的な現象 | JAE独立、ODSP一般枠と重複定量を回避 |
| **LOUIS** | 10King Rail + matched avail water depth、10/10 state retention | 1動物種の強い自然生態パターン | 独立動物生態稿。環境状態追跡の地理的移動因果はHOLD |
| **EAzami** | Cirsium複数頭花moduleの反復とcurrent vs origin気候非一致 | 若い放散の異なる履歴、原因の境界が重要 | JEB V10独立、AZAMIとは本文/図/独立性を分ける |
| **AZAMI** | 259 taxa広域atlas、42 taxa complete integration | 形態構成の種内/種間変化は支持 | GEB独立、画像出典/尺度感度を固定 |
| **CHUN temporal / Camellia** | 32色系統群 vs Camellia文献/分子観測 | 異なる時間記憶/分子推定対象 | Evolution LettersとAJB別稿。TURNOVERとの階層的統合は将来 |
| **EGC+EGWE** | finite mechanistic simulator＋必要状態・警告・再表現 | 自然への普遍性まだない | NEE高目標は追加外部自然証拠後。理論稿を持続、EGWEEとは別 |
| **EGWEE** | 5研究/17効果、全体p=.0121、leave-outSerapias p=.1819 | 自然多層状態の普遍分離は支持されない | Journal of Ecology候補、Serapias依存/一致するChacoを正文に |
| **SLK** | SCH/BALANCE/PAYOFF導出を持つ構造価値→進化選択ゲート | 証明の射程は大きい、実験値の一般性は未実測 | **The American Naturalist**が現行本人の投稿選択（Elより先） |
| **SDMR M5** | known-truth成功/リアル50taxa基準未達 | 「実環境同定が未達」を含む方法的貢献 | MEE方法稿として厳密に限定、positive Product Aにはしない |
| **REC+V3 / TNOA** | 入口選択野外、information theory、target-nuisance state | 他の研究を校正する共通方法・本当の分母問題 | REC+V3 Ecological Informatics M4、TNOA MEE separateで重複管理 |
| **284b** | Level A 283/288 evaluable/0 violations + invalid→zero数学 | 独立方法論と実証の二層 | 最新mainは**招待Ecology Letters M1+M2セット**投稿準備 |
| **MROD / adaptive-gain / CED / Boundary** | 新しい観測費用最適性・未識別機構・誤報資格 | 数学上の鋭い命題はあるがC2実測で常勝ではない | 各別の定理を保護。新しい生物機構が確かめられたと表現しない |
| **CCOC / MLTR / MRM / CREST / THEOUNI** | 状態の構造的必要区別、歴史/未来/機構 | 有限定理のgeneralization、野外経験則ではない | theorem provenance別本論、CREST/THEOUNIは統合/重複抑止 |
| **MOIS** | 全球写真色と雨/季節組成、条件づけ後CI跨0 | 真の花割合/気候因果ではなく観測組成の問題を残す | 実画像更新の結果確認後にGEB案を慎重再構築 |
| **TAMPA / AZORES / EOG / ACSP / ODSP** | 異なるstate・過程・capture stage | それぞれ1本ずつの生物/手法論文。共通一論文にはestimand統一が必要 | 継承せず分離、外部ホールドアウト完了が鍵 |
| **HOLD** | NEON・IWE3interaction types・TURNOVER旧spatial+interaction・PolliPi/InsePi physical・ACSP broad occupancy | HOLDはpositiveや生態的nullではない | 元の科学ロック維持。必要な新標本が来るまで投稿優先群に数えない |

## VI. 52件から新たに提案する横断論文候補（別論文の結果を使い回して水増ししない）

### 新統合α：Organization Beyond Abundance
- **中核3独立な生態系**：frogcs (鳴声の空間pulse)、mina (繁殖component集中)、batter (個体の垂直profile)。
- **補助の境界事例**：louis (環境緩衝)、Tampa (在と量の分離)、NEON (旧空間指標破綻)。NEONの無効結果をbiology-positiveと扱わない。
- **共通統計の提案**：種・個体・地域の真の反復単位で、総数/同時環境/サンプリング強度/局所履歴を保存する帰無条件下の、残差的空間・垂直・時間分布構造のexcessを測定。同一の有効標本数重みと、条件付き permutation/cross-validated proper scoreを比較する。
- **先行文献との差**：単なるaggregate ecology/island space concentrationではなく、「粗い状態が十分か」を複数分類群・観測方式で同じ帰無帰結として問う。現行3結果から新共同p-valueを作らない。
- **査読可能になる条件**：データベースから完全未使用の独立系を確保し統合仮説・統計量・境界を事前登録。まったく同じ出典では新しい独立検証にならない。
- **誌**：まず独立元稿を出す。新しい外部実証で本当に統合効果が成立したら Ecology Letters / Nature Ecology & Evolution を評価。

### 新統合β：Evolutionary Memory Is Trait × Lineage, Not a Portable Trait Constant
- **支持済み基盤**：turnover 201系/45科/12形質、chun 32色系統群、EAzami独立モジュール履歴。
- **厳密な区別**：CHUNは離散色状態記憶、TURNOVERは連続形質状態距離の系統間勾配。両者の絶対rhoは同じestimandではない。外部データのコード体系を共通化できる範囲でsign recurrence、heldout prediction gain、clade-interactionの共通階層テストを用いる。
- **既知先行**：Ackerly (2009)は同じ形質のclade間速度差を示しているので、「系統で違う」だけでは新規性にならない。新規なのはprospective leave-family-out portabilityと、trait identityを越えたclade residual information。
- **誌**：TURNOVER単独 GEB/Evolution Letters候補を先に。独立ソース/別形質の完全heldoutでpositive/negativeを確認後にβ統合を行う。

### 新統合γ：The Window Between Trait Loss and Loss of Evolvability
- **理論・モデル**：anto high-order resource + history mediation、EGWE p/q/capacity再表現、izu-core finite allele support、SLK accessibility→invasion→retention。
- **植物実証**：aza3でCirsium内の同一個体floret/head DNA/RNA/LC-MSとdated ancestry＋viable achenes。CREST SeedClimはまず元site連結を通すこと。Petuniaなど独立クレードで真正復帰の分子実証を別に登録。
- **中心因果比較**：現表現型が同じでも隠れたjoint functional inventoryが異なれば未来応答が変わるか、実測inventoryを足すと祖先史のheldout予測利得が減るか。イントログレッションと既存の有色個体移入を別categoryで報告。
- **誌**：自然での同一個体mechanism/fitnessが通るまでNEE級生態実証論文ではない。現在はANTo定理とEGWE有限モデルを優先。

### 新統合δ：When Opportunity Expands But Realized Interaction Does Not
- **大規模資源**：chocho 239蝶×寄主植物の導入地理、islandの種・SC隔離とGloPL、EOG到達世界とSDMR/Structural負の参照。
- **新しい未実測主仮説**：導入寄主が拡大した地域でも、蝶の現地占有は分散到達、気候閾値、繁殖成立の積で制限される。その制約で生態的specializationとの相互作用は変わる。
- **必要な一次data**：導入寄主の時系列、蝶の時系列（absence/detectionを別）、地域×種の前向きソース、host colonization時期を固定したbefore-afterまたは回帰不連続、観察努力帰無。現存CHOCHOの potential opportunity を占有拡大として転用しない。
- **誌**：CHOCHO GEBは単独先行。δは新しいマクロ生態因果検証があるときだけ。

## VII. 具体的な次の実作業（途中でテーマを追加しない）

1. **完了** 52現行リポ全件の直近3コミットと最新changed-filesを取得し、[52 HEAD識別子台帳](PORTFOLIO_52_LAST_COMMIT_INDEX_20261019.json)へ固定。主要変更に対して source-locked result/doc/testを確認。
2. **完了** FCP「447500 pending」→実測、「local FCP遺伝的多型支持」→5km月条件不支持、TURNOVER「全解析HOLD」→201系temporal positive programme完了、EGWEの発現/維持分離、SCH/BALANCE同種機能ペア差、C2観測適応の負の比較を訂正。
3. **次工程1** αの新しい共通nullと未使用外部生物データの事前資格審査。まず既存3生物系の生物学的単位・帰無・採択/不採択表を固定し、別の第四系をresponse-blindで選ぶ。
4. **次工程2** TURNOVER既存完成201系の投稿素材化を最優先（CHUN既発見を拡張するのでなく、記憶の「転移可能性」という別の問いで独立投稿）。
5. **later** γの遺伝/発生分子実証、δの時間付き資源/蝶分布、MOIS新350399写真の実数値検証。設計が可能でも真の測定がない段階で結論を前倒ししない。

**結論:** 52リポ横断で現在一番一般性の高い新しい経験的主張は、単なる「すべては文脈依存」ではなく、TURNOVERが真正の201系・45植物科で**trait-specific memoryの他科への予測転用を直接試した**こと、FCPが4,475種で**粗い地理的記憶と厳格局所帰無の不一致**を見せたこと、そしてFROGCS/MINA/BATTERが独立に**総量・平均へ潰れない生態的組織化**を実際の条件付きnullで示したこと。ただし3現象を合わせた単一メタ解析の支持はまだない。投稿で一番守るべき原理は「繰り返し見えた方向」「未使用分類群への転移」「同一因果機構の一般性」を別々に明示することである。
