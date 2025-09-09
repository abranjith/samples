import asyncio
from fastmcp import Client

#simple client
async def test_client():
    async with Client("http://localhost:8000/mcp") as client:
        #create item
        result = await client.call_tool("create_item", {"name": "Test Item", "description": "This is a test item."})
        print(f"Create item result: {result}")
        print("-" * 40)

        await asyncio.sleep(1)
        #get all items
        result = await client.call_tool("get_all_items", {})
        print(f"Get all items result: {result}")
        print("-" * 40)
        
        await asyncio.sleep(1)
        #delete item
        result = await client.call_tool("delete_item", {"item_id": 1})
        print(f"Delete item result: {result}")

if __name__ == "__main__":
    asyncio.run(test_client())