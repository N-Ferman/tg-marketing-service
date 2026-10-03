LEGAL_DOCUMENTS = {
    "privacy": {
        "title": "РџРѕР»РёС‚РёРєР° РєРѕРЅС„РёРґРµРЅС†РёР°Р»СЊРЅРѕСЃС‚Рё",
        "updated_at": "2026-07-01",
    },
    "agreement": {
        "title": "РџРѕР»СЊР·РѕРІР°С‚РµР»СЊСЃРєРѕРµ СЃРѕРіР»Р°С€РµРЅРёРµ",
        "updated_at": "2026-07-01",
    },
    "offer": {
        "title": "РџСѓР±Р»РёС‡РЅР°СЏ РѕС„РµСЂС‚Р°",
        "updated_at": "2026-07-01",
    },
}

CONSENT_DOCUMENTS = {
    "privacy_policy": LEGAL_DOCUMENTS["privacy"],
    "personal_data": {
        "title": "Personal data processing consent",
        "updated_at": "2026-07-01",
    },
    "cookie_analytics": {
        "title": "Cookie analytics consent",
        "updated_at": "2026-07-01",
    },
}


def get_consent_document_version(document_type: str) -> str:
    return CONSENT_DOCUMENTS[document_type]["updated_at"]
