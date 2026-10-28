# 55リポ横断 V3 — レビュー／理論の蓄積を、新しい原データ・マクロ解析／メタ解析へ変える

**監査日:** 2026-10-28 JST
**全数:** GitHubのowner一覧に現在56リポ。研究ホームページ zuizui0223.github.io を除く55リポの各最新コミットを確認。最重要の直近変更について、changed files、解析済み原データ・結果JSON、実証・出版境界を個別読了。既存52リポ全件の直近3コミット監査V2を研究史・データ重複の基準とした。
**最新HEADと主たる役割:** [55リポ一覧](PORTFOLIO_55_HEADS_AND_ROLE_INDEX_20261028.json)。これは2026-10-28に観測したスナップショット。各リポの全ブランチを実行・最新原データを再解析したという意味ではない。
**V2:** [52リポの原実証／理論・データ依存監査](PORTFOLIO_52_UNIVERSALITY_COMMIT_EVIDENCE_V2_20261019.md)。
**ユーザー意図:** 文献を寄せ集めたレビューを追加するのでなく、レビューで発見した機能ペア・生態機構・未識別部分を使い、定量的な原データ研究を新しく設計する。

## 結論：新しい生物学的推定対象は少なくとも五つある

1. **段階の違う繁殖機能は、いつ同じ形質に異なる選択をかけるか。** SCH × BALANCE × BITA × AZA3 × IWE。メタ解析の第一候補。
2. **導入された相互作用資源は、potentialな生息可能域をどれだけactualな分布拡大に変えるか。** CHOCHO × IWE × ACSP × ISLAND と2026外部チョウ再分布記録。新規外部結合型マクロ解析。
3. **生物の組織化は、総量や平均が同じでも条件付きに予測情報を持つか。** FROGCS × MINA × BATTER × BOIDS。共通帰無と未来ホールドアウトが必要。
4. **花色の分子機能は、表現型分類や祖先史より未知の系統の色素化学量を予測するか。** ANTO × CHUN × TURNOVER × FCP × AZA3。Petunieae実59種が新しい大きな足掛かり。
5. **日長・太陽位置に対する時間ニッチと方向ニッチは異なる空間・時間尺度で分離するか。** RSDS × BOIDS × BATTER × ESDM。元GPSの機器・UTC cadenceを固定する。

上記を**一つの巨大論文にまとめない**。異なる生物学的推定対象に共通語を貼るだけの「理論的統一」では学術的な独立実証にならない。独立論文／データプロジェクトの母艦は各元リポ、THEOUNIには横断登録・参照・審査基準のみ残す。

## I. レビューやアイデア性の強いリポを、どう実証へ変換するか

| 主リポ | 現在の元根拠と分母 | すぐに言えないこと | 統合研究での価値 |
|---|---|---|---|
| **sch** | **8独立原研究・41処理×形質**の実数値パイロット。6/8で平均の絶対選択勾配弱化方向、正確なsign p=0.289。16/41点推定は符号反転するが**40 SE付き比較のfamilywise変化証明0**。共通花数軸5研究の保守的推定+0.0619、区間[−0.0221,+0.1459]。 | 一般的に送粉によって選択の符号が変わる、共通の進化的効果量を推定した、など。 | **メタ解析の実数値・独立study ID・機能別処理比較の母艦**。[最新研究](https://github.com/zuizui0223/sch/blob/main/docs/SCH_EIGHT_PROGRAMME_EXPERIMENTAL_POLLEN_META_PILOT_V1.md) |
| **balance** | U6は**21植物の原出典依存group**、予測前固定ルールに基づく6植物の生態原論文情報を抽出。見つけた機構は送粉者と花粉盗取者のaccess差、雄雌ステージ・花粉提示タイミングなど。独立構造コーダーの正規結果は未開封。 | 21個の機能分業進化を検証した、分業の頻度を推定した、など。 | **介入の時間順序・機能ペア・相互作用相手の厳格コード辞書**。[U6](https://github.com/zuizui0223/balance/blob/main/docs/BALANCE_U6_SIX_ORIGINAL_SOURCE_ECOLOGY_EXTRACTION_V1.md) |
| **iwe** | STRICT-H1で正方向の**4実数値行すべて相利相互作用**。SMDに関する独立clusterは相利2、拮抗0、混合送粉者＋種子捕食者0。 | 相利／拮抗／混合のメタ平均の違い。 | **季節的相互作用windowを真の可用性・繁殖適応度に連結するsource gate**。未取得の混合・拮抗の文献原数値を先に取得。[IWE](https://github.com/zuizui0223/iwe) |
| **slk, payoff** | 葛藤・分業利得・構造費用・選択／侵入の条件付き数理。 | 花の機能葛藤の頻度、実進化の実証。 | 生物学的帰無・反対仮説、測定すべき異なる共分散と費用の定義。**別独立な実証studyとしてカウントしない**。 |
| **egwee, egwe, egc** | published biological cases の整理と、同じピン留めEGC再現・有限遺伝／生態モデル。最新EGWEは高形質bin潜在成長と対立遺伝子選択の境界を区別（例：モデル q_grid=0.5991975 と q_allele=0.625）。 | 同じ遺伝子系の別原生物実証、自然界の回復率。 | 発現・潜在的生育能力・対立遺伝子の増減・継続の**別エンドポイント**を作る。 |
| **azami, EAzami, aza3** | AZAMIは公開画像の同時形質と生態文献。EAzamiは属内形態の系統史。AZA3は**実C. arvense 615頭花／36原4処理ブロック**、**実C. undulatum 105母植物の頂端／側枝共同成功**、実Ryukyu若葉RNA6ランを別途保有。 | 形態相関だけで送粉・防御利益と遺伝的LEGOの進化を確証すること。 | 段階別繁殖機能、器官position、実生殖アウトカムの原データ担当。原データ間には共通plant IDがない。 |
| **theouni, ccoc, mrm, mltr, ced, boundary, mrod, adaptive-gain** | 情報十分性、観測・未来・過去・機構・結論のゲート／計算定理が中心。 | これらの本数を生物学的独立再現数と数えること。 | メタデータ・観測過程・根拠の適格性・データをプールしてよい条件を厳格化する。 |

**元のレビューから新研究へ進めるための規律：** 文献の存在 → 調査対象と推定対象の適格化 → 元数値・独立実験単位・比較対照の取得 → harmonized outcomeと依存性調整 → 未使用地域／分類群へ予測 → 機構別の外部追試。レビュー数や引用数を「生物学的サンプル数」に転換してはいけない。

## II. 第一候補 — 繁殖成功を「連続した機能段階」で分解する実験メタ解析

**仮タイトル**: *Where do ecological partners change reproductive fitness? A stage-resolved synthesis across flowering plants.*

**問い**: 同じ花の構造／色／向き／開花時期が、外部の送粉者・花粉盗取者・種子食者・降雨に出会ったとき、どの段階のconditional successを増減させるか。平均来訪数が増えても、実際の受粉、胚発生、充実種子、子孫へ利益が伝わるとは限らない。相手の種類と順序・操作によって同じtraitの利益の符号が変わる可能性を直接試す。

**現有の研究系と限界**:
- SCH：8独立研究、41比較。見かけの選択勾配符号反転は多数でも確証は僅少。40 SE付き比較でBonferroni後の方向変化証拠なし。
- BALANCE U6：21group中6群の原論文生態記述のみ、独立A/B coder結果は開封前。構造分業の効果は未同定。
- IWE：4 strict effectはmutualistだけ。negative/seed-predator mixedとの3-class interaction metaは推定不可。
- BITA：原ネットワークの盗蜜比率上昇は、真の盗蜜絶対増加でなく正当採餌の低下でも作られる。訪問**比率**と受粉**機能**を区別。
- AZA3：C. arvense 615頭花・36整合blockで送粉者袋掛け−対照の良好種子/頭花差−41.59、分解上の良好種子率項−41.25、小花数項−0.33。重要だが、授粉・食害・袋内微気象のどの因果経路が差を作ったか不明。
- ISLAND GloPL：2,969花粉補充実験・919文献と性質の別層。SCHと原論文単位で重なる可能性があるため、**研究IDと実験DOIで重複除去**してから使う。GloPLの平均花粉制限とSCHの花形質選択勾配は同じ効果量ではない。

**新しい共通統計量**: 一つの観測段階について
  Δ_logit,k = logit Pr(stage k succeeds | stage k−1 reached, treatment)
              − logit Pr(stage k succeeds | stage k−1 reached, control).
ただし個体段階データがない文献は、分母と対象が異なるので同じΔへ強制変換しない。別の階層モデル（選択勾配変化、段階成功率、充実種子数）を作り、**study/experiment/plant/taxonごとの依存性**を保持する。

**最低限の原論文行スキーマ**: study DOI, experiment_id, species, population, site-year, experimental arm, partner guild, functional trait, stage identifier, numerator, eligible denominator, signed effect/SE, covariance availability, organ pre/post-treatment, source figures/table, study-wide inclusion rule。口吻長・鳥・ハチ等の群名だけで受粉有効性を機械的に符号化しない。

**ゼロ／反証**: 送粉者操作後も進行段階に一貫した差がない、環境やstageを条件付けると符号変化が消える、原論文の測定不十分で全機能共通推定量が作れない。後者はNOT_IDENTIFIABLEであり効果ゼロではない。

**先行研究の強い壁**: Caruso et al. (2019), Evolution DOI 10.1111/evo.13639はすでに多くの原研究に対するpollinator選択の強さとtrait/guild別異質性をメタ解析した。単なる「送粉者の種類で選択が違う」では新規性がない。**操作した相互作用がどの繁殖移行段階に作用し、別の機能に損失を移すか**が今回の生物学的な新規方向。

**投稿境界**: 原数値を幅広く確保し、独立studyと元データ対照が揃い、結果の新しい生態機構を証明した場合 Ecology Letters / New Phytologistを検討。現状はpilotメタ解析でありsubmission-readyではない。

## III. 第二候補 — チョウの寄主資源の拡張は、実際の地理的定着を予測するか

**仮タイトル**: *When do introduced host plants become realised butterfly range expansions?*

**母体CHOCHOの実測ではない推定対象**: 239種の既知幼虫寄主を固定したとき、導入寄主地理により206/239種の潜在的資源機会が広がり、aggregate coverage +54.9%。FAO作物寄主除外でも約+46–47%、食性幅勾配ρ≈0.008でほぼゼロ。ただし**蝶の実在分布拡大・産卵成功は直接観測していない**。

**新しい外部資料**: 2026年8月のNature Ecology & Evolution論文（DOI 10.1038/s41559-026-03117-y）は、567文献＋専門家評価に基づく1,758蝶種の再分布記録を編集し、Supplementary Information section 3に対象種名簿を公開した。しかし掲載内容は**reported shift**であって、元蝶の同一粒度の個体群統計・地域別移動時刻・寄主利用の観察ではない。種名簿とCHOCHO239種の実際の重複・国/地域・year-grain・導入寄主の到着時刻は**今回まだ計数していない**。

**新しい仮説**: 既知寄主のgeographic opportunity gainは、気候適合・成虫分散・観測努力が同程度な地域では、報告されるrange expansionsよりも**潜在資源への侵入成功の時差**を説明する。ただし「報告された拡大の多くは気候関連」という既知2026報告を上書きせず、気候と寄主の交互作用を事前指定する。

**最初の実務ゲート**: ①種名とtaxon conceptを厳格対応、②外部記録の方向・country/cell・報告期間を確認、③同じ粒度へCHOCHO WGSRPD3-region hostsを集約可能か検定、④国際的なsurvey/GBIF effortで非報告をabsenceにしない、⑤原宿主の導入時期が蝶の新しい記録より前か検証。時期がない場合は真の因果ラグ研究を停止し、断面予測のみへ格下げする。

**強い先行・独立性の注意**: 2026年の上記NEE論文はすでにglobal butterfly shiftを扱う。新規性は**植食者の資源供給（実際の導入寄主の可用性）と現実の侵入成績を独立データで結び付ける点**であり、もう一つの気候変動レビューではない。同じGBIF記録を両研究で使えば真の独立source validationではない。CHOCHOの既存GEB稿を上書きせず、**別の検証パッケージ**として設計する。

**投稿境界**: species×region×periodの真の独立exposure/outcomeが揃えば GEB、強い時間順序と対照があれば Ecology Letters、単なる種間重複のみなら独立投稿不可。

## IV. 第三候補 — 総量を固定しても空間的な組織化は残るか

**仮タイトル**: *Organisation beyond abundance across animal systems.*

| 互いに別の原データ源 | 今の実証と真の単位 | 比較できない部分 |
|---|---|---|
| FROGCS | NAAMP等の鳴声原記録：マッチした雨／乾燥調査4,236組では活動の多地点集中が単純総量変化だけでは説明しきれない。別新マクロで**4,248調査地点**のOdonata/Caudata適地×呼び声が調べられ、3-way項の観測とモデルで符号不一致。 | 鳴声検出・個体数・幼生個体群の配置を同じものとは呼べない。 |
| MINA | ペンギンの5繁殖個体群で有効繁殖パッチの縮小が19–83%。個体数減少比だけでは再現しにくい。 | 1コロニー内のパッチ＝個体数との混同、衛星観測誤差、同じ南極生物群に偏る。 |
| BATTER | コウモリ縦分布の個体特有形状が水平空間利用/中央値高度調整後も残る比較パネル。 | 鳴声の同調や繁殖位置ではなく個体の垂直利用分布。ODSP起源のTadaridaを独立複製と呼ばない。 |
| BOIDS | **新しい原著由来野生ホロホロチョウ21社会群、15反復群、未来24group-season**。過去の自己群空間fidelityを使う固定縮小予測は、他群履歴基準からgroup-equal MSE+0.002648改善、whole-group bootstrap CI[+0.000618,+0.004493]、11/15符号検定p=0.0592。一方、面積と速度では支持不足。 | 履歴が有効でも群れの協調力・個体の神経記憶・Boids力を直接測っていない。原GPSは使えず著者集約表の予測。 |
| LOUIS / TAMPA / NEON | 現場状態の保持、植生出現と密度の違い、NEON abundance saturating 16/16 siteの負対照。 | 主分析の4システムが成功することを前提に選ばず、非改善対照を残す。 |

**共通推定量の案**: 元の生物学的単位ごとに (i) abundance/count/occupancy/effortを保存する再割当nullで計算した標準化されたconditional organisation excessと、(ii) その組織指標が**未使用の次時点の空間利用／繁殖状態**を予測するlog score改善。分類群・ソース内相関でclusterし、異なるnullを同じ確率モデルへ無理にプールしない。

**致命的条件**: 時間軸・観測カーネル・真の使用空間を統一できず同じ再配列操作が合法でない場合、メタ平均を計算せず独立結果の比較とholdout診断に留める。最初の三本は現在の推定量が異なるので「既存3リポから普遍性支持」はまだ誤り。

**投稿境界**: 第4完全holdout、測定観測の負対照と共通推定量が通れば Ecology Letters / GEB。記述的な異なる生態パターンを並べただけでは格上げしない。

## V. 第四候補 — 潜在的な分子機能は、花色の「過去」より将来の化学状態を予測するか

**新しい実データの前進**: ANTOは2026-10-28にWheeler et al. 2023（DOI 10.1098/rspb.2023.0275）の**原著公開花芽RNA発現×HPLC色素量の59 Petunieae種**を、指定5原ファイルのMD5/SHA256一致確認後、種ごとの真のleave-one-species-out ridgeモデルで再解析。

| Original 59 Petunieae species, heldout model | Anthocyanidins RMSE | Flavonols RMSE |
|---|---:|---:|
| Training mean only | 0.390797 | 1.377145 |
| CHI only | 0.396685 | 1.369020 |
| Pathway branch: F3'H / F3'5'H / FLS | **0.329612** | **1.186676** |
| Preselected six-gene panel | **0.326321** | **1.162451** |

先行Iochrominae 2019原著の「CHIが最良というin-sample AIC」と、別Petunieaeの未知種予測で「分岐3遺伝子の良いスコア」は**直接の矛盾・再現失敗ではない**。母集団・測定・目的・統計モデルが異なる。ITO原著2019の元RAR配列はDryad401/403で未取得。Petunieae原著種コードの先頭2字を丸ごと除くテストは**真の系統クレードleave-one-outではない**。両者は同じナス科であり、ANGIOSPERM-wide独立検証を完了したとは言えない。

**次の新規マクロ解析**: 同じ予測目標（対数花器官化学色素、アントシアニンとフラボノールは分離）、同じ6候補分子状態・真正phylogenetic whole-clade holdoutをIochrominae／Petunieae／別の科に適用。さらに祖先色復帰や遺伝資源破壊は**別の縦断エンドポイント**であることを守る。

CHUNは花色系統史32クレード、TURNOVERはBIEN系統記憶201 family×trait system /45科で、trait名だけから別科への記憶の強度持ち越しが改善しなかった。FCPは4,475種の**写真**色軸・空間差であって真の分子色素・遺伝的多型頻度ではない。AZA3の琉球6ランは若葉RNA候補断片であり、花器官調節子と化学経路の真の同時測定はない。

**普遍性の反証対象**: 「同じ生化学的traitを持つ系統でも、必要な分子予測状態は別の系統へ転移しない／転移する」。この問いなら、いつのまにか祖先色が再進化したと誤記することなく、実測原表から推定可能。

**投稿境界**: 真の系統外holdout、複数科の同定された花芽RNA/HPLC共通パネルと検定前固定の枝方向が通るまで、現時点は**単一Petunieae source内予測結果**。New Phytologist / Evolution Lettersの主張は将来条件付き。

## VI. 第五候補 — 時間ニッチと方向ニッチの分離のマクロ生態学

**実証済みの入口**: RSDSは8元Movebank研究・12 study×taxon行、同じ原タグと天文日をそろえるUTC cadence三系列で8群が比較可能、観測NIGHT−DAY GPS変位差の符号が全系列で一致したのは5/8、q~日長係数の正の符号まで支持2/8。元GPSの偶奇観測時刻・補助ERA5の物理値取得版に強い観測条件差があり、48原研究の日射負方向効果の外部再現は**FAIL/HOLD**のまま。太陽コンパスの利用や真の活動ニッチの因果作用はまだ不明。

**追加の独立文脈**: BOIDS野生Guineafowlは社会群の次季空間fidelity、BATTERは哺乳類個体の縦利用分布、ESDMはカメラによる相対夜昼検出。**GPS速度・ヘッド方位・縦位置・カメラ検出比は別の測定変数**なので、これらの係数をそのままメタ平均しない。

**本当に新しい推定対象**: 同一animal/studyを内側に固定した**時間ニッチ**（観測区間長・GPS cadence条件付けた昼夜変位）と**方向ニッチ**（同時点の移動方位から太陽方位を引いた円統計量）を分離し、研究ホールドアウトで同じ環境因子の予測符号の転移性をテスト。よりよい空間・時間観測カーネルがある原調査を未使用外部群として凍結する。群のごとの正負混在こそ事前予測対象であって、無理に一方向を押し付けない。

**投稿境界**: JAE/GEBへ向けた新しいsource-matched macroecology。現在は源GPS観測過程・共通ソース数・地域構成の制約が強く、論文の普遍的な太陽方位効果を支持しない。

## VII. 追加の後続テーマ（今は主線から分離）

### ISLAND × IZU-CORE × SHIMAHOTARUBUKURO — 島の機能的なコロナイズ制約

ISLAND現主論文には8,264島解析母集団、4,379 H1島、106,295植物種、GloPL 2,969補充実験/919文献の独立層。自家和合性と隔離の正関連は4地域で比較的安定だが、他の花形質は地域差が大きい。既存原稿のH1–H4と同じGloPL/trait/geographyを再利用して「別の新規性」と主張すると**二重論文化**になる。

Prior art: 2024-11公開のZell et al. *New Phytologist* DOI 10.1111/nph.20234 は3,222種/169科を用いて島への進出で交配様式・寿命・花対称性・到達機会の交互作用を実証済み。またBurns et al. 2019 DOI 10.1111/nph.15935 は2,000以上の植物集団の侵入形質×花粉制限をメタ解析済み。**「島＝自殖が多い」とする新規テーマは論文として不足**。将来独立原データを導入し、例えば地域で利用できる送粉チャネルの喪失によって**どの器官・どの reproductive stage が選択されたか**を特定する場合にのみ新しい単位とする。

### 観測過程に由来する生態学的符号反転：MEE 方法論候補

FCP（原花色写真447,500／4,475種、photo ROI推定）, MOIS（2026-10-25時点1,019,272真正画像試行、449,741自動4色分類、未分類が大きい）, RSDS（同じGPS元タグでも記録UTC位相でQ方向が変わり得る）, ESDM（カメラ条件による相対夜昼比）, REC・284b・SDMR・ACSP・EOGなど。

ここに**観測選抜は生態推論を反転し得る**という再現性の高い共通問題はある。しかし、I-Nat写真の白さ、移動速度、カメラ夜昼検出、NEON在不在は、同じ生態効果量ではない。「X研究中Y研究で符号反転」と無条件にプールするのは無効。特定のunbiased same-site/same-individual sourceと、観測機構の事前固定による差を共通なログスコア・bias診断として作れるなら、*Methods in Ecology and Evolution*の方法論比較へ。自然の機構の新発見と混同しない。

## VIII. 55リポの所属整理（主たる研究機能の一例）

**花・形質・進化軸（16）：** hotarubukuro、azami、island、izu-core、shimahotarubukuro、fcp、mois、chun、EAzami、aza3、anto、turnover、egc、egwe、egwee、crest。

**相互作用・繁殖選択・資源供給（7）：** bita、balance、sch、payoff、slk、iwe、chocho。

**動物の空間・時間・組織化（9）：** frogcs、batter、mina、Tampa、louis、boids、RSDS、odsp、azores。

**観測過程・生態推定方法（11）：** acsp、eog、esdm、sdmr、284b、rec、neon、TTF、tnoa、pollipi、insepi。

**条件付き理論・科学統合基盤（11）：** mrod、ccoc、mltr、ced、mrm、boundary、v3、adaptive-gain、Structural、theouni、SDEA。SDEAは現時点**initial commit/README見出しのみ**で、既存実証や解析にカウントしない。

**補助的な社会・意思決定系（1）：** keiba。馬の実データと投票者モデルを生態モデルに類比できるが、競馬のオッズと野外送粉・島嶼系は共通生態実証ではない。主な生態メタの独立系に数えない。

**この分類は論文タイトルではなく、新しい研究へ原データ・方法論を移せる主役割である。** 55リポの間には実写真・同じシミュレータ・同じ原論文・同じ分類群の重複が多い。

## IX. データ独立性と報告・投稿のルール

| 資料接続 | 実際の関係 | 統合するときの禁止事項 |
|---|---|---|
| FCP / MOIS | 元iNaturalist写真・photo ID・ROIが広く共通 | 二つの独立な花色データ群としてメタ計算しない。MOIS百万画像試行は百万の花色実測・野生植物確証ではない |
| ANTO / EGWE / EGC | 理論モデル群。EGWEはEGCシミュレータsource-pinned | 二つの独立した野生植物再進化テストとして扱わない |
| ANTO / AZA3 / AZAMI / EAzami | 同じCirsiumや花形質の理論と実データ | 若葉RNAを機能的花色保持・祖先的復帰の証明にしない |
| SCH / BALANCE / PAYOFF / SLK | 原文献と機能ペアを共有する場合がある | 行や比較軸を独立studyとして水増ししない |
| ISLAND / SCH / 外部GloPL | 多数の同一原論文の花粉補充 | 同じ実験を異なるリポの独立複製として二重計上しない |
| FROGCS内部 | 旧frog acoustic RC6 vs新4,248-siteマクロは同じリポでも目標・データ生成が異なる | 旧多数地点集中を新Odonata×Caudata機構の独立再現と呼ばない。Macro 3-wayとsimulation 3-wayは符号不一致 |
| ODSP / RSDS | 太陽・季節・方向の研究はRSDSへ移転。現在のODSPは観測設計的方法など | 履歴移管を新生態実証として数えない |
| REC / THEOUNI C2; ODSP / BATTER; EOG / LOUIS・TAMPA | 元ソースの一部に親子関係あり | 元研究を合併後に複数独立な外部再現へ格上げしない |
| CHOCHO / 2026 NEE蝶range shifts | 現状**別々の原出典で、species×period×region join未実施** | 文献で報告されたrange shiftがCHOCHOのintroduced hostで生じたと先に仮定しない |

**普遍性レベル**をU0条件付き理論、U1系内反復、U2分類群内/多地域、U3完全独立外部データ・同一推定量、U4異分類群での同じ因果機構検証と区別。現行の55リポ横断では**U4一般則を裏付ける実証の組は確認されていない**。

## X. 今、本当に手を動かす優先順

**主線1 — 花の繁殖ステージ・メタ解析：** SCHの8study×41比較は新しい原数値パイロットとして固定、BALANCE独立コーダーを開く前にS1–S5のstage定義と欠測を凍結。新原論文で段階successの分母と群別効果が取得できる研究を事前登録して追加する。最初のgo/no-goは**「現有研究で同じstage間transitionの同じ効果量を何研究取り出せるか」**であり、必ずしも陽性結果を探さない。

**主線2 — CHOCHOの実際の蝶分布：** 公開NEE2026Supplementary対象種名簿と239既知種の**taxon concept重複率**を初めて計算する。重複が存在しても、region/yearの元記録と原host導入時期が揃わなければ因果実証の枠を作らない。初期analysisは再分布文献への対象選択確率の計測。

**主線3 — 空間組織化の共通帰無：** FROGCS・MINA・BATTER・BOIDSの「合法な交換可能単位」「保存すべき観測努力・総量」「未来予測可能なアウトカム」を一つのmanifestに列挙。完全別ソースの検証前には横断効果量・普遍法則を公表しない。

**later:** ANTOの59種化学量を真正系統holdoutへ、RSDSの8元GPSのsource-cadence対照へ、ISLAND新H5を元Chapter1と非重複な実証へ、観測method統合MEEへ進める。

## 参照した主な元リポ・文献

- SCH実数値8研究：[元表と不支持のメタパイロット](https://github.com/zuizui0223/sch/blob/main/docs/SCH_EIGHT_PROGRAMME_EXPERIMENTAL_POLLEN_META_PILOT_V1.md)
- BALANCE独立pilot：[U6原出典群](https://github.com/zuizui0223/balance/blob/main/docs/BALANCE_U6_SIX_ORIGINAL_SOURCE_ECOLOGY_EXTRACTION_V1.md)
- IWE：[strict-H1 origin grain, missing mixed/antagonist](https://github.com/zuizui0223/iwe)
- AZA3：[C. arvense 615頭花のステージ分解](https://github.com/zuizui0223/aza3/blob/main/docs/CIRSIUM_ARVENSE_ORIGINAL_HEAD_FLORET_VS_SEED_CONVERSION_20261023.md)
- ISLAND：[current corrected main study](https://github.com/zuizui0223/island)
- CHOCHO：[239 butterfly/host source opportunity](https://github.com/zuizui0223/chocho)
- 外部蝶range shifts：[Nature Ecology & Evolution, 2026, 1,758 species](https://doi.org/10.1038/s41559-026-03117-y)
- ANTO 59実種：[Petunieae原OSF色素・発現の真のholdout](https://github.com/zuizui0223/anto/blob/main/docs/PETUNIEAE_2023_ORIGINAL_SOURCE_AND_PREDICTION_GATE_V26.md)
- TURNOVER：[201 trait×family systems](https://github.com/zuizui0223/turnover/blob/main/docs/TRAIT_MEMORY_CONTEXT_SYNTHESIS_V0_1.md)
- BOIDS：[wild guineafowl 15 social groups future fidelity](https://github.com/zuizui0223/boids/blob/main/docs/V20_OBSERVED_WILD_GROUP_FIDELITY_RESULT.md)
- RSDS：[eight-study GPS temporal/solar macro source](https://github.com/zuizui0223/RSDS)
- FROGCS：[new macro versus mechanistic sign mismatch evidence gate](https://github.com/zuizui0223/frogcs/blob/main/research/manuscript/HIGH_IMPACT_SUBMISSION_GATES_2026-10-27.md)
- Caruso et al. (2019) Evolution, experimental floral selection meta DOI 10.1111/evo.13639
- Zell et al. (2025 issue, Nov 2024 online) New Phytologist, island colonization DOI 10.1111/nph.20234
- Burns et al. (2019) New Phytologist, invasive/native pollen limitation meta DOI 10.1111/nph.15935

**このV3は研究・出版設計と元の結果の証拠監査。新しいメタ推定値、独立cross-taxon pooled効果、一般則の機構実験を今回の文章で新たに実行したと主張しない。**
