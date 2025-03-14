import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pippa_db import PippaDB
import shutil
import time

# Use a placeholder API key for testing
os.environ["OPENAI_API_KEY"] = "sk-mock-key-for-testing-purposes-only"

class TestPippaDB:
    @pytest.fixture
    def test_db(self):
        """Create a test DB instance"""
        test_db_path = "./test_vector_db"
        db = PippaDB(db_path=test_db_path)
        yield db
        # Cleanup after tests
        if os.path.exists(test_db_path):
            shutil.rmtree(test_db_path)
    
    def test_init_db(self, test_db):
        """Test DB initialization"""
        assert test_db.init_db() == True
        assert os.path.exists(test_db.db_path)
    
    def test_backup(self, test_db):
        """Test backup functionality"""
        test_db.init_db()
        backup_path = test_db.backup()
        assert backup_path is not None
        assert os.path.exists(backup_path)
    
    def test_add_and_query(self, test_db):
        """Test adding and querying entries"""
        test_db.init_db()
        test_text = "Test memory about Uffizi"
        id = test_db.add(test_text)
        assert id is not None
        
        results = test_db.query("Uffizi")
        assert len(results) > 0
        assert "Uffizi" in results[0].page_content
    
    def test_update(self, test_db):
        """Test updating entries"""
        test_db.init_db()
        original_text = "Original Uffizi memory"
        new_text = "Updated Uffizi memory"
        
        id = test_db.add(original_text)
        assert test_db.update(id, new_text) == True
        
        results = test_db.query("Uffizi")
        assert new_text in results[0].page_content
    
    def test_delete(self, test_db):
        """Test deleting entries"""
        test_db.init_db()
        text = "Memory to delete"
        id = test_db.add(text)
        
        assert test_db.delete(id) == True
        results = test_db.query(text)
        assert len(results) == 0
    
    def test_batch_operations(self, test_db):
        """Test batch operations"""
        test_db.init_db()
        memories = [
            "Uffizi memory 1",
            "Uffizi memory 2",
            "Different memory"
        ]
        ids = test_db.add(memories)
        assert len(ids) == 3
        
        # Test batch update
        assert test_db.update_all("Uffizi", "Updated Uffizi") == True
        results = test_db.query("Uffizi")
        assert all("Updated Uffizi" in r.page_content for r in results)
        
        # Test batch delete
        assert test_db.delete_all("Uffizi") == True
        results = test_db.query("Uffizi")
        assert len(results) == 0
    
    def test_edge_cases(self, test_db):
        """Test edge cases and error handling"""
        test_db.init_db()
        
        # Empty DB queries
        assert len(test_db.query("anything")) == 0
        
        # Empty string handling
        id = test_db.add("")
        assert id is not None  # Should handle empty strings
        
        # Very long text
        long_text = "memory " * 1000
        id = test_db.add(long_text)
        assert id is not None
        
        # Special characters
        special_text = "Memory with 特殊文字 and émojis 🎨"
        id = test_db.add(special_text)
        results = test_db.query("特殊文字")
        assert len(results) > 0 