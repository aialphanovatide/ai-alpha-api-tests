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

BOTS_SCHEMA = {
    "type": "object",
    "properties": {
    "alias": { "type": ["string", "null"] },
    "background_color": { "type": ["string", "null"] },
    "category_id": { "type": "integer" },
    "created_at": { "type": ["string", "null"], "format": "date-time" },
    "dalle_prompt": { "type": ["string", "null"] },
    "icon": { "type": ["string", "null"], "format": "uri" },
    "id": { "type": "integer" },
    "is_active": { "type": "boolean" },
    "last_run_status": { "type": ["string", "null"] },
    "last_run_time": { "type": ["string", "null"], "format": "date-time" },
    "name": { "type": "string" },
    "next_run_time": { "type": ["string", "null"], "format": "date-time" },
    "prompt": { "type": ["string", "null"] },
    "run_count": { "type": ["integer", "null"] },
    "run_frequency": { "type": "string" },
    "status": { "type": ["string", "null"] },
    "updated_at": { "type":  ["null", "string"], "format": "date-time" }
    },
    "required": [
    "alias",
    "background_color",
    "category_id",
    "created_at",
    "dalle_prompt",
    "icon",
    "id",
    "is_active",
    "last_run_status",
    "last_run_time",
    "name",
    "next_run_time",
    "prompt",
    "run_count",
    "run_frequency",
    "status",
    "updated_at"
    ]
}

NEWS_BOTS_CATEGORY_SCHEMA = {
    "type": "object",
    "properties": {
    "alias": { "type": "string" },
    "border_color": { "type": "string" },
    "bots": {
        "type": "array",
        "items": BOTS_SCHEMA
    },
    "created_at": { "type": "string", "format": "date-time" },
    "icon": { "type": "string" },
    "id": { "type": "integer" },
    "is_active": { "type": "boolean" },
    "name": { "type": "string" },
    "slack_channel": { "type": "string" },
    "updated_at": { "type":  ["null", "string"], "format": "date-time" }
    },
    "required": [
        "alias",
        "name"
    ]
}

NEWS_BOT_CATEGORY_RESPONSE_SCHEMA = { 
    "type": "object",
    "properties": {
        "data": NEWS_BOTS_CATEGORY_SCHEMA,
        "error": { "type": ["null", "string"] },
        "success": { "type": "boolean" }
    }
 }

NEWS_BOTS_CATEGORIES_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
        "type": "object",
        "properties": {
            "categories": {
            "type": "array",
            "items": NEWS_BOTS_CATEGORY_SCHEMA,
            },
        },
        "required": ["categories"]
        },
        "error": { "type": ["null", "string"] },
        "success": { "type": "boolean" }
    },
    "required": ["error", "success"]
}

NEWS_BOTS_CATEGORY_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
        "type": "object",
        "properties": {
            "category": NEWS_BOTS_CATEGORY_SCHEMA
            }
        },
        "error": { "type": ["null", "string"] },
        "success": { "type": "boolean" }
    },
    "required": ["error", "success"]
}

NEWS_BOTS_SCHEMA = {
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alias": { "type": ["null", "string"] },
          "background_color": { "type": ["null", "string"] },
          "category_id": { "type": "integer" },
          "created_at": { "type": ["null", "string"], "format": "date-time" },
          "dalle_prompt": { "type": ["null", "string"] },
          "icon": { "type": ["null", "string"] },
          "id": { "type": "integer" },
          "is_active": { "type": "boolean" },
          "name": { "type": "string" },
          "prompt": { "type": ["null", "string"] },
          "run_frequency": { "type": "string" },
          "updated_at": { "type": ["null", "string"], "format": "date-time" }
        },
        "required": [
          "alias",
          "background_color",
          "category_id",
          "created_at",
          "dalle_prompt",
          "icon",
          "id",
          "is_active",
          "name",
          "prompt",
          "run_frequency",
          "updated_at"
        ]
      }
    },
    "success": { "type": "boolean" }
  },
  "required": ["data", "success"]
}

POST_NEWS_BOT_RESPONSE = {
  "type": "object",
  "properties": {
    "bot": {
      "type": "object",
      "properties": {
        "alias": { "type": "string" },
        "background_color": { "type": "string", "format": "color" },
        "category_id": { "type": "integer" },
        "created_at": { "type": "string", "format": "date-time" },
        "dalle_prompt": { "type": "string" },
        "icon": { "type": "string", "format": "uri" },
        "id": { "type": "integer" },
        "is_active": { "type": "boolean" },
        "last_run_status": { "type": ["string", "null"] },
        "last_run_time": { "type": ["string", "null"], "format": "date-time" },
        "name": { "type": "string" },
        "next_run_time": { "type": ["string", "null"], "format": "date-time" },
        "prompt": { "type": "string" },
        "run_count": { "type": "integer" },
        "run_frequency": { "type": "integer" },
        "status": { "type": "string" },
        "updated_at": { "type": "string", "format": "date-time" }
      },
      "required": [
        "alias",
        "background_color",
        "category_id",
        "created_at",
        "dalle_prompt",
        "icon",
        "id",
        "is_active",
        "name",
        "run_count",
        "run_frequency",
        "status",
        "updated_at"
      ]
    },
    "data": { "type": ["object", "null"] },
    "error": { "type": ["object", "null", "string"] },
    "message": { "type": "string" },
    "success": { "type": "boolean" }
  }
}

NEWS_BOT_METRICS_SCHEMA = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "metrics": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "articles_processed": { "type": "integer" },
              "articles_saved": { "type": "integer" },
              "bot_id": { "type": "integer" },
              "cpu_percent": { "type": "number" },
              "end_time": { "type": ["string", "null"], "format": "date-time" },
              "error_reasons": { "type": ["string", "null"] },
              "filter_reasons": { "type": ["string", "null"] },
              "id": { "type": "integer" },
              "memory_percent": { "type": "number" },
              "start_time": { "type": ["string", "null"], "format": "date-time" },
              "total_articles_found": { "type": "integer" },
              "total_errors": { "type": "integer" },
              "total_filtered": { "type": "integer" },
              "total_runtime": { "type": ["string", "null"] }
            },
            "required": [
              "articles_processed",
              "articles_saved",
              "bot_id",
              "cpu_percent",
              "end_time",
              "error_reasons",
              "filter_reasons",
              "id",
              "memory_percent",
              "start_time",
              "total_articles_found",
              "total_errors",
              "total_filtered",
              "total_runtime"
            ]
          }
        },
        "pagination": {
          "type": "object",
          "properties": {
            "current_page": { "type": "integer" },
            "has_next": { "type": "boolean" },
            "has_prev": { "type": "boolean" },
            "per_page": { "type": "integer" },
            "total_items": { "type": "integer" },
            "total_pages": { "type": "integer" }
          },
          "required": [
            "current_page",
            "has_next",
            "has_prev",
            "per_page",
            "total_items",
            "total_pages"
          ]
        }
      },
      "required": ["metrics", "pagination"]
    },
    "error": { "type": ["string", "null"] },
    "success": { "type": "boolean" }
  },
  "required": ["data", "error", "success"]
}

NEWS_BOT_RESPONSE_SCHEMA = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "alias": { "type": "string" },
        "background_color": { "type": "string" },
        "blacklist": {
          "type": "array",
          "items": { "type": "string" }
        },
        "category_id": { "type": "integer" },
        "created_at": { "type": ["string", "null"], "format": "date-time" },
        "dalle_prompt": { "type": "string" },
        "icon": { "type": "string", "format": "uri" },
        "id": { "type": "integer" },
        "is_active": { "type": "boolean" },
        "keywords": {
          "type": "array",
          "items": { "type": "string" }
        },
        "last_run_status": { "type": ["string", "null"] },
        "last_run_time": { "type": ["string", "null"], "format": "date-time" },
        "name": { "type": "string" },
        "next_run_time": { "type": ["string", "null"], "format": "date-time" },
        "prompt": { "type": "string" },
        "run_count": { "type": ["integer", "null"] },
        "run_frequency": { "type": "string" },
        "site": {
          "type": "object",
          "properties": {
            "bot_id": { "type": "integer" },
            "created_at": { "type": ["string", "null"], "format": "date-time" },
            "id": { "type": "integer" },
            "name": { "type": "string" },
            "updated_at": { "type": ["string", "null"], "format": "date-time" },
            "url": { "type": "string", "format": "uri" }
          },
          "required": ["bot_id", "id", "name", "url"]
        },
        "status": { "type": ["string", "null"] },
        "updated_at": { "type": "string", "format": "date-time" }
      },
      "required": [
        "alias",
        "background_color",
        "blacklist",
        "category_id",
        "dalle_prompt",
        "icon",
        "id",
        "is_active",
        "keywords",
        "name",
        "prompt",
        "run_frequency",
        "site",
        "status",
        "updated_at"
      ]
    },
    "error": { "type": ["string", "null"] },
    "success": { "type": "boolean" }
  },
  "required": ["data", "error", "success"]
}

USER = {
  "type": "object",
  "properties": {
    "auth0id": { "type": ["string", "null"]},
    "auth_token": { "type": "string" },
    "birth_date": { "type": ["string", "null"] },
    "created_at": { "type": "string", "format": "date-time" },
    "email": { "type": "string", "format": "email" },
    "email_verified": { "type": ["string", "boolean"]},
    "full_name": { "type": "string" },
    "nickname": { "type": "string" },
    "picture": { "type": ["string", "null"] },
    "provider": { "type": ["string", "null"] },
    "purchased_plans": {
      "type": "array",
      "items": { "type": "object" }
    },
    "updated_at": { "type": "string", "format": "date-time" },
    "user_id": { "type": "integer" }
  },
  "required": [
  "auth0id",
  "auth_token",
  "created_at",
  "email",
  "email_verified",
  "full_name",
  "nickname",
  "updated_at",
  "user_id"
  ]
}

USERS_SCHEMA = {
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": USER
    },
    "message": { "type": "string" },
    "pagination": { "type": ["object", "null"] },
    "success": { "type": "boolean" }
  },
  "required": ["data", "message"]
}

USER_SCHEMA = {
  "type": "object",
  "properties": {
    "message": { "type": ["string", "object"] },
    "success": { "type": "boolean" },
    "user": USER
  },
  "required": ["message", "success"]
}

USER_RESPONSE_SCHEMA = {
  "type": "object",
  "properties": {
    "data": USER,
    "message": { "type": "string" },
    "success": { "type": "boolean" }
  },
  "required": ["data", "message", "success"]
}