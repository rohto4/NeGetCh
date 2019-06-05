'''
Created on 2019/06/04

@author: Rohto
'''
from enum import IntEnum, Enum
import pathlib

# TODO (20190604)考えるコト
# DBで使用するものとscript内で使用するものを分けるべきかどうか
# 共通で同じ文字列を使用できるなら問題なし
# →問題が発生してから分割でも大して影響ないか

class MyClass(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
    
    class Dir():
        # プロジェクトルート
        _PROJECT_ROOT = pathlib.Path('../../').resolve()
        # サムネイル保存
        _THUMBNAIL_DIR = pathlib.Path('../core/img/thumbnail/').resolve()
        # ログ保存
        _LOG_DIR = pathlib.Path('../core/log/').resolve()
        
    class Date():
        _DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
        _NOTICE_SLACK = '%Y-%m-%d %H:%M:%S'
    
    class TagCategory():
        class AtIt():
            # 新着はカテゴリ不明になってしまうため対象外
            _FEATURES = 'Features'
            _CLOUD = 'クラウド'
            _AI_IOT = 'AI IoT'
            _AGILE_DEVOPS = 'アジャイル/DevOps'
            _SECURITIY = 'セキュリティ'
            _CAREER = 'キャリア&スキル'
            _RANKING_DAY = '日間ランキング'
            _RANKING_MONTH = '月間ランキング'
            
        class TechFeed():
            # 未調査            
            _JAVA = 'Java'
            _JAVASCRIPT = 'JavaScript'
            _PYTHON = 'Python'
            _Android = 'Android'
            
    class Type():
        # ニュース / トレンド / コラム / 新技術おためし / 問題解決
        _NEWS = 'NEWS'
        _TREND = 'TREND'
        _COLUMN = 'COLUMN'
        _SKILL = 'SKILL'
        _SOLUTION = 'SOLUTION'
    
    class SiteTitle():
        _ATIT = '@IT'
        _TECHFEED = 'TechFeed'
