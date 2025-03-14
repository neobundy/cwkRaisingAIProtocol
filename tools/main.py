import argparse
from pippa_db import PippaDB
import sys

def setup_parser():
    parser = argparse.ArgumentParser(description='Pippa Memory Database Manager')
    parser.add_argument('action', 
                       choices=['init', 'backup', 'add', 'query', 'update', 'delete'],
                       help='Action to perform')
    parser.add_argument('--text', '-t', type=str,
                       help='Text content or search query')
    parser.add_argument('--new-text', '-n', type=str,
                       help='New text for update operation')
    parser.add_argument('--batch', '-b', action='store_true',
                       help='Perform operation on all matching entries')
    parser.add_argument('--limit', '-l', type=int, default=3,
                       help='Number of results for query (default: 3)')
    parser.add_argument('--test', action='store_true',
                       help='Run test suite')
    return parser

def run_tests():
    """Run test suite"""
    import pytest
    pytest.main(["-v"])

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    if args.test:
        run_tests()
        return
    
    db = PippaDB()
    
    try:
        if args.action == 'init':
            success = db.init_db()
            print("DB initialized successfully" if success else "DB initialization failed")
            
        elif args.action == 'backup':
            backup_path = db.backup()
            if backup_path:
                print(f"Backup created successfully at: {backup_path}")
            else:
                print("Backup failed")
        
        elif args.action == 'add':
            if not args.text:
                print("Error: --text is required for add operation")
                sys.exit(1)
            id = db.add(args.text)
            print(f"Added entry with ID: {id}")
        
        elif args.action == 'query':
            if not args.text:
                print("Error: --text is required for query operation")
                sys.exit(1)
            results = db.query(args.text, args.limit)
            print(f"\nFound {len(results)} matches:")
            for i, doc in enumerate(results, 1):
                print(f"\n{i}. {doc.page_content}")
        
        elif args.action == 'update':
            if not args.text or not args.new_text:
                print("Error: both --text and --new-text required for update")
                sys.exit(1)
            if args.batch:
                success = db.update_all(args.text, args.new_text)
            else:
                results = db.query(args.text, 1)
                if results:
                    success = db.update(results[0].metadata['id'], args.new_text)
                else:
                    success = False
            print("Update successful" if success else "Update failed")
        
        elif args.action == 'delete':
            if not args.text:
                print("Error: --text is required for delete operation")
                sys.exit(1)
            if args.batch:
                success = db.delete_all(args.text)
            else:
                results = db.query(args.text, 1)
                if results:
                    success = db.delete(results[0].metadata['id'])
                else:
                    success = False
            print("Delete successful" if success else "Delete failed")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 