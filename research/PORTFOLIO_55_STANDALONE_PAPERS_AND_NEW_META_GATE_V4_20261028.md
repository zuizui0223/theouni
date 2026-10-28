# 55リポ再精査 V4 — 独立論文を保護した横断研究・投稿設計

**2026-10-28 JST。V3の統合候補の一部を明示的に撤回・修正。** GitHub所有リポ56件から研究サイトを除く55件の現行main READMEを全件読み、最新HEADの凍結索引・主要最新変更ファイル・現行原稿・元結果の対象と照合。過去52リポの変更ファイル監査も参照。全ブランチ／外部原著の全データ再実行ではない。

**結論：** 「同じ概念が出てくるリポを一つのマクロ論文にする」というV3の一部判断は誤り。各研究の**中心質問・独立な応答変数・既存原稿・所有者・科学的HOLD**を先に固定し、独立論文の成果は残す。新しいマクロ・メタ解析は**新しい原ソースと、新しい共通推定対象**が存在するときだけ派生させる。

- [55件最新HEAD一覧（10/28スナップショット）](PORTFOLIO_55_HEADS_AND_ROLE_INDEX_20261028.json)
- [修正した所有権・統合禁止ルール](PORTFOLIO_55_V4_OWNERSHIP_RULES.json)
- [V3の経緯・統合案の履歴](PORTFOLIO_55_REVIEW_TO_ORIGINAL_DATA_MACRO_META_V3_20261028.md)（このV4に矛盾する統合案は廃案）
- [V2の各リポ最新変更と生態学的独立性](PORTFOLIO_52_UNIVERSALITY_COMMIT_EVIDENCE_V2_20261019.md)

## 1. FROGCSは単独の中心生態学論文。Mina/Batter/Boidsと束ねない

[現行README](https://github.com/zuizui0223/frogcs)と[正規の二部構成原稿](https://github.com/zuizui0223/frogcs/blob/main/research/manuscript/TWO_PART_MANUSCRIPT_DRAFT_2026-10-26.md)、[最新の機構比較](https://github.com/zuizui0223/frogcs/blob/main/research/manuscript/FINAL_MECHANISM_COMPARISON_2026-10-27.md)、[10/27高インパクト投稿ゲート](https://github.com/zuizui0223/frogcs/blob/main/research/manuscript/HIGH_IMPACT_SUBMISSION_GATES_2026-10-27.md)を照合した。

**主題:** 「カエルの繁殖期の強い発声の地理的配置とトンボ類・有尾類・植生の条件付き関係を明らかにし、発生段階に沿った捕食・加入過程の何がその関係を説明し得るか」。

**第1部：実際のマクロ解析。** NAAMP音響調査4,248地点、成体発声call index≥2の調査割合と、GBIFからのOdonata/Caudata **SDM適合度**、EarthEnvの周辺3 km植生。トンボ適合度と鳴声頻度の全域相関ρ −0.095（uniform）／−0.086（target-group）。池繁殖有尾類高低でOdonata–鳴声相関差 −0.385 [−0.509,−0.240]／−0.179 [−0.328,−0.029]。マクロ三者項はuniform +0.037 [+0.008,+0.068]、target-groupは+0.027 [−0.024,+0.073]。いずれも実際のヤゴ密度・幼生生残・植生隠れ場の測定ではない。[原結果の最終整理](https://github.com/zuizui0223/frogcs/blob/main/research/FROGCS_MACRO_ANALYSIS_FINAL_REPORT_2026-10-26.md)。

**第2部：数理機構の選別。** 3,600の有限構成、20候補×24の共通感度条件。相手別の植生保護・ヤゴ→有尾類・密度依存的捕食の組が条件付きの第一候補だが、同時成立は1/24条件のみ、有尾類→ヤゴ捕食は必要条件でなかった。**マクロの正の三者項を、モデルは負として出した。** 第2部は第1部を因果的に解明したとは言えない。[最終比較](https://github.com/zuizui0223/frogcs/blob/main/research/manuscript/FINAL_MECHANISM_COMPARISON_2026-10-27.md)。

**現行の論文化方針:** frogcs内でマクロ×発生段階の「1研究・二部構成」を深化する。NEEは将来の独立実証がある場合の高リスクstretch、ELも同様に実データ・観測変換のゲート次第。すでにNEE readyとは言えない。旧RC6の鳴声多地点集中は凍結済みの歴史／導入的資料であり、現行論文の別Resultとして複製扱いしない。

**V3の誤り:** 共通の「組織化は総量に還元できない」という言葉の類似だけでfrogcsをmina／batter／boidsとの新しいマクロ論文の材料にしたこと。**撤回：その統合論文案は優先課題から削除する。**

## 2. 他にも独立した主題・原稿がある。統合しない

| 独立owner | 研究の中心（同じ“空間組織化”でも応答が違う） | 現在の原結果／投稿単位 |
|---|---|---|
| [mina](https://github.com/zuizui0223/mina) | ペンギンの繁殖地コンポーネントの相対的集中と、次の南極繁殖島全域での繁殖基盤フィルター | **Paper1 Ecology Report**：Palmer/Signy5個体群、有効繁殖位置数の19–83%縮小。**Paper2**：MAPPPDから始まる南極島アトラス・マクロ。両方mina内、frogcsとは別 |
| [batter](https://github.com/zuizui0223/batter) | コウモリ個体の垂直利用確率分布の反復可能な形状 | 4分類群6追跡パネル、Tadaridaは中心化後の形状の境界例。独立JAE研究で、両生類の発声機構とプールしない |
| [boids](https://github.com/zuizui0223/boids) | 群れ移動・個体/社会群履歴・ニッチと運動予測 | 合成Boidsと別々の鳥・コウモリ現実資料。最新野生ホロホロチョウ21群/45群季節行、15反復群24未来ターゲットの**空間fidelity予測**、他群基準MSE減少+0.002648。ただし真の社会力・個体記憶は未同定 |
| [louis](https://github.com/zuizui0223/louis) | King Railが局所水深の時間変化を移動で緩衝するか | 実10鳥190対応行動・可用性事象。個体の**微環境追跡**研究 |
| [Tampa](https://github.com/zuizui0223/Tampa) | 海草の存在記録は保たれても量・サイズ・密度が悪化し得るか | **独立海草状態保持**研究、41ノード将来TNC実験計画 |
| [azores](https://github.com/zuizui0223/azores) | ウナギ捕獲時の回遊準備形質は、回遊開始と開始後の速度を同じように予測するか | 欧州ウナギの回遊開始／移動速度分離研究。louis/Tampaとは論文を統合しない |
| [Structural](https://github.com/zuizui0223/Structural) | 地理的分離の起源が違っても現状・参照モデルの後に残る景観構造の追加予測情報 | EOGから独立した原資料検証／方法論論文 |
| [neon](https://github.com/zuizui0223/neon) | 小型哺乳類の局所グリッド空間利用 | Oikos V6は**HOLD**、旧「グリッド内組織がゼロ」は幾何学的参照による可能性が高い。陽性の独立生態複製に数えない |

**明示された境界:** EOGには独立した方法論本体があり、元になったlouis/Tampa/azoresは互いに別個の生態学論文。用語や源ツールが同じことを独立性にも同一論文にも変換しない。

## 3. 花・植物でも、すでに独立の論文／章を持つ

| 現行owner | 直接支持された研究領域 | 何に統合しないか |
|---|---|---|
| [hotarubukuro](https://github.com/zuizui0223/hotarubukuro) | Campanula punctata花色の地理構造。Zenodo原画像を伴う1965観測から再生成できる専用解析 | CHUN/ANTO/ISLANDの素材論文に吸収しない |
| [island](https://github.com/zuizui0223/island) | Ch1：8,264島の地理、H1 4,379島・106,295植物種、4地域の自家和合性と隔離関連、GloPL花粉制限 | IZU-CORE Ch2やシマホタルブクロCh3と一論文化しない |
| [izu-core](https://github.com/zuizui0223/izu-core) | Ch2：自殖／花投資／有限遺伝の到達可能性と存続の理論・シミュレーション | 植物形態Ch3をCh2因果モデルの既存実証と呼ばない |
| [shimahotarubukuro](https://github.com/zuizui0223/shimahotarubukuro) | Ch3：伊豆5島125個体218花冠の形態・アロメトリー/Pst | 上二章を同一生物学的効果としてプールしない |
| [azami](https://github.com/zuizui0223/azami) | GEB V4：頭花の画像形態8連続量・BIO18との関連・ native/introduction比較 | EAzamiの系統進化結果と混ぜない |
| [EAzami](https://github.com/zuizui0223/EAzami) | JEB V10：Cirsiumの頭花向き・総苞・粘液の反復進化と起源分離 | AZAMI写真系とは別の論文 |
| [aza3](https://github.com/zuizui0223/aza3) | 独立の機構・実証プログラム。Cirsiumの花器官、実生殖、歴史、機能形質を扱う | ANTO理論から自然の形質復活・遺伝的構造を捏造しない |
| [chun](https://github.com/zuizui0223/chun) | Camellia専用Paper1＋別の多系統花色時間記憶論文 | FCPの写真空間変異と統一した「時間/空間記憶係数」を持ち越さない |
| [fcp](https://github.com/zuizui0223/fcp) | New Phytologist内種写真花色多型／地理差 447,500画像4,475種 | MOISの種間気候色論文と一つにしない |
| [mois](https://github.com/zuizui0223/mois) | 別の種間全球色構成・水分と季節の論文、真正写真取得継続 | FCPと重複する元iNaturalist写真を独立生物実測として数えない |
| [turnover](https://github.com/zuizui0223/turnover) | 一般形質の時間/空間記憶。時空間joint路はHOLD、独立BIEN時間側結果あり | CHUN/FCP実験を別cladeの検証と読み替えない |
| [anto](https://github.com/zuizui0223/anto) | 「形質が消えた後の機能的可能性」理論＋Petunieae59種の現存花芽RNA→HPLC色素予測 | 祖先的再発現や適応度の真の追跡とは違う |

これ以外にもCHOCHOは[導入寄主地理と蝶の**潜在**幼虫資源のGEB原稿](https://github.com/zuizui0223/chocho)で独立、RSDSは[GPS時間・日長・太陽相対方向の元調査マクロ](https://github.com/zuizui0223/RSDS)で独立。ISLANDの個体群HOLDと別に、CHI/DFR/ANS等の分子作用を解明する仕事はANTO/AZA3に残す。 

## 4. レビュー寄りに見える「すでに独立の仕事」と、実際に外部原研究を集める役割

| 独立の科学主題 | 原資料・現時点の状態 | 統合してよいのは何か |
|---|---|---|
| [sch](https://github.com/zuizui0223/sch) | **機能葛藤の識別**という論文が既に中心。付随する8原研究×41比較の探索的送粉操作メタでは、平均勾配の一般的弱化は支持されず（study sign p=.289）、sign reversalの確証も弱い | 同じ元studyのstage/trait/supplementationの比較条件の辞書。SCH原稿を別の新metaへ転記しない |
| [bita](https://github.com/zuizui0223/bita) | **蜜盗み比率が高くても絶対盗み率の増加とは限らない**独立Ecology Letters Letter。2独立ネットワーク | 訪花accessの定義や合法な相互作用ラベル。機能葛藤のメタ系と一研究扱いしない |
| [balance](https://github.com/zuizui0223/balance) | 持続するcompromiseとfunctional architectureの独立理論。U6=21生物groupの原著証拠抽出、独立コーダー結果は未確定 | 因子・階層・機能ペアの外部標準化辞書。文献説明を新たな実験のようにプールしない |
| [slk](https://github.com/zuizui0223/slk), [payoff](https://github.com/zuizui0223/payoff) | SLKはすでにSCH/BALANCE/PAYOFFから異なる理論オブジェクトを引き取る旗艦研究。PAYOFFは理論原導出 | 登録済みのモデル量のみ引渡す。統計的な8原研究の一部が4回再現したとは数えない |
| [iwe](https://github.com/zuizui0223/iwe) | **相互作用の季節一致による植物の実繁殖成功**が独立メタ解析の主題。厳格な数量は相利2原cluster、敵対・混合は0 | IWE主研究内で不足するクラスの元研究を補完。SCHの花形質選択係数とは異なる推定量 |
| [egwee](https://github.com/zuizui0223/egwee) | **分断化で相互作用/繁殖/移動/遺伝応答が層ごとに異なるか**という独立メタ。5原programme/17周辺効果。Serapias除外で主検定p=.012→.182 | EGWEE内の標本範囲拡張。EGC/EGWEのシミュレーターを原実証としてプールしない |
| [egc](https://github.com/zuizui0223/egc), [egwe](https://github.com/zuizui0223/egwe) | EGC有限モデルは現在EGWE一つのNEE旗艦原稿のload-bearing input。別々の同時投稿はしないと明記 | ここは**本人が明示した内部の論文統合例**。ただしEGWEEは別自然資料 |

**大切な修正:** "レビュー性の強いリポ"にも、独立した原著再解析・元実験メタ・独立方法論・抽象的数理が混在している。READMEに文献が多いことは、レビュー論文であることを意味しない。

## 5. 残りのリポも、方法・理論・未開封を区別する

- **独立方法論の所有者:** [eog](https://github.com/zuizui0223/eog)、[acsp](https://github.com/zuizui0223/acsp)、[sdmr](https://github.com/zuizui0223/sdmr)、[esdm](https://github.com/zuizui0223/esdm)、[odsp](https://github.com/zuizui0223/odsp)、[rec](https://github.com/zuizui0223/rec)、[tnoa](https://github.com/zuizui0223/tnoa)、[mrod](https://github.com/zuizui0223/mrod)、[TTF](https://github.com/zuizui0223/TTF)、[284b](https://github.com/zuizui0223/284b)、[pollipi](https://github.com/zuizui0223/pollipi)、[insepi](https://github.com/zuizui0223/insepi)。それぞれ個別の識別問題・成果・HOLDを持ち、技術が同じだけでは生態学的な複製にならない。
- **数理理論の所有者:** [ccoc](https://github.com/zuizui0223/ccoc)、[mltr](https://github.com/zuizui0223/mltr)、[ced](https://github.com/zuizui0223/ced)、[mrm](https://github.com/zuizui0223/mrm)、[crest](https://github.com/zuizui0223/crest)、[boundary](https://github.com/zuizui0223/boundary)、[v3](https://github.com/zuizui0223/v3)、[adaptive-gain](https://github.com/zuizui0223/adaptive-gain)、[theouni](https://github.com/zuizui0223/theouni)。これらはレビューの補助ではなく**自前の定理・科学方法・投稿論点を持つ別研究**。
- **開発・データ検証で独立:** [Structural](https://github.com/zuizui0223/Structural)、[neon](https://github.com/zuizui0223/neon)（SUBMISSION HOLD）、[keiba](https://github.com/zuizui0223/keiba)（競走馬行動とオッズを明示分離）。[SDEA](https://github.com/zuizui0223/SDEA) は現時点でREADME見出しのみ。ゼロを成功に数えない。

ODSPから太陽・季節原研究はRSDSへ**移管**されており、2つの別生物学的追試にはなっていない。MRODとBoundaryは方法論とPerspectiveを**意図して別論文**としている。

## 6. それでも新しい原データ論文を生み出す余地はあるか？

**ある。ただし現在の原稿を吸収する形ではない。** 新しい科学推定対象のある子研究として、次の候補を審査する。

### A. CHOCHO派生：導入食草という「潜在資源の獲得」が、本当のチョウの定着を予測する条件

- **元論文を保護:** CHOCHO/GEBの239蝶種・206種の導入食草によるpotential resource機会拡大（+54.9%）はそれ自体が独立研究。
- **新しく必要な原資料:** 個体群・地域・期間に鍵を持った外部チョウの繁殖/定着データ、寄主導入の年・実際の産卵/幼虫利用、気候・観測努力。2026蝶分布シフトの大きいレビューは**種名簿だけでは時差・原因を判定できない**。
- **新しい推定量:** Pr(観察された繁殖定着 | 寄主利用可能性・その導入時期・気候・成虫到達性)。観測されていないregionは原則missing。**CHOCHOのGEB原稿は分割・差替えしない**。
- **優先**: 真のregion×year×species記録が調達できれば、新しい外部検証として高い価値。まだ実結合ゼロ。

### B. 花の「どの繁殖段階に利益・損失が現れるか」の**新しい原論文メタ**（SCH/BALANCE/BITAを合併しない）

- **現状**：SCHの8原実験×41比較は**花形質選択勾配**であり、種子数・訪問数にそのまま換算できない。BITAはaccess/robbery、BALANCEのU6 source抽出はarchitecture coder未開封。IWEは**季節的タイミング×最終繁殖成績**の別メタ。AZA3原著Cirsiumの頭花／種子段階データも他の独立原実験。
- **新しく必要な原資料:** **同じ元生物単位**で接近→着地→柱頭花粉→受精→良好種子→翌年成体をなるべく複数段階測った、処理付き独立原実験。pre/post処理で実験単位・共分散・分母を保ち、空白を0にしない。
- **新しい推定量:** 原studyで定義できる各条件付き段階遷移の処理差、例えばΔ logit P(良好種子 | 受精済み胚珠) のように**その段階の分母が揃う場合だけ**プール。単一共通効果量へ空間尺度や指標の異なる原著を押し込まない。
- **新規性審査**: Carusoらの既存選択強度メタやPageらの訪花有効性メタとの差は、*連鎖した同一個体/花の生殖stageの実際の伝播・符号反転*を新しく定量化すること。原著の同一データを重複計数しない。
- **最初のGO/NO-GO**: **同じ段階遷移を少なくとも何独立study、処理2群＋誤差付きで抽出できるか**。現有8 SCH研究だけでは自動的に新しいstageメタにならない。

### C. ANTOの分子状態→色素予測を、真正phylogenetic holdoutで他系統へ外挿する研究

- **元論文を保護:** ANTOのPetunieae2023原実RNA/HPLC **59種**の現化学量予測は固有の分析。
- **新しく必要な実証:** Iochrominaeなどの原著に対する**同じ遺伝子群・花器官・色素量・解析単位**の再定量、実種名と原系統樹を連結したwhole-clade holdout、追加の非Solanaceae科での真正外部比較。CHUNは花色進化時間、TURNOVERは一般形質記憶で別アウトカム。
- **新推定量:** 未使用系統の化学色素量に対する予測log-score/RMSE改善。歴史的再進化可能性、遺伝子の触媒機能、祖先経路保持は**別応答**であり現59種からは推定不可。
- **GO/NO-GO:** 真の系統×遺伝子×色素の2番目以降の原sourceが揃うか。新分子因果実験がないなら新しい普遍法則には格上げしない。

### D. 方法論専用：元観測過程が異なると、「ある/ない」と数値の結論はどの程度変わるか

- REC／TNOA／SDMR／EOG／ACSPの独立論文を合併するのでなく、**共通の観測欠測・検出正しさ・holdout単位**に揃えた未使用現場データがあれば、推定の追加情報／誤り比較だけを新設。
- FCP/MOISの写真、RSDSのGPS、カメラESDM、NEON小型哺乳類を**同じ自然の「活動量」や「花色消失率」としてメタプールしない**。測定機構ごとの異なる原作用として検証する。
- 既存の方法論論文に近く、*Methods in Ecology and Evolution*が候補となるのは、真の観測原本・予測対象・外部holdoutを共通化した**新しいソフトウェアベンチマークと一般化の実証**を作った場合だけ。

### 削除する旧案：FROGCS × MINA × BATTER × BOIDSの「organization beyond abundance」論文

**V3の第III節とランキング第3位は、実行優先の横断論文としては撤回。** 4リポの対象は順に**発声・三者環境関連、ペンギン繁殖地の構成、コウモリの垂直空間分布、野生社会群の次季空間fidelity**で、共有の生態統計量も同じ生物個体の強さも存在しない。1本のメタ効果に変換する操作は定義できていない。

将来これらの独立論文をもとに普遍性比較する研究があっても、それは**論文投稿後の独立した共通推定対象・新しい原資料**で評価する二次作業。現時点では新統合テーマとして提案しない。

## 7. 優先順位と出版に関する修正

**まず既存原稿を仕上げる。** FROGCSの実測マクロ+stage機構の不一致・地域交絡を解消する作業は**frogcsが所有する**。MINAのPaper1とPaper2、BATTER独立JAE、CHOCHO独立GEB、ISLAND Ch1、AZAMI V4、EAzami JEB、FCP／MOIS、EGWEEメタ、IWEメタ、SCH独立機能葛藤、BITA独立ELをTHEOUNIで再編しない。

**新規の子研究として最初に優先判定するのはA CHOCHO定着データの時間/空間照合、次点がB花段階別の新原論文メタ適格性。** 原sourceが揃わず同一estimandを作れないなら未実施として停止。焦ってレビュー群を混ぜた「上位誌向けの大統合原稿」を作らない。

**許される横断**：
1. 他リポのモデルを、元研究の主張の境界を保ってコントロール／新しい予測として借りる。
2. 別の原生物資料を、適切な鍵と元著者の依存関係で結び新しい一次二次解析を行う。
3. 独立に保存した論文の結果を、同じ検定対象・共通帰無へ本当に変換できる場合に限り、**別の新研究として**比較する。

**禁止する横断**：
1. 「空間組織化」「記憶」「境界」という同じキーワードで複数独立論文を一原稿へ吸収。
2. 資料源が同じ実写真／生物study／シミュレーターを独立生態複製として水増し。
3. 有意な原稿の結果はポジティブだけ抽出し、別原稿の不支持・HOLDを落として普遍法則を作る。
4. 原著のレビュー件数・研究数を、実際の独立メタの処理比較数と交換する。

**結論:** 55リポを「どれが似ているか」より、「**それぞれ何を識別し、独立した論文の中心となるか**」で整理する。再利用で初めて新しい科学的に比較可能な結果ができる場合だけ、新しいマクロ・メタ研究を立てる。
