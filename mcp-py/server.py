import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastmcp import FastMCP

base_dir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = "sqlite:///" + os.path.join(base_dir, "app.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a simple model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

Base.metadata.create_all(bind=engine)

mcp = FastMCP("Sample")

@mcp.tool()
def create_item(name: str, description: str = "") -> str:
    """Create a new item with the given name and description."""
    db = SessionLocal()
    try:
        new_item = Item(name=name, description=description)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return f"Item created successfully with ID: {new_item.id}"
    except Exception as e:
        db.rollback()
        return f"Error creating item: {str(e)}"
    finally:
        db.close()


@mcp.tool()
def get_item(item_id: int) -> str:
    """Get an item by its ID."""
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            return f"Item ID: {item.id}, Name: {item.name}, Description: {item.description}"
        else:
            return f"Item with ID {item_id} not found"
    except Exception as e:
        return f"Error retrieving item: {str(e)}"
    finally:
        db.close()


@mcp.tool()
def get_all_items() -> str:
    """Get all items from the database."""
    db = SessionLocal()
    try:
        items = db.query(Item).all()
        if not items:
            return "No items found in the database"
        
        result = "All items:\n"
        for item in items:
            result += f"- ID: {item.id}, Name: {item.name}, Description: {item.description}\n"
        return result
    except Exception as e:
        return f"Error retrieving items: {str(e)}"
    finally:
        db.close()


@mcp.tool()
def delete_item(item_id: int) -> str:
    """Delete an item by its ID."""
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
            return f"Item with ID {item_id} deleted successfully"
        else:
            return f"Item with ID {item_id} not found"
    except Exception as e:
        db.rollback()
        return f"Error deleting item: {str(e)}"
    finally:
        db.close()



if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000) #streamable http
    #mcp.run(transport="sse", host="127.0.0.1", port=8000) #sse
