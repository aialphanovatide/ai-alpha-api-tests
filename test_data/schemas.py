COIN_SCHEMA ={
    "type": ["object", "null"],
    "properties": {
        "alias": {"type": ["string", "null"]},
        "background_color": {"type": ["string", "null"]},
        "bot_id": {"type": "integer"},
        "category_id": {"type": ["integer", "string"]},
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

COIN_RESPONSE_SCHEMA = {
   "type": "object",
    "properties": {
        "coin": COIN_SCHEMA,
        "error": {"type": ["string", "null"]},
        "success": {"type": "boolean"},
    },
    "required": ["coin", "error", "success"] 
}

COINS_RESPONSE_SCHEMA = {
   "type": "object",
    "properties": {
        "coins": {
            "type": "array", 
            "items": COIN_SCHEMA
            },
        "error": {"type": ["string", "null"]},
        "success": {"type": "boolean"},
    },
    "required": ["coins", "error", "success"] 
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

CHART_SCHEMA = {
    "type": ["object", "null"],
    "properties": {
        "chart_id": {"type": "integer"},
        "coin_bot_id": {"type": "integer"},
        "created_at": {"type": "string", "format": "date-time"},
        "is_essential": {"type": "boolean"},
        "pair": {"type": "string"},
        "resistance_1": {"type": "number"},
        "resistance_2": {"type": "number"},
        "resistance_3": {"type": "number"},
        "resistance_4": {"type": "number"},
        "support_1": {"type": "number"},
        "support_2": {"type": "number"},
        "support_3": {"type": "number"},
        "support_4": {"type": "number"},
        "temporality": {"type": "string"},
        "token": {"type": "string"},
        "updated_at": {"type": "string", "format": "date-time"}
    },
    "required": [
        "chart_id",
        "coin_bot_id",
        "created_at",
        "is_essential",
        "pair",
        "resistance_1",
        "resistance_2",
        "resistance_3",
        "resistance_4",
        "support_1",
        "support_2",
        "support_3",
        "support_4",
        "temporality",
        "token",
        "updated_at"
    ]
}

DATA_ITEM_SCHEMA = {
    "type": "object",
    "properties": {
        "close": {"type": "number"},
        "date": {"type": "string", "format": "date-time"},
        "high": {"type": "number"},
        "low": {"type": "number"},
        "open": {"type": "number"}
    },
    "required": ["close", "date", "high", "low", "open"]
}

DATA_ARRAY_SCHEMA = {
    "type": "array",
    "items": DATA_ITEM_SCHEMA
}

CHART_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {"anyOf": [CHART_SCHEMA, DATA_ARRAY_SCHEMA]},
        "error": {"type": ["string", "null"]},
        "message": {"type": ["string", "null"]},
        "status": {"type": "integer"}
    },
    "required": ["data", "error", "message", "status"]
}

CHART_GET_SCHEMA = {
  "type": "object",
  "properties": {
    "error": {
      "type": ["null", "string"]
    },
    "message": CHART_SCHEMA,
    "status": {
      "type": "integer"
    }
  },
  "required": ["error", "message", "status"]
}

TOP_MOVERS_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
        "type": "object",
        "properties": {
            "top_10_gainers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                "current_price": { "type": "number" },
                "id": { "type": "string" },
                "image": { "type": "string", "format": "uri" },
                "last_updated": { "type": "string", "format": "date-time" },
                "name": { "type": "string" },
                "price_change_percentage_24h": { "type": "number" },
                "symbol": { "type": "string" }
                },
                "required": [
                "current_price",
                "id",
                "image",
                "last_updated",
                "name",
                "price_change_percentage_24h",
                "symbol"
                ]
            }
            },
            "top_10_losers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                "current_price": { "type": "number" },
                "id": { "type": "string" },
                "image": { "type": "string", "format": "uri" },
                "last_updated": { "type": "string", "format": "date-time" },
                "name": { "type": "string" },
                "price_change_percentage_24h": { "type": "number" },
                "symbol": { "type": "string" }
                },
                "required": [
                "current_price",
                "id",
                "image",
                "last_updated",
                "name",
                "price_change_percentage_24h",
                "symbol"
                ]
            }
            }
        },
        "required": ["top_10_gainers", "top_10_losers"]
        },
        "order": { "type": "string" },
        "success": { "type": "boolean" }
    },
    "required": ["data", "order", "success"]
}

OHLC_DATA_ITEMS_SCHEMA = {
    "type": "array",
    "minItems": 5,
    "maxItems": 5
}

OHLC_CHART_SCHEMA = {
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": OHLC_DATA_ITEMS_SCHEMA
    },
    "error": {
      "type": ["string", "null"]
    }
  },
  "required": ["data", "error"]
}
