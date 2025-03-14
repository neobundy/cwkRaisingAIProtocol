from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from typing import List, Dict, Optional
import shutil
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PippaDB:
    def __init__(self, db_path: str = "./vector_db"):
        self.db_path = db_path
        self.embedding = OpenAIEmbeddings()
        self.db = Chroma(
            persist_directory=db_path,
            embedding_function=self.embedding
        )
    
    def backup(self) -> str:
        """Create a backup of the current DB"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = f"backups/pippa_db_{timestamp}"
            os.makedirs("backups", exist_ok=True)
            
            if os.path.exists(self.db_path):
                shutil.copytree(self.db_path, backup_path)
                return backup_path
            return None
        except Exception as e:
            print(f"Error creating backup: {e}")
            return None
    
    def init_db(self) -> bool:
        """Initialize DB (with automatic backup if exists)"""
        try:
            # Backup if exists
            if os.path.exists(self.db_path):
                backup_path = self.backup()
                if backup_path:
                    print(f"Existing DB backed up to: {backup_path}")
                    
                # Remove existing DB
                shutil.rmtree(self.db_path)
            
            # Initialize fresh DB
            os.makedirs(self.db_path, exist_ok=True)
            self.db = Chroma(
                persist_directory=self.db_path,
                embedding_function=self.embedding
            )
            return True
        except Exception as e:
            print(f"Error initializing DB: {e}")
            return False
    
    def add(self, text: str | List[str], metadata: Optional[Dict | List[Dict]] = None) -> str | List[str]:
        """Add single or multiple entries"""
        try:
            texts = [text] if isinstance(text, str) else text
            metas = [metadata] if metadata and not isinstance(metadata, list) else metadata
            
            ids = self.db.add_texts(texts, metadatas=metas)
            self.db.persist()
            return ids[0] if isinstance(text, str) else ids
        except Exception as e:
            print(f"Error adding entries: {e}")
            return None
    
    def query(self, text: str, limit: int = 3) -> list:
        """Search similar entries"""
        try:
            return self.db.similarity_search(text, k=limit)
        except Exception as e:
            print(f"Error querying: {e}")
            return []
    
    def update_all(self, query: str, new_text: str) -> bool:
        """Update all entries matching query"""
        try:
            matches = self.db.similarity_search(query)
            if not matches:
                return False
            
            # Get all IDs
            ids = [doc.metadata.get('id') for doc in matches]
            
            # Delete old entries
            self.db.delete(ids)
            
            # Add new entries with same IDs
            self.db.add_texts([new_text] * len(ids), ids=ids)
            self.db.persist()
            return True
        except Exception as e:
            print(f"Error batch updating: {e}")
            return False
    
    def delete_all(self, query: str) -> bool:
        """Delete all entries matching query"""
        try:
            matches = self.db.similarity_search(query)
            if not matches:
                return False
            
            ids = [doc.metadata.get('id') for doc in matches]
            self.db.delete(ids)
            self.db.persist()
            return True
        except Exception as e:
            print(f"Error batch deleting: {e}")
            return False 