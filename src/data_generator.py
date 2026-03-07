import random
from faker import Faker

MAX_AMOUNT = 9999  # maximum amount that can be generated at once

LOCALE_MAPPING_NAME = {
    "ar_AA": "Arabic (Arabia)",
    "ar_DZ": "Arabic (Algeria)",
    "ar_PS": "Arabic (Palestine)",
    "ar_SA": "Arabic (Saudi Arabia)",
    "hy_AM": "Armenian (Armenia)",
    "az_AZ": "Azerbaijani (Azerbaijan)",
    "bn_BD": "Bengali (Bangladesh)",
    "bg_BG": "Bulgarian (Bulgaria)",
    "zh_CN": "Chinese (China)",
    "zh_TW": "Chinese (Taiwan)",
    "hr_HR": "Croatian (Croatia)",
    "cs_CZ": "Czech (Czech Republic)",
    "da_DK": "Danish (Denmark)",
    "nl_BE": "Dutch (Belgium)",
    "nl_NL": "Dutch (Netherlands)",
    "en": "English (Generic)",
    "en_GB": "English (United Kingdom)",
    "en_IE": "English (Ireland)",
    "en_IN": "English (India)",
    "en_KE": "English (Kenya)",
    "en_NG": "English (Nigeria)",
    "en_NZ": "English (New Zealand)",
    "en_PK": "English (Pakistan)",
    "en_TH": "English (Thailand)",
    "en_US": "English (United States)",
    "et_EE": "Estonian (Estonia)",
    "fil_PH": "Filipino (Philippines)",
    "fi_FI": "Finnish (Finland)",
    "fr_BE": "French (Belgium)",
    "fr_CA": "French (Canada)",
    "fr_CH": "French (Switzerland)",
    "fr_DZ": "French (Algeria)",
    "fr_FR": "French (France)",
    "ka_GE": "Georgian (Georgia)",
    "de_AT": "German (Austria)",
    "de_CH": "German (Switzerland)",
    "de_DE": "German (Germany)",
    "de_LI": "German (Liechtenstein)",
    "de_LU": "German (Luxembourg)",
    "el_GR": "Greek (Greece)",
    "gu_IN": "Gujarati (India)",
    "ha_NG": "Hausa (Nigeria)",
    "he_IL": "Hebrew (Israel)",
    "hi_IN": "Hindi (India)",
    "hu_HU": "Hungarian (Hungary)",
    "is_IS": "Icelandic (Iceland)",
    "ig_NG": "Igbo (Nigeria)",
    "id_ID": "Indonesian (Indonesia)",
    "ga_IE": "Irish (Ireland)",
    "it_IT": "Italian (Italy)",
    "ja_JP": "Japanese (Japan)",
    "ko_KR": "Korean (South Korea)",
    "lv_LV": "Latvian (Latvia)",
    "lt_LT": "Lithuanian (Lithuania)",
    "ne_NP": "Nepali (Nepal)",
    "no_NO": "Norwegian (Norway)",
    "or_IN": "Odia (India)",
    "fa_IR": "Persian (Iran)",
    "pl_PL": "Polish (Poland)",
    "pt_BR": "Portuguese (Brazil)",
    "pt_PT": "Portuguese (Portugal)",
    "ro_RO": "Romanian (Romania)",
    "ru_RU": "Russian (Russia)",
    "sk_SK": "Slovak (Slovakia)",
    "sl_SI": "Slovenian (Slovenia)",
    "es": "Spanish (Generic)",
    "es_CA": "Spanish (Canada)",
    "es_CL": "Spanish (Chile)",
    "es_CO": "Spanish (Colombia)",
    "es_ES": "Spanish (Spain)",
    "es_MX": "Spanish (Mexico)",
    "sv_SE": "Swedish (Sweden)",
    "sw": "Swahili (Generic)",
    "tl_PH": "Tagalog (Philippines)",
    "ta_IN": "Tamil (India)",
    "th_TH": "Thai (Thailand)",
    "tr_TR": "Turkish (Turkey)",
    "tw_GH": "Twi (Ghana)",
    "uk_UA": "Ukrainian (Ukraine)",
    "uz_UZ": "Uzbek (Uzbekistan)",
    "vi_VN": "Vietnamese (Vietnam)",
    "yo_NG": "Yoruba (Nigeria)",
    "zu_ZA": "Zulu (South Africa)"
}

LOCALE_MAPPING_PHONE = {
    'sq_AL': 'Albanian',
    'ar_AA': 'Arabic',
    'ar_DZ': 'Arabic (Algeria)',
    'ar_BH': 'Arabic (Bahrain)',
    'ar_EG': 'Arabic (Egypt)',
    'ar_JO': 'Arabic (Jordan)',
    'ar_PS': 'Arabic (Palestine)',
    'ar_SA': 'Arabic (Saudi Arabia)',
    'ar_AE': 'Arabic (United Arab Emirates)',
    'hy_AM': 'Armenian',
    'az_AZ': 'Azerbaijani',
    'bn_BD': 'Bengali',
    'bs_BA': 'Bosnian',
    'bg_BG': 'Bulgarian',
    'zh_CN': 'Chinese (China)',
    'zh_TW': 'Chinese (Taiwan)',
    'hr_HR': 'Croatian',
    'cs_CZ': 'Czech',
    'da_DK': 'Danish',
    'nl_BE': 'Dutch (Belgium)',
    'nl_NL': 'Dutch (Netherlands)',
    'en_AU': 'English (Australia)',
    'en_CA': 'English (Canada)',
    'en_GB': 'English (Great Britain)',
    'en_IN': 'English (India)',
    'en_IE': 'English (Ireland)',
    'en_NZ': 'English (New Zealand)',
    'en_TH': 'English (Thailand)',
    'en_US': 'English (United States)',
    'et_EE': 'Estonian',
    'fi_FI': 'Finnish',
    'fr_BE': 'French (Belgium)',
    'fr_CA': 'French (Canada)',
    'fr_FR': 'French (France)',
    'fr_CH': 'French (Switzerland)',
    'ka_GE': 'Georgian',
    'de_AT': 'German (Austria)',
    'de_DE': 'German (Germany)',
    'de_CH': 'German (Switzerland)',
    'el_GR': 'Greek',
    'he_IL': 'Hebrew',
    'hi_IN': 'Hindi',
    'hu_HU': 'Hungarian',
    'id_ID': 'Indonesian',
    'it_IT': 'Italian',
    'ja_JP': 'Japanese',
    'ko_KR': 'Korean',
    'lv_LV': 'Latvian',
    'lt_LT': 'Lithuanian',
    'ne_NP': 'Nepali',
    'fa_IR': 'Persian',
    'pl_PL': 'Polish',
    'pt_BR': 'Portuguese (Brazil)',
    'pt_PT': 'Portuguese (Portugal)',
    'ro_RO': 'Romanian',
    'ru_RU': 'Russian',
    'sk_SK': 'Slovak',
    'sl_SI': 'Slovenian',
    'es_AR': 'Spanish (Argentina)',
    'es_CL': 'Spanish (Chile)',
    'es_CO': 'Spanish (Colombia)',
    'es_MX': 'Spanish (Mexico)',
    'es_ES': 'Spanish (Spain)',
    'sv_SE': 'Swedish',
    'ta_IN': 'Tamil',
    'th_TH': 'Thai',
    'tr_TR': 'Turkish',
    'tw_GH': 'Twi (Ghana)',
    'uk_UA': 'Ukrainian',
    'vi_VN': 'Vietnamese'
}


def generate_random_name(sex=None, locale=None, include_title=False):
    fake = Faker(locale)

    if include_title:
        if sex == "male":
            return fake.name_male()
        elif sex == "female":
            return fake.name_female()
        elif sex == "non-binary":
            return fake.name_nonbinary()
        else:
            return fake.name()
    else:
        if sex == "male":
            first_name = fake.first_name_male()
        elif sex == "female":
            first_name = fake.first_name_female()
        elif sex == "non-binary":
            first_name = fake.first_name_nonbinary()
        else:
            first_name = fake.first_name()

        last_name = fake.last_name()
        return f"{first_name} {last_name}"


def generate_random_phone_number(locale=None):
    fake = Faker(locale)
    phone_number = fake.phone_number()
    return phone_number
