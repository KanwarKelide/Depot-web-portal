from django.db import models


#-------------------------***************************---------------------------
#VARIABLE DECLARATION
#DEPOT NAMES
MIYAPUR = 'MIYAPUR'
JBS     = 'JBS'

#ROUTE NUMBERS
MYP_AJ = 'AJ'
MYP_AB = 'AB'
JBS_AM = 'AM'
JBS_AL = 'AL'

#SHIFT OPTIONS
SHIFT_CHOICES    = (('1st', '1st'), ('2nd', '2nd'))

#DRIVER ID'S MIYAPUR
MYP_20001 = '20001'
MYP_20002 = '20002'
MYP_20005 = '20005'
MYP_20008 = '20008'
MYP_20009 = '20009'
MYP_20011 = '20011'
MYP_20012 = '20012'
MYP_20013 = '20013'
MYP_20014 = '20014'
MYP_20017 = '20017'
MYP_20019 = '20019'
MYP_20025 = '20025'
MYP_20028 = '20028'
MYP_20029 = '20029'
MYP_20031 = '20031'
MYP_20032 = '20032'
MYP_20034 = '20034'
MYP_20036 = '20036'
MYP_20037 = '20037'
MYP_20038 = '20038'
MYP_20043 = '20043'
MYP_20044 = '20044'
MYP_20045 = '20045'
MYP_20049 = '20049'
MYP_20050 = '20050'
MYP_20054 = '20054'
MYP_20055 = '20055'
MYP_20056 = '20056'
MYP_20058 = '20058'
MYP_20059 = '20059'
MYP_20064 = '20064'
MYP_20071 = '20071'
MYP_20072 = '20072'
MYP_20074 = '20074'
MYP_20076 = '20076'
MYP_20077 = '20077'
MYP_20080 = '20080'
MYP_20081 = '20081'
MYP_20082 = '20082'
MYP_20084 = '20084'
MYP_20085 = '20085'
MYP_20086 = '20086'
MYP_20087 = '20087'
MYP_20088 = '20088'
MYP_20089 = '20089'
MYP_20090 = '20090'
MYP_20091 = '20091'
MYP_20092 = '20092'
MYP_20093 = '20093'
MYP_20094 = '20094'
MYP_20095 = '20095'
MYP_20096 = '20096'
MYP_20097 = '20097'
MYP_20098 = '20098'
MYP_20099 = '20099'

#DRIVER ID'S JBS
JBS_10004 = '10004'
JBS_10005 = '10005'
JBS_10006 = '10006'
JBS_10007 = '10007'
JBS_10008 = '10008'
JBS_10009 = '10009'
JBS_10010 = '10010'
JBS_10011 = '10011'
JBS_10012 = '10012'
JBS_10014 = '10014'
JBS_10016 = '10016'
JBS_10018 = '10018'
JBS_10023 = '10023'
JBS_10026 = '10026'
JBS_10027 = '10027'
JBS_10028 = '10028'
JBS_10030 = '10030'
JBS_10034 = '10034'
JBS_10035 = '10035'
JBS_10038 = '10038'
JBS_10040 = '10040'
JBS_10041 = '10041'
JBS_10043 = '10043'
JBS_10044 = '10044'
JBS_10047 = '10047'
JBS_10048 = '10048'
JBS_10049 = '10049'
JBS_10052 = '10052'
JBS_10056 = '10056'
JBS_10058 = '10058'
JBS_10060 = '10060'
JBS_10061 = '10061'
JBS_10064 = '10064'
JBS_10068 = '10068'
JBS_10071 = '10071'
JBS_10073 = '10073'
JBS_10074 = '10074'
JBS_10075 = '10075'
JBS_10076 = '10076'
JBS_10077 = '10077'
JBS_10079 = '10079'
JBS_10080 = '10080'
JBS_10081 = '10081'
JBS_10083 = '10083'
JBS_10085 = '10085'
JBS_10086 = '10086'
JBS_10087 = '10087'
JBS_10093 = '10093'
JBS_10094 = '10094'
JBS_10096 = '10096'

#SERVICE NUMBER MIYAPUR
MYP_AJ_500 = '500'
MYP_AJ_501 = '501'
MYP_AJ_502 = '502'
MYP_AJ_503 = '503'
MYP_AJ_504 = '504'
MYP_AJ_505 = '505'
MYP_AJ_506 = '506'
MYP_AJ_507 = '507'
MYP_AJ_508 = '508'
MYP_AJ_509 = '509'
MYP_AJ_510 = '510'
MYP_AJ_511 = '511'
MYP_AJ_512 = '512'
MYP_AJ_513 = '513'
MYP_AJ_514 = '514'
MYP_AJ_515 = '515'
MYP_AB_516 = '516'
MYP_AB_517 = '517'
MYP_AB_518 = '518'
MYP_AB_519 = '519'

#SERVICE NO JBS
JBS_AL_501 = '501'
JBS_AL_502 = '502'
JBS_AL_503 = '503'
JBS_AL_504 = '504'
JBS_AL_505 = '505'
JBS_AL_506 = '506'
JBS_AL_507 = '507'
JBS_AL_508 = '508'
JBS_AL_509 = '509'
JBS_AL_510 = '510'
JBS_AL_521 = '521'
JBS_AL_522 = '522'
JBS_AM_511 = '511'
JBS_AM_512 = '512'
JBS_AM_513 = '513'
JBS_AM_514 = '514'
JBS_AM_515 = '515'
JBS_AM_516 = '516'
JBS_AM_517 = '517'
JBS_AM_518 = '518'


#MIYAPUR BUS NUMBERS
MYP_TS_10UB_8168 = 'TS 10UB 8168'
MYP_TS_10UB_8169 = 'TS 10UB 8169'
MYP_TS_10UB_8170 = 'TS 10UB 8170'
MYP_TS_10UB_8171 = 'TS 10UB 8171'
MYP_TS_10UB_8172 = 'TS 10UB 8172'
MYP_TS_10UB_8177 = 'TS 10UB 8177'
MYP_TS_10UB_8178 = 'TS 10UB 8178'
MYP_TS_10UB_8179 = 'TS 10UB 8179'
MYP_TS_10UB_8180 = 'TS 10UB 8180'
MYP_TS_10UB_8181 = 'TS 10UB 8181'
MYP_TS_10UB_8182 = 'TS 10UB 8182'
MYP_TS_10UB_8183 = 'TS 10UB 8183'
MYP_TS_10UB_8184 = 'TS 10UB 8184'
MYP_TS_10UB_8185 = 'TS 10UB 8185'
MYP_TS_10UB_8186 = 'TS 10UB 8186'
MYP_TS_10UB_8187 = 'TS 10UB 8187'
MYP_TS_10UB_8188 = 'TS 10UB 8188'
MYP_TS_10UB_8189 = 'TS 10UB 8189'
MYP_TS_10UB_8190 = 'TS 10UB 8190'
MYP_TS_10UB_8191 = 'TS 10UB 8191'
MYP_TS_10UB_8169 = 'TS 10UB 8169'

#JBS BUS NUMBERS
JBS_TS_10UB_8167 = 'TS 10UB 8167'
JBS_TS_10UB_8173 = 'TS 10UB 8173'
JBS_TS_10UB_8174 = 'TS 10UB 8174'
JBS_TS_10UB_8175 = 'TS 10UB 8175'
JBS_TS_10UB_8176 = 'TS 10UB 8176'
JBS_TS_10UB_8166 = 'TS 10UB 8166'
JBS_TS_10UB_6785 = 'TS 10UB 6785'
JBS_TS_10UB_6784 = 'TS 10UB 6784'
JBS_TS_10UB_6783 = 'TS 10UB 6783'
JBS_TS_10UB_6782 = 'TS 10UB 6782'
JBS_TS_10UB_7963 = 'TS 10UB 7963'
JBS_TS_10UB_7966 = 'TS 10UB 7966'
JBS_TS_10UB_7964 = 'TS 10UB 7964'
JBS_TS_10UB_8025 = 'TS 10UB 8025'
JBS_TS_10UB_6921 = 'TS 10UB 6921'
JBS_TS_10UB_8353 = 'TS 10UB 8353'
JBS_TS_10UB_8351 = 'TS 10UB 8351'
JBS_TS_10UB_8352 = 'TS 10UB 8352'
JBS_TS_10UB_8354 = 'TS 10UB 8354'
JBS_TS_10UB_8355 = 'TS 10UB 8355'

#-------------------------***************************---------------------------
#LIST OF TUPLES DEFINING DROPDOWN CHOICES

DEPOT_CHOICES = [
    (MIYAPUR, MIYAPUR),
    (JBS, JBS),
]

ROUTE_CHOICES = [
    (MYP_AJ, MYP_AJ),
    (MYP_AB, MYP_AB),
    (JBS_AM, JBS_AM),
    (JBS_AL, JBS_AL),
]

VEHICLE_CHOICES = [
    (MYP_TS_10UB_8168, MYP_TS_10UB_8168),
    (MYP_TS_10UB_8169, MYP_TS_10UB_8169),
    (MYP_TS_10UB_8170, MYP_TS_10UB_8170),
    (MYP_TS_10UB_8171, MYP_TS_10UB_8171),
    (MYP_TS_10UB_8172, MYP_TS_10UB_8172),
    (MYP_TS_10UB_8177, MYP_TS_10UB_8177),
    (MYP_TS_10UB_8178, MYP_TS_10UB_8178),
    (MYP_TS_10UB_8179, MYP_TS_10UB_8179),
    (MYP_TS_10UB_8180, MYP_TS_10UB_8180),
    (MYP_TS_10UB_8181, MYP_TS_10UB_8181),
    (MYP_TS_10UB_8182, MYP_TS_10UB_8182),
    (MYP_TS_10UB_8183, MYP_TS_10UB_8183),
    (MYP_TS_10UB_8184, MYP_TS_10UB_8184),
    (MYP_TS_10UB_8185, MYP_TS_10UB_8185),
    (MYP_TS_10UB_8186, MYP_TS_10UB_8186),
    (MYP_TS_10UB_8187, MYP_TS_10UB_8187),
    (MYP_TS_10UB_8188, MYP_TS_10UB_8188),
    (MYP_TS_10UB_8189, MYP_TS_10UB_8189),
    (MYP_TS_10UB_8190, MYP_TS_10UB_8190),
    (MYP_TS_10UB_8191, MYP_TS_10UB_8191),
    (JBS_TS_10UB_8167, JBS_TS_10UB_8167),
    (JBS_TS_10UB_8173, JBS_TS_10UB_8173),
    (JBS_TS_10UB_8174, JBS_TS_10UB_8174),
    (JBS_TS_10UB_8175, JBS_TS_10UB_8175),
    (JBS_TS_10UB_8176, JBS_TS_10UB_8176),
    (JBS_TS_10UB_8166, JBS_TS_10UB_8166),
    (JBS_TS_10UB_6785, JBS_TS_10UB_6785),
    (JBS_TS_10UB_6784, JBS_TS_10UB_6784),
    (JBS_TS_10UB_6783, JBS_TS_10UB_6783),
    (JBS_TS_10UB_6782, JBS_TS_10UB_6782),
    (JBS_TS_10UB_7963, JBS_TS_10UB_7963),
    (JBS_TS_10UB_7966, JBS_TS_10UB_7966),
    (JBS_TS_10UB_7964, JBS_TS_10UB_7964),
    (JBS_TS_10UB_8025, JBS_TS_10UB_8025),
    (JBS_TS_10UB_6921, JBS_TS_10UB_6921),
    (JBS_TS_10UB_8353, JBS_TS_10UB_8353),
    (JBS_TS_10UB_8351, JBS_TS_10UB_8351),
    (JBS_TS_10UB_8352, JBS_TS_10UB_8352),
    (JBS_TS_10UB_8354, JBS_TS_10UB_8354),
    (JBS_TS_10UB_8355, JBS_TS_10UB_8355),
]

DRIVER_CHOICES=[
        (MYP_20001, MYP_20001),
        (MYP_20002, MYP_20002),
        (MYP_20005, MYP_20005),
        (MYP_20008, MYP_20008),
        (MYP_20009, MYP_20009),
        (MYP_20011, MYP_20011),
        (MYP_20012, MYP_20012),
        (MYP_20013, MYP_20013),
        (MYP_20014, MYP_20014),
        (MYP_20017, MYP_20017),
        (MYP_20019, MYP_20019),
        (MYP_20025, MYP_20025),
        (MYP_20028, MYP_20028),
        (MYP_20029, MYP_20029),
        (MYP_20031, MYP_20031),
        (MYP_20032, MYP_20032),
        (MYP_20034, MYP_20034),
        (MYP_20036, MYP_20036),
        (MYP_20037, MYP_20037),
        (MYP_20038, MYP_20038),
        (MYP_20043, MYP_20043),
        (MYP_20044, MYP_20044),
        (MYP_20045, MYP_20045),
        (MYP_20049, MYP_20049),
        (MYP_20050, MYP_20050),
        (MYP_20054, MYP_20054),
        (MYP_20055, MYP_20055),
        (MYP_20056, MYP_20056),
        (MYP_20058, MYP_20058),
        (MYP_20059, MYP_20059),
        (MYP_20064, MYP_20064),
        (MYP_20071, MYP_20071),
        (MYP_20072, MYP_20072),
        (MYP_20074, MYP_20074),
        (MYP_20076, MYP_20076),
        (MYP_20077, MYP_20077),
        (MYP_20080, MYP_20080),
        (MYP_20081, MYP_20081),
        (MYP_20082, MYP_20082),
        (MYP_20084, MYP_20084),
        (MYP_20085, MYP_20085),
        (MYP_20086, MYP_20086),
        (MYP_20087, MYP_20087),
        (MYP_20088, MYP_20088),
        (MYP_20089, MYP_20089),
        (MYP_20090, MYP_20090),
        (MYP_20091, MYP_20091),
        (MYP_20092, MYP_20092),
        (MYP_20093, MYP_20093),
        (MYP_20094, MYP_20094),
        (MYP_20095, MYP_20095),
        (MYP_20096, MYP_20096),
        (MYP_20097, MYP_20097),
        (MYP_20098, MYP_20098),
        (MYP_20099, MYP_20099),
        (JBS_10004, JBS_10004),
        (JBS_10005, JBS_10005),
        (JBS_10006, JBS_10006),
        (JBS_10007, JBS_10007),
        (JBS_10008, JBS_10008),
        (JBS_10009, JBS_10009),
        (JBS_10010, JBS_10010),
        (JBS_10011, JBS_10011),
        (JBS_10012, JBS_10012),
        (JBS_10014, JBS_10014),
        (JBS_10016, JBS_10016),
        (JBS_10018, JBS_10018),
        (JBS_10023, JBS_10023),
        (JBS_10026, JBS_10026),
        (JBS_10027, JBS_10027),
        (JBS_10028, JBS_10028),
        (JBS_10030, JBS_10030),
        (JBS_10034, JBS_10034),
        (JBS_10035, JBS_10035),
        (JBS_10038, JBS_10038),
        (JBS_10040, JBS_10040),
        (JBS_10041, JBS_10041),
        (JBS_10043, JBS_10043),
        (JBS_10044, JBS_10044),
        (JBS_10047, JBS_10047),
        (JBS_10048, JBS_10048),
        (JBS_10049, JBS_10049),
        (JBS_10052, JBS_10052),
        (JBS_10056, JBS_10056),
        (JBS_10058, JBS_10058),
        (JBS_10060, JBS_10060),
        (JBS_10061, JBS_10061),
        (JBS_10064, JBS_10064),
        (JBS_10068, JBS_10068),
        (JBS_10071, JBS_10071),
        (JBS_10073, JBS_10073),
        (JBS_10074, JBS_10074),
        (JBS_10075, JBS_10075),
        (JBS_10076, JBS_10076),
        (JBS_10077, JBS_10077),
        (JBS_10079, JBS_10079),
        (JBS_10080, JBS_10080),
        (JBS_10081, JBS_10081),
        (JBS_10083, JBS_10083),
        (JBS_10085, JBS_10085),
        (JBS_10086, JBS_10086),
        (JBS_10087, JBS_10087),
        (JBS_10093, JBS_10093),
        (JBS_10094, JBS_10094),
        (JBS_10096, JBS_10096),

]


SERVICE_CHOICES = [
    (MYP_AJ_500, MYP_AJ_500),
    (MYP_AJ_501, MYP_AJ_501),
    (MYP_AJ_502, MYP_AJ_502),
    (MYP_AJ_503, MYP_AJ_503),
    (MYP_AJ_504, MYP_AJ_504),
    (MYP_AJ_505, MYP_AJ_505),
    (MYP_AJ_506, MYP_AJ_506),
    (MYP_AJ_507, MYP_AJ_507),
    (MYP_AJ_508, MYP_AJ_508),
    (MYP_AJ_509, MYP_AJ_509),
    (MYP_AJ_510, MYP_AJ_510),
    (MYP_AJ_511, MYP_AJ_511),
    (MYP_AJ_512, MYP_AJ_512),
    (MYP_AJ_513, MYP_AJ_513),
    (MYP_AJ_514, MYP_AJ_514),
    (MYP_AJ_515, MYP_AJ_515),
    (MYP_AB_516, MYP_AB_516),
    (MYP_AB_517, MYP_AB_517),
    (MYP_AB_518, MYP_AB_518),
    (MYP_AB_519, MYP_AB_519),
    (JBS_AL_501, JBS_AL_501),
    (JBS_AL_502, JBS_AL_502),
    (JBS_AL_503, JBS_AL_503),
    (JBS_AL_504, JBS_AL_504),
    (JBS_AL_505, JBS_AL_505),
    (JBS_AL_506, JBS_AL_506),
    (JBS_AL_507, JBS_AL_507),
    (JBS_AL_508, JBS_AL_508),
    (JBS_AL_509, JBS_AL_509),
    (JBS_AL_510, JBS_AL_510),
    (JBS_AL_521, JBS_AL_521),
    (JBS_AL_522, JBS_AL_522),
    (JBS_AM_511, JBS_AM_511),
    (JBS_AM_512, JBS_AM_512),
    (JBS_AM_513, JBS_AM_513),
    (JBS_AM_514, JBS_AM_514),
    (JBS_AM_515, JBS_AM_515),
    (JBS_AM_516, JBS_AM_516),
    (JBS_AM_517, JBS_AM_517),
    (JBS_AM_518, JBS_AM_518),

]


#-------------------------***************************---------------------------

#FUNCTIONS TO PUSH DATA TO MODELS
#SERVICE FUNTION MIYAPUR AJ
def get_myp_service_aj_strings():
    myp_service_aj_strings = [
        MYP_AJ_500,
        MYP_AJ_501,
        MYP_AJ_502,
        MYP_AJ_503,
        MYP_AJ_504,
        MYP_AJ_505,
        MYP_AJ_506,
        MYP_AJ_507,
        MYP_AJ_508,
        MYP_AJ_509,
        MYP_AJ_510,
        MYP_AJ_511,
        MYP_AJ_512,
        MYP_AJ_513,
        MYP_AJ_514,
        MYP_AJ_515,
    ]
    return myp_service_aj_strings

#SERVICE FUNTION MIYAPUR AB
def get_myp_service_ab_strings():
    myp_service_ab_strings = [
        MYP_AB_516,
        MYP_AB_517,
        MYP_AB_518,
        MYP_AB_519,
    ]
    return myp_service_ab_strings

#SERVICE FUNTION MIYAPUR AM
def get_jbs_service_am_strings():
    jbs_service_am_strings = [
        JBS_AM_511,
        JBS_AM_512,
        JBS_AM_513,
        JBS_AM_514,
        JBS_AM_515,
        JBS_AM_516,
        JBS_AM_517,
        JBS_AM_518,
    ]
    return jbs_service_am_strings

#SERVICE FUNTION MIYAPUR AL
def get_jbs_service_al_strings():
    jbs_service_al_strings = [
        JBS_AL_501,
        JBS_AL_502,
        JBS_AL_503,
        JBS_AL_504,
        JBS_AL_505,
        JBS_AL_506,
        JBS_AL_507,
        JBS_AL_508,
        JBS_AL_509,
        JBS_AL_510,
        JBS_AL_521,
        JBS_AL_522,
    ]
    return jbs_service_al_strings

#ROUTE FUNCTION MIYAPUR
def get_myp_route_strings():
    myp_route_strings = [
        MYP_AJ,
        MYP_AB,
    ]
    return myp_route_strings


#ROUTE FUNCTION JBS
def get_jbs_route_strings():
    jbs_route_strings = [
        JBS_AM,
        JBS_AL,
    ]
    return jbs_route_strings


#DRIVER FUNCTION MIYAPUR
def get_myp_driver_strings():
    myp_driver_strings = [
        MYP_20001,
        MYP_20002,
        MYP_20005,
        MYP_20008,
        MYP_20009,
        MYP_20011,
        MYP_20012,
        MYP_20013,
        MYP_20014,
        MYP_20017,
        MYP_20019,
        MYP_20025,
        MYP_20028,
        MYP_20029,
        MYP_20031,
        MYP_20032,
        MYP_20034,
        MYP_20036,
        MYP_20037,
        MYP_20038,
        MYP_20043,
        MYP_20044,
        MYP_20045,
        MYP_20049,
        MYP_20050,
        MYP_20054,
        MYP_20055,
        MYP_20056,
        MYP_20058,
        MYP_20059,
        MYP_20064,
        MYP_20071,
        MYP_20072,
        MYP_20074,
        MYP_20076,
        MYP_20077,
        MYP_20080,
        MYP_20081,
        MYP_20082,
        MYP_20084,
        MYP_20085,
        MYP_20086,
        MYP_20087,
        MYP_20088,
        MYP_20089,
        MYP_20090,
        MYP_20091,
        MYP_20092,
        MYP_20093,
        MYP_20094,
        MYP_20095,
        MYP_20096,
        MYP_20097,
        MYP_20098,
        MYP_20099,

    ]
    return myp_driver_strings


#DRIVER FUNCTION JBS
def get_jbs_driver_strings():
    jbs_driver_strings = [
        JBS_10004,
        JBS_10005,
        JBS_10006,
        JBS_10007,
        JBS_10008,
        JBS_10009,
        JBS_10010,
        JBS_10011,
        JBS_10012,
        JBS_10014,
        JBS_10016,
        JBS_10018,
        JBS_10023,
        JBS_10026,
        JBS_10027,
        JBS_10028,
        JBS_10030,
        JBS_10034,
        JBS_10035,
        JBS_10038,
        JBS_10040,
        JBS_10041,
        JBS_10043,
        JBS_10044,
        JBS_10047,
        JBS_10048,
        JBS_10049,
        JBS_10052,
        JBS_10056,
        JBS_10058,
        JBS_10060,
        JBS_10061,
        JBS_10064,
        JBS_10068,
        JBS_10071,
        JBS_10073,
        JBS_10074,
        JBS_10075,
        JBS_10076,
        JBS_10077,
        JBS_10079,
        JBS_10080,
        JBS_10081,
        JBS_10083,
        JBS_10085,
        JBS_10086,
        JBS_10087,
        JBS_10093,
        JBS_10094,
        JBS_10096,
    ]
    return jbs_driver_strings

#VEHICLE NUMBER FUNCTION MIYAPUR
def get_myp_vehicle_strings():
    myp_vehicle_strings = [
        MYP_TS_10UB_8168,
        MYP_TS_10UB_8169,
        MYP_TS_10UB_8170,
        MYP_TS_10UB_8171,
        MYP_TS_10UB_8172,
        MYP_TS_10UB_8177,
        MYP_TS_10UB_8178,
        MYP_TS_10UB_8179,
        MYP_TS_10UB_8180,
        MYP_TS_10UB_8181,
        MYP_TS_10UB_8182,
        MYP_TS_10UB_8183,
        MYP_TS_10UB_8184,
        MYP_TS_10UB_8185,
        MYP_TS_10UB_8186,
        MYP_TS_10UB_8187,
        MYP_TS_10UB_8188,
        MYP_TS_10UB_8189,
        MYP_TS_10UB_8190,
        MYP_TS_10UB_8191,
    ]
    return myp_vehicle_strings

#VEHICLE NUMBER FUNCTION JBS
def get_jbs_vehicle_strings():
    jbs_vehicle_strings = [
        JBS_TS_10UB_8167,
        JBS_TS_10UB_8173,
        JBS_TS_10UB_8174,
        JBS_TS_10UB_8175,
        JBS_TS_10UB_8176,
        JBS_TS_10UB_8166,
        JBS_TS_10UB_6785,
        JBS_TS_10UB_6784,
        JBS_TS_10UB_6783,
        JBS_TS_10UB_6782,
        JBS_TS_10UB_7963,
        JBS_TS_10UB_7966,
        JBS_TS_10UB_7964,
        JBS_TS_10UB_8025,
        JBS_TS_10UB_6921,
        JBS_TS_10UB_8353,
        JBS_TS_10UB_8351,
        JBS_TS_10UB_8352,
        JBS_TS_10UB_8354,
        JBS_TS_10UB_8355,
    ]
    return jbs_vehicle_strings

#-------------------------***************************---------------------------

class arrival(models.Model):
    Depot                    = models.CharField(max_length=255, choices=DEPOT_CHOICES,   default='SOME STRING')
    Shift                    = models.CharField(max_length=255, choices=SHIFT_CHOICES,   default='SOME STRING')
    Vehicle_id               = models.CharField(max_length=255, choices=VEHICLE_CHOICES, default='SOME STRING')
    Service_no               = models.CharField(max_length=255, choices=SERVICE_CHOICES, default='SOME STRING')
    Route_no                 = models.CharField(max_length=255, choices=ROUTE_CHOICES,   default='SOME STRING')
    Driver_id                = models.CharField(max_length=255, choices=DRIVER_CHOICES,  default='SOME STRING')
    Scheduled_departure_time = models.CharField(max_length=100)
    Actual_departure_time    = models.CharField(max_length=100)
    Odometer_start_reading   = models.CharField(max_length=100)
    SOC_at_departure         = models.CharField(max_length=100)

    def __str__(self):
        return self.name
