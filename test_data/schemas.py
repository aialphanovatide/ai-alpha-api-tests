COIN_SCHEMA ={
    "type": "object",
    "properties": {
        "alias": {"type": ["string", "null"]},
        "background_color": {"type": "null"},
        "bot_id": {"type": "integer"},
        "category_id": {"type": "integer"},
        "created_at": {"type": "string"},
        "gecko_id": {"type": "string"},
        "icon": {"type": "string"},
        "is_active": {"type": "boolean"},
        "name": {"type": "string"},
        "symbol": {"type": "string"},
        "updated_at": {"type": "string"},

    },
    "required": ["alias", "background_color", "bot_id", "category_id", "created_at",
                 "gecko_id", "icon", "is_active", "name", "symbol", "updated_at"]

}

CATEGORY_SCHEMA = {
    "type": ["object", "null"],
    "properties": {
        "alias": {"type": "string"},
        "border_color": {"type": ["string", "null"]},
        "category_id": {"type": "integer"},
        "coins": {"type": "array", "items": COIN_SCHEMA},
        "created_at": {"type": "string"},
        "icon": {"type": ["string", "null"]},
        "is_active": {"type": "boolean"},
        "name": {"type": "string"},
        "updated_at": {"type": "string"},
    },
    "required": ["alias", "name", "category_id", "created_at"]
}

CATEGORIES_RESPONSE_SCHEMA = {
   "type": "object",
    "properties": {
        "categories": {
            "type": "array", 
            "items": CATEGORY_SCHEMA
            },
        "error": {"type": ["string", "null"]},
        "success": {"type": "boolean"},
    },
    "required": ["categories", "error", "success"] 
}

CATEGORY_RESPONSE_SCHEMA = {
   "type": "object",
    "properties": {
        "category": CATEGORY_SCHEMA,
        "error": {"type": ["string", "null"]},
        "success": {"type": "boolean"},
    },
    "required": ["category", "error", "success"] 
}