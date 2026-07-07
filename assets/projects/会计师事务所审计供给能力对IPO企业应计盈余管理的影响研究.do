clear all
set more off
set linesize 240
cap mkdir results

*------------------------------------------------------------------*
* 会计师事务所审计供给方能力对 IPO 企业应计盈余管理的影响
* 核心解释变量 审计师行业专长 AuditSpec 事务所规模调节 Big4
* 被解释变量 应计盈余管理绝对值 AbsDA 修正 Jones 模型
* 样本 2011-2024 A 股 IPO 公司
*------------------------------------------------------------------*

*==================================================================*
* 1 数据构建 在 master 控制变量表上逐表 merge
*==================================================================*
use "data/raw_controls.dta", clear
capture drop 丘知数据分析会员之家
destring stkcd, replace force
gen int year_i = year
drop year
rename year_i year
keep stkcd year 行业代码 Size Lev ROA Growth Top1 Board Big4 Opinion AuditFee SOE Industry
duplicates drop stkcd year, force
tempfile ctrl
save `ctrl'

* 被解释变量 应计盈余管理 AbsDA
use "data/raw_absda.dta", clear
rename 证券代码 stkcd
rename 年份 year
destring stkcd, replace force
keep stkcd year DA AbsDA
duplicates drop stkcd year, force
tempfile da
save `da'

* 核心解释变量 审计师行业专长
use "data/raw_auditspec.dta", clear
capture drop 丘知数据分析会员之家
destring stkcd, replace force
gen int year_i = year
drop year
rename year_i year
keep stkcd year 审计师行业专长
rename 审计师行业专长 AuditSpec
duplicates drop stkcd year, force
tempfile spec
save `spec'

* 以控制变量表为主表合并
use `ctrl', clear
merge 1:1 stkcd year using `da', keep(master match) nogen
merge 1:1 stkcd year using `spec', keep(master match) nogen

* 仅保留 2011-2024 年间 IPO 的公司样本
merge m:1 stkcd using "data/raw_ipo_list.dta", keep(match) nogen
keep if year>=2011 & year<=2024

*==================================================================*
* 2 变量处理
*==================================================================*
* 缩尾 缓解极端值 替换式不删观测
winsor2 AbsDA AuditSpec AuditFee, cuts(1 99) replace

label var AbsDA     "应计盈余管理"
label var AuditSpec "审计师行业专长"
label var Big4      "事务所规模(国际四大)"
label var Size      "公司规模"
label var Lev       "资产负债率"
label var ROA       "盈利能力"
label var Growth    "营收增长率"
label var Top1      "第一大股东持股"
label var Board     "董事会规模"

* 非标准审计意见 Opinion==0 为非标
gen ModOpinion = (Opinion==0) if !missing(Opinion)
label var ModOpinion "非标准审计意见"

* 交互项 调节效应
gen SpecBig4 = AuditSpec*Big4
label var SpecBig4 "审计师行业专长×事务所规模"

* 行业与年度固定效应标识
encode 行业代码, gen(ind_id)

* 控制变量集合
global X AuditSpec
global Controls Size Lev ROA Growth Top1 Board

*==================================================================*
* 3 统一分析样本 保证全文 N 一致
*==================================================================*
mark touse
markout touse AbsDA AuditSpec Big4 SpecBig4 $Controls ind_id year
keep if touse==1
count
global N = r(N)
di "最终分析样本量 N = $N"

*==================================================================*
* 4 描述性统计
*==================================================================*
estpost summarize AbsDA AuditSpec Big4 $Controls, detail
esttab using "results/t1_desc.rtf", replace ///
    cells("mean(fmt(4)) sd(fmt(4)) min(fmt(4)) p50(fmt(4)) max(fmt(4)) count(fmt(0))") ///
    label nonumber noobs title("表1 描述性统计")
esttab using "results/t1_desc.csv", replace ///
    cells("mean(fmt(4)) sd(fmt(4)) min(fmt(4)) p50(fmt(4)) max(fmt(4)) count(fmt(0))") ///
    label nonumber noobs plain

*==================================================================*
* 5 相关系数矩阵 带显著性
*==================================================================*
estpost correlate AbsDA AuditSpec Big4 $Controls, matrix listwise
esttab using "results/t2_corr.rtf", replace unstack not noobs compress ///
    b(%9.3f) star(* 0.1 ** 0.05 *** 0.01) title("表2 相关系数矩阵")
esttab using "results/t2_corr.csv", replace unstack not noobs plain b(%9.3f) star(* 0.1 ** 0.05 *** 0.01)
pwcorr AbsDA AuditSpec Big4 $Controls, star(0.05)

*==================================================================*
* 6 多重共线性 VIF
*==================================================================*
regress AbsDA AuditSpec Big4 $Controls
estat vif

*==================================================================*
* 6b Hausman 检验 固定效应与随机效应选择
*==================================================================*
xtset stkcd year
qui xtreg AbsDA AuditSpec $Controls i.year, fe
estimates store FE
qui xtreg AbsDA AuditSpec $Controls i.year, re
estimates store RE
hausman FE RE, sigmamore

*==================================================================*
* 7 基准回归 逐步加入
*==================================================================*
eststo clear
* 行业专长为行业相对份额度量 主回归用年度固定效应加公司层面控制
* 行业固定效应会机械吸收行业份额变量 故双向固定效应列作稳健性
eststo m1: reghdfe AbsDA AuditSpec, noabsorb vce(cluster stkcd)
eststo m2: reghdfe AbsDA AuditSpec $Controls, noabsorb vce(cluster stkcd)
eststo m3: reghdfe AbsDA AuditSpec $Controls, absorb(year) vce(cluster stkcd) keepsingletons
eststo m4: reghdfe AbsDA AuditSpec $Controls, absorb(ind_id year) vce(cluster stkcd) keepsingletons
di "基准 主模型 N = " e(N)
esttab m1 m2 m3 m4 using "results/t4_baseline.rtf", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label nogaps compress ///
    mtitles("OLS" "加控制" "年度FE" "双向FE") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("观测值" "调整R2")) ///
    title("表4 基准回归 被解释变量 应计盈余管理")
esttab m1 m2 m3 m4 using "results/t4_baseline.csv", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label plain mtitles("OLS" "Ctrl" "YearFE" "TwoWay") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "adjR2"))

*==================================================================*
* 8 调节效应 事务所规模
*==================================================================*
eststo clear
eststo r1: reghdfe AbsDA AuditSpec Big4 $Controls, absorb(year) vce(cluster stkcd) keepsingletons
eststo r2: reghdfe AbsDA AuditSpec Big4 SpecBig4 $Controls, absorb(year) vce(cluster stkcd) keepsingletons
esttab r1 r2 using "results/t5_moderation.rtf", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label nogaps compress ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("观测值" "调整R2")) ///
    title("表5 调节效应 事务所规模")
esttab r1 r2 using "results/t5_moderation.csv", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label plain stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "adjR2"))

*==================================================================*
* 9 子样本 进一步研究
*==================================================================*
* 按事务所规模 四大 与 非四大
eststo clear
eststo s1: reghdfe AbsDA AuditSpec $Controls if Big4==1, absorb(year) vce(cluster stkcd)
eststo s2: reghdfe AbsDA AuditSpec $Controls if Big4==0, absorb(year) vce(cluster stkcd)
* 按行业专长高低 中位数
qui sum AuditSpec, detail
gen HighSpec = AuditSpec>=r(p50) if !missing(AuditSpec)
eststo s3: reghdfe AbsDA AuditSpec $Controls if HighSpec==1, absorb(year) vce(cluster stkcd)
eststo s4: reghdfe AbsDA AuditSpec $Controls if HighSpec==0, absorb(year) vce(cluster stkcd)
* 按产权性质
eststo s5: reghdfe AbsDA AuditSpec $Controls if SOE==1, absorb(year) vce(cluster stkcd)
eststo s6: reghdfe AbsDA AuditSpec $Controls if SOE==0, absorb(year) vce(cluster stkcd)
esttab s1 s2 s3 s4 s5 s6 using "results/t6_subsample.rtf", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label nogaps compress ///
    mtitles("四大" "非四大" "高专长" "低专长" "国有" "非国有") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("观测值" "调整R2")) ///
    title("表6 子样本分析")
esttab s1 s2 s3 s4 s5 s6 using "results/t6_subsample.csv", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label plain mtitles("Big4" "NonBig4" "HighSpec" "LowSpec" "SOE" "NonSOE") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "adjR2"))

*==================================================================*
* 10 机制检验 中介三步法 审计投入 审计费用
*==================================================================*
eststo clear
eststo me1: reghdfe AbsDA AuditSpec $Controls, absorb(year) vce(cluster stkcd) keepsingletons
eststo me2: reghdfe AuditFee AuditSpec $Controls, absorb(year) vce(cluster stkcd) keepsingletons
eststo me3: reghdfe AbsDA AuditSpec AuditFee $Controls, absorb(year) vce(cluster stkcd) keepsingletons
esttab me1 me2 me3 using "results/t7_mechanism.rtf", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label nogaps compress ///
    mtitles("应计盈余管理" "审计费用" "应计盈余管理") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("观测值" "调整R2")) ///
    title("表7 机制检验 中介三步法")
esttab me1 me2 me3 using "results/t7_mechanism.csv", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label plain mtitles("AbsDA" "AuditFee" "AbsDA") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "adjR2"))

*==================================================================*
* 11 内生性 加分项
*==================================================================*
* 11.1 工具变量 同行业同年度其他公司行业专长均值
bysort ind_id year: egen _sumspec = total(AuditSpec)
bysort ind_id year: egen _cntspec = count(AuditSpec)
gen IV_spec = (_sumspec - AuditSpec)/(_cntspec - 1) if _cntspec>1
label var IV_spec "同行业同年度行业专长均值"
eststo clear
capture noisily eststo iv1: ivreghdfe AbsDA $Controls (AuditSpec=IV_spec), absorb(year) cluster(stkcd) first
if _rc!=0 {
    di "ivreghdfe 不可用 改用 ivreg2"
    capture noisily eststo iv1: ivreg2 AbsDA $Controls i.year (AuditSpec=IV_spec), cluster(stkcd) first
}
* 11.2 解释变量滞后一期
xtset stkcd year
eststo iv2: reghdfe AbsDA L.AuditSpec $Controls, absorb(year) vce(cluster stkcd)
capture noisily esttab iv1 iv2 using "results/t8_endogeneity.rtf", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label nogaps compress ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("观测值" "调整R2")) ///
    title("表8 内生性检验")
capture noisily esttab iv1 iv2 using "results/t8_endogeneity.csv", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label plain stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "adjR2"))

*==================================================================*
* 12 稳健性 替换被解释变量 带符号 DA 绝对值用 EM 另测度
*==================================================================*
eststo clear
gen AbsDA_alt = abs(DA)
winsor2 AbsDA_alt, cuts(1 99) replace
eststo rb1: reghdfe AbsDA_alt AuditSpec $Controls, absorb(year) vce(cluster stkcd)
eststo rb2: reghdfe AbsDA AuditSpec $Controls, absorb(ind_id year) vce(cluster stkcd) keepsingletons
capture noisily esttab rb1 rb2 using "results/t9_robust.rtf", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label nogaps compress ///
    mtitles("替换被解释变量" "双向固定效应") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("观测值" "调整R2")) ///
    title("表9 稳健性检验")
capture noisily esttab rb1 rb2 using "results/t9_robust.csv", replace b(%9.4f) se(%9.4f) ///
    star(* 0.1 ** 0.05 *** 0.01) label plain mtitles("AltY" "TwoWay") ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "adjR2"))

*==================================================================*
* 13 图形 出自 Stata
*==================================================================*
graph set window fontface "Times New Roman"

* 图1 应计盈余管理核密度 按事务所规模
twoway (kdensity AbsDA if Big4==1, lpattern(solid)) ///
       (kdensity AbsDA if Big4==0, lpattern(dash)), ///
    legend(order(1 "{stSerif:四大}" 2 "{stSerif:非四大}") size(*1.1)) ///
    xtitle("{stSerif:应计盈余管理}", size(*1.3)) ytitle("{stSerif:核密度}", size(*1.3)) ///
    xlabel(, labsize(*1.2)) ylabel(, labsize(*1.2)) scheme(s2mono)
graph export "results/fig1_kdensity.png", as(png) width(3000) replace

* 图2 调节效应 边际图
qui reghdfe AbsDA c.AuditSpec##i.Big4 $Controls, absorb(year) vce(cluster stkcd)
margins Big4, at(AuditSpec=(0(0.1)0.6))
marginsplot, ///
    xtitle("{stSerif:审计师行业专长}", size(*1.3)) ytitle("{stSerif:应计盈余管理预测值}", size(*1.3)) ///
    legend(order(3 "{stSerif:非四大}" 4 "{stSerif:四大}") size(*1.1)) ///
    title("") xlabel(, labsize(*1.2)) ylabel(, labsize(*1.2)) scheme(s2mono)
graph export "results/fig2_moderation.png", as(png) width(3000) replace

* 保存清洗后面板
save "data/cleaned_panel.dta", replace
export delimited using "data/cleaned_panel.csv", replace

di "==== ALL DONE N = $N ===="
