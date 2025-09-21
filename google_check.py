#!/usr/bin/env python3

import os
from google.cloud import storage
from google.auth import default
from dotenv import load_dotenv
load_dotenv()

def test_authentication():
    """Test Google Cloud authentication and permissions."""
    
    # Check if credentials environment variable is set
    creds_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    print(f"GOOGLE_APPLICATION_CREDENTIALS: {creds_path}")
    
    if not creds_path:
        print("❌ GOOGLE_APPLICATION_CREDENTIALS not set")
        return False
    
    if not os.path.exists(creds_path):
        print(f"❌ Credentials file not found: {creds_path}")
        return False
    
    print(f"✅ Credentials file exists: {creds_path}")
    
    try:
        # Test default credentials
        credentials, project_id = default()
        print(f"✅ Default credentials loaded successfully")
        print(f"Project ID: {project_id}")
        
        # Test Storage client initialization
        client = storage.Client()
        print(f"✅ Storage client initialized successfully")
        print(f"Client project: {client.project}")
        
        # List accessible buckets (optional - comment out if you don't want to list all)
        print("\nTesting bucket access...")
        try:
            buckets = list(client.list_buckets())
            print(f"✅ Found {len(buckets)} accessible buckets:")
            for bucket in buckets[:5]:  # Show first 5 buckets
                print(f"  - {bucket.name}")
            if len(buckets) > 5:
                print(f"  ... and {len(buckets) - 5} more")
        except Exception as e:
            print(f"⚠️  Could not list buckets: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return False

def test_specific_bucket(bucket_name):
    """Test access to a specific bucket."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        
        # Test if bucket exists and is accessible
        if bucket.exists():
            print(f"✅ Bucket '{bucket_name}' is accessible")
            
            # List some objects (optional)
            blobs = list(bucket.list_blobs(max_results=5))
            print(f"Found {len(blobs)} objects (showing first 5):")
            for blob in blobs:
                print(f"  - {blob.name}")
            return True
        else:
            print(f"❌ Bucket '{bucket_name}' not found or not accessible")
            return False
            
    except Exception as e:
        print(f"❌ Error accessing bucket '{bucket_name}': {e}")
        return False

if __name__ == "__main__":
    print("🔐 Testing Google Cloud authentication...")
    print("=" * 50)
    
    # Test basic authentication
    auth_success = test_authentication()
    
    if auth_success:
        print("\n" + "=" * 50)
        # Test specific bucket if needed
        bucket_name = input("Enter bucket name to test (or press Enter to skip): ").strip()
        if bucket_name:
            test_specific_bucket(bucket_name)
    
    print("\n" + "=" * 50)
    if auth_success:
        print("🎉 Authentication test completed successfully!")
    else:
        print("💥 Authentication test failed!")