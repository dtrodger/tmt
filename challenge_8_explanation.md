# Adding an Inventory Item via API

This guide provides an overview of how to add an item to the Inventory using our API.

## Inventory Resource

The Inventory resource contains:
- `name`: A string representing the name of the inventory item.
- `type`: A foreign key linking to the InventoryType resource.
- `language`: A foreign key linking to the InventoryLanguage resource.
- `tags`: A many-to-many relationship with InventoryTag resource.
- `metadata`: A JSON field that stores various attributes like year, actors, ratings, etc.

## POST Method in InventoryListCreateView

Here’s what happens when you send a POST request:
1. **Data Reception**: The JSON data is extracted from the request.
2. **Metadata Handling**: Metadata is validated using Pydantic to ensure it follows expected formats and types.
3. **Serialization**: The data is then processed by InventorySerializer. If there are any issues with the data, such as missing required fields or invalid data types, the serializer will raise validation errors.
4. **Saving Data**: If the serializer is valid, it saves the inventory item to the database.
5. **Response**: A successful save will return the serialized inventory data. Otherwise, it will return an error message.

## Request

Use this `curl` command to add a new inventory item to the system:

```bash
curl -X POST "http://localhost:8000/inventory/" \
     -H "Content-Type: application/json" \
     -d '{
         "name": "New Inventory Item",
         "type": {"id": 1},
         "language": {"id": 1},
         "tags": [{"id": 1}, {"id": 2}],
         "metadata": {
             "year": 2021,
             "actors": ["Actor A", "Actor B"],
             "imdb_rating": "7.5",
             "rotten_tomatoes_rating": 85
         }
     }'
```

## Respons

### HTTP 201 Created

```json
{
  "id": 1,
  "name": "New Inventory Item",
  "type": {
    "id": 1,
    "name": "Type Name"
  },
  "language": {
    "id": 1,
    "name": "Language Name"
  },
  "tags": [
    {
      "id": 1,
      "name": "Tag 1",
      "is_active": true
    },
  ],
  "metadata": {
    "year": 2021,
    "actors": ["Actor A", "Actor B"],
    "imdb_rating": 7.5,
    "rotten_tomatoes_rating": 85
  }
}
```
### HTTP 400 Bad Request

```json
    {
    "name": ["This field is required."],
    "type": ["This field must be a dictionary with an 'id' key."],
    "metadata": ["Invalid data format: 'year' must be an integer."]
    }
```