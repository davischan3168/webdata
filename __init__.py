__version__ = '0.5.0'
__author__ = 'Davis Chan'

"""
for trading data
"""
from webdata.stock.trading import (get_hist_data, get_tick_data,
                                   get_today_all, get_realtime_quotes,
                                   get_h_data, get_today_ticks,
                                   get_index, get_hists,
                                   get_sina_dd)

"""
for trading data
"""
from webdata.stock.fundamental import (get_stock_basics, get_report_data,
                                       get_profit_data,
                                       get_operation_data, get_growth_data,
                                       get_debtpaying_data, get_cashflow_data)

"""
for macro data
"""
from webdata.stock.macro import (get_gdp_year, get_gdp_quarter,
                                 get_gdp_for, get_gdp_pull,
                                 get_gdp_contrib, get_cpi,
                                 get_ppi, get_deposit_rate,
                                 get_loan_rate, get_rrr,
                                 get_money_supply, get_money_supply_bal)

"""
for classifying data
"""
from webdata.stock.classifying import (get_industry_classified, get_concept_classified,
                                       get_area_classified, get_gem_classified,
                                       get_sme_classified, get_st_classified,
                                       get_hs300s, get_sz50s, get_zz500s,
                                       get_terminated, get_suspended)

"""
for macro data
"""
from webdata.stock.newsevent import (get_latest_news, latest_content,
                                     get_notices, notice_content,
                                     guba_sina)

"""
for reference
"""
from webdata.stock.reference import (profit_data, forecast_data,
                                     xsg_data, fund_holdings,
                                     new_stocks, sh_margins,
                                     sh_margin_details,
                                     sz_margins, sz_margin_details)

"""
for shibor
"""
from webdata.stock.shibor import (shibor_data, shibor_quote_data,
                                  shibor_ma_data, lpr_data,
                                  lpr_ma_data)

"""
for LHB
"""
from webdata.stock.billboard import (top_list, cap_tops, broker_tops,
                                     inst_tops, inst_detail)


"""
for utils
"""
from webdata.util.dateu import (is_holiday)


"""
for DataYes Token
"""
#from webdata.util.upass import (set_token, get_token)

#from webdata.datayes.api import *

from webdata.internet.boxoffice import (realtime_boxoffice, day_boxoffice,
                                        day_cinema, month_boxoffice)

#for person aastock.com
from webdata.puse.aastock import (get_hk_firatio_data,
                                  get_hk_bsheet_data, get_mainindex_data, 
                                  get_hk_earsummary_data)

"""
for eastmoney data
"""
from webdata.puse.eastmoney import (get_currency_data, get_hangye_list,
                                    get_diyu_list,get_gainian_list,
                                    get_usa_list, get_all_list,
                                    get_global_index, get_global_index,
                                    get_mainland_index, get_mainland_index,
                                    get_ha_trading_data, get_hhist_data,
                                    get_ghist_data, get_data_hbf_t,
                                    get_data_hbf_d)

"""
for sina data
"""
from webdata.puse.sina import (get_sina_pepb, get_hangye_sina,
                               get_gainian_sina, get_zjh_sina,
                               get_share_all_sina,
                               get_share_percode_sina,
                               get_hk_trading_sina,
                               get_kzz_trading_sina,
                               get_hk_ha_trading_sina,
                               get_hk_hangye_trading_sina,
                               get_hk_hcg_trading_sina,
                               get_hk_gqg_trading_sina,
                               get_week_zd_sina, get_month_zd_sina,
                               get_balance_sheet_sina,
                               get_income_statement_sina,
                               get_cashflow_statement_sina,
                               get_financial_index_sina,
                               get_euro_sina_index, get_asia_sina_index,
                               get_america_sina_index, get_africa_sina_index,
                               get_ocean_sina_index, get_realtime_fc_sina,
                               get_hmin_fc, get_hmin_if, get_hday_fc,
                               get_hday_if, get_ddV, get_ddA, get_ddT,
                               get_predict, get_predict_percode)

"""
for jqka data 
"""
from webdata.puse.jqka import ( get_current_hu_ths,
                                get_current_hongk_ths,
                                get_share_cashflow_ths,
                                get_finance_index_ths,
                                get_hk_financial_ths)
                                    
"""
For person app
"""
from webdata.puse.myapp import ( annlysis_shares_holdbyfund, get_myquandl,
                                 get_myquandl_hdf5, get_history_data_mp,
                                 get_data_last3year_mp)
                                  

