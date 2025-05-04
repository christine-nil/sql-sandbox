#!/usr/bin/env python3
"""
Reset script for the SQL Learning Sandbox database.
This script removes the existing database and recreates it with fresh data.
"""

import os
import sys
import importlib.util

def main():
    """Reset the database by running the create_database function."""
    print("\nSQL Learning Sandbox - Database Reset")
    print("====================================")
    
    if not os.path.exists('sandbox.db'):
        print("\n❌ No existing database found. Please run build-sandbox.py first.")
        sys.exit(1)
    
    try:
        # Import the function directly here instead
        spec = importlib.util.spec_from_file_location("build_sandbox", "build-sandbox.py")
        build_sandbox = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build_sandbox)
        
        build_sandbox.create_database()  # This will handle the confirmation prompt
        print("\n✅ Database reset completed successfully!")
    except KeyboardInterrupt:
        print("\n\nReset cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error resetting database: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
