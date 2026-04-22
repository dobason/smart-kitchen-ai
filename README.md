# Cookbook API

AI-powered API that detects ingredients from images and generates recipes.

## Endpoints

Base path: `/api/v1/recipe`

---

### POST `/api/v1/recipe/ingredients`

Upload a food image to detect ingredients.

**Headers**

| Header | Type | Default | Description |
|--------|------|---------|-------------|
| `Accept-Language` | `string` | `en` | Language for ingredient names in the response |

**Request**

`multipart/form-data`

| Field | Type | Description |
|-------|------|-------------|
| `file` | file | Image file of food/ingredients |

**Response**

```json
{
  "image_obj": {
    "image_name": "uuid.jpg",
    "presigned_url": "http://...",
    "bucket_name": "smart-kitchen-vn"
  },
  "ingredients": ["chicken", "garlic", "onion"]
}
```

**Example**

```bash
curl -X POST http://localhost:8000/api/v1/recipe/ingredients \
  -H "Accept-Language: vi" \
  -F "file=@/path/to/image.jpg"
```

---

### POST `/api/v1/recipe/instruction`

Generate a recipe from a list of ingredients.

**Headers**

| Header | Type | Default | Description |
|--------|------|---------|-------------|
| `Accept-Language` | `string` | `en` | Language for the recipe response |

**Request**

`application/json`

```json
{
  "ingredients": ["chicken", "garlic", "onion"],
  "preference": {
    "dietary_restrictions": "no pork",
    "cuisine_preferences": "Asian",
    "flavor_profiles": "spicy",
    "time_constraints": "30 minutes",
    "specific_note": "kid-friendly"
  }
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ingredients` | `string[]` | yes | List of available ingredients |
| `preference` | object | no | Cooking preferences (all fields optional) |

**Response**

```json
{
  "dish": "Garlic Chicken Stir-fry",
  "ingredients": ["chicken breast", "garlic", "onion", "soy sauce"],
  "steps": [
    "Cut chicken into bite-sized pieces.",
    "Sauté garlic and onion until fragrant.",
    "Add chicken and cook through.",
    "Season with soy sauce and serve."
  ],
  "time": "25 minutes"
}
```

**Example**

```bash
curl -X POST http://localhost:8000/api/v1/recipe/instruction \
  -H "Content-Type: application/json" \
  -H "Accept-Language: vi" \
  -d '{"ingredients": ["chicken", "garlic", "onion"]}'
```

---

## Running locally

```bash
uv run python main.py
```

API docs available at `http://localhost:8000/docs`.
